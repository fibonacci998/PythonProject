# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    numberBedrooms = scrapy.Field()
    numberToilets = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()

    nameOwner = scrapy.Field()
    mobile = scrapy.Field()
    email = scrapy.Field()
    pass
