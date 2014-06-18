from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from noticias.items import NoticiasItem

class NoticiasSpider(CrawlSpider):
    name = "noticias"
    allowed_domains = ["fct.unl.pt"]
    start_urls = [
        "http://www.fct.unl.pt/noticias"
    ]
    rules = [Rule(SgmlLinkExtractor(allow=['/noticias/2014/\d+']), 'parse_noticia')]

    def parse_noticia(self, response):
        sel = Selector(response)
        noticia = NoticiasItem()
        noticia['title'] = sel.css("#content-middle .page-titles::text").extract()
        noticia['description'] = sel.css("#content-middle .node p::text").extract()
        noticia['url'] = response.url
        return noticia