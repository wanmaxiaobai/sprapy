# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Identity, Compose,MapCompose,Join


class TutorialItem(scrapy.Item):
    text = Field()
    author = Field()
    tags = Field()


class TutorialLoader(ItemLoader):
    default_item_class = TutorialItem

class TutorialtwoItem(scrapy.Item):
    text = Field()
    author = Field()
    tags = Field()