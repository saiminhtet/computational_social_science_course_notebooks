# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

#each item is a page
class WikicrawlerItem(Item):
    # define the fields for your item here like:
    name = Field()
    url = Field()
    #text = Field()
    #header = Field()