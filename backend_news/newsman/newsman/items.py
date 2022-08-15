# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def isna_url_fixer(url):
    return 'https://www.isna.ir' + url

class IsnaNewsItem(scrapy.Item):
    a_title = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    b_url = scrapy.Field(input_processor = MapCompose(isna_url_fixer))
    c_image = scrapy.Field()
    d_short_description = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    e_time = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())



def iribnews_url_fixer(url):
    return 'https://www.iribnews.ir' + url

class IribnewsItem(scrapy.Item):
    a_title = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    b_url = scrapy.Field(input_processor = MapCompose(iribnews_url_fixer))
    c_image = scrapy.Field(input_processor = MapCompose(iribnews_url_fixer))
    d_short_description = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    #e_time = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())



def rasanews_url_fixer(url):
    return 'https://rasanews.ir' + url

class RasanewsItem(scrapy.Item):
    a_title = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    b_url = scrapy.Field(input_processor = MapCompose(rasanews_url_fixer))
    c_image = scrapy.Field(input_processor = MapCompose(rasanews_url_fixer))
    d_short_description = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    #e_time = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())


def roozno_url_fixer(url):
    return 'https://roozno.com' + url

class RooznonewsItem(scrapy.Item):
    a_title = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    b_url = scrapy.Field(input_processor = MapCompose(roozno_url_fixer))
    c_image = scrapy.Field(input_processor = MapCompose(roozno_url_fixer))
    d_short_description = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    #e_time = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())


def tasnimnews_url_fixer(url):
    return 'https://www.tasnimnews.com' + url

class TasnimnewsItem(scrapy.Item):
    a_title = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    b_url = scrapy.Field(input_processor = MapCompose(tasnimnews_url_fixer))
    c_image = scrapy.Field()
    d_short_description = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
    e_time = scrapy.Field(input_processor = MapCompose(remove_tags), output_procesor = TakeFirst())
