# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Bds1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    numberBedrooms = scrapy.Field()
    numberToilets = scrapy.Field()
    numberFloors = scrapy.Field()
    sizeFront = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    wardin = scrapy.Field()
    homeDirection = scrapy.Field()
    balconyDirection = scrapy.Field()
    interior = scrapy.Field()

    nameOwner = scrapy.Field()
    mobile = scrapy.Field()
    email = scrapy.Field()

    projectName = scrapy.Field()
    projectSize = scrapy.Field()
    projectOwner = scrapy.Field()

    codePost = scrapy.Field()
    startDatePost = scrapy.Field()
    endDatePost = scrapy.Field()
    typePost = scrapy.Field()
    pass
