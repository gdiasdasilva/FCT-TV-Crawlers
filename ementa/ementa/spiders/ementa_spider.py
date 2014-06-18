from scrapy.spider import Spider
from scrapy.selector import Selector
from ementa.items import EmentaItem

class EmentaSpider(Spider):
    name = "ementa"
    allowed_domains = ["http://sas.unl.pt/cantina"]
    start_urls = [
        "http://sas.unl.pt/cantina"
    ]

    def parse(self, response):
    	sel = Selector(response)
    	item = EmentaItem()
    	item['soup'] = sel.xpath('//div[contains(., "ncias e Tecnologia")]/div[@class="lunch"]/ul/li[1]/span[@class="dish"]/text()').extract()
    	item['diet'] = sel.xpath('//div[contains(., "ncias e Tecnologia")]/div[@class="lunch"]/ul/li[2]/span[@class="dish"]/text()').extract()
    	item['dish'] = sel.xpath('//div[contains(., "ncias e Tecnologia")]/div[@class="lunch"]/ul/li[3]/span[@class="dish"]/text()').extract()
        return item