from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http.request import Request
from noticias.items import NoticiasItem

class NoticiasSpider(CrawlSpider):
    name = "noticias"
    allowed_domains = ["fct.unl.pt"]
    start_urls = [
        "http://www.fct.unl.pt/noticias"
    ]

    def parse(self, response):
        sel = Selector(response)
        noticias = sel.css('.views-row')
        items = []
        for noticia in noticias:
            item = NoticiasItem()
            link = "http://www.fct.unl.pt" + noticia.css('.views-field-title a::attr(href)').extract()[0].strip()
            item['date'] = noticia.css('.views-field-created > span::text').extract()[0].strip()
            item = Request(url = link, callback = self.getInfo, meta={'item': item})
            items.append(item)
        return items

    def getInfo(self, response):
        sel = Selector(response)
        item = response.request.meta['item']
        item['title'] = sel.css('#content-middle h1::text').extract()[0]
        item['description'] = sel.css("#content-middle .node .content p ::text").extract()
        item['url'] = response.url
        return item