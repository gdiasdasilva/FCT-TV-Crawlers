from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http.request import Request
from provas.items import ProvasItem

class ProvasSpider(CrawlSpider):
    name = "provas"
    allowed_domains = ["fct.unl.pt"]
    start_urls = [
        "http://www.fct.unl.pt/provas-academicas"
    ]

    def parse(self, response):
        sel = Selector(response)
        provas = sel.css('.views-row')
        items = []
        for prova in provas:
            item = ProvasItem()
            link = "http://www.fct.unl.pt" + prova.css('.views-field-title a::attr(href)').extract()[0].strip()
            item['date'] = prova.css('span.date-display-single::text').extract()[0].strip()
            item['author'] = prova.css('.views-field-title a::text').extract()[0].split(',')[1].strip()
            item = Request(url = link, callback = self.getInfo, meta={'item': item})
            items.append(item)
        return items

    def getInfo(self, response):
        sel = Selector(response)
        item = response.request.meta['item']
        item['url'] = response.url
        item['title'] = sel.css('.node p ::text').extract()
        item['department'] = sel.css('.node .field-field-local-evento .field-item::text').extract()[0].strip()
        item['classroom'] = sel.css('.node .field-field-specific-location .field-item::text').extract()[0].strip()
        return item