python-crawlers
===============

Three python scripts to crawl information from FCT-UNL's official website.

I used <a href="http://scrapy.org" target="_blank">Scrapy</a> for the effect. To run each crawler, you just have to be in its root directory and type:
`scrapy crawl spider_name -o outputFileName.json -t json`

For example, to crawl the news from FCT-UNL's website, you'd run:
`scrapy crawl noticias -o myoutput.json -t json`
