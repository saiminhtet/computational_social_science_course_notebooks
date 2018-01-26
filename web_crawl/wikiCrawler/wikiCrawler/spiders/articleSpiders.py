import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from items import WikicrawlerItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class ArticleSpider(CrawlSpider):
    ''' spiders for pages in each wiki article'''
    name = "wiki_pages"
    allowed_domains = ["en.wikipedia.org"]
    #identify a list of start urls for scraping
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page", "https://en.wikipedia.org/wiki/History_of_Python"]
    # Denying certain wikipedia pages not providing us with good content
    rules = (Rule(LinkExtractor(deny=[
        "https://en\.wikipedia\.org/wiki/Wikipedia.*",
        "https://en\.wikipedia\.org/wiki/Main_Page",
        "https://en\.wikipedia\.org/wiki/Free_Content",
        "https://en\.wikipedia\.org/wiki/Talk.*",
        "https://en\.wikipedia\.org/wiki/Portal.*",
        "https://en\.wikipedia\.org/wiki/Special.*"
    ]), callback='parse_wiki'),)
    
    def parse_wiki(self, response):
        item = WikicrawlerItem()
        soup = BeautifulSoup(response.body)
        
        item['url'] = response.url
        item['name'] = soup.find("h1", {"id": "firstHeading"}).string
                
        return item