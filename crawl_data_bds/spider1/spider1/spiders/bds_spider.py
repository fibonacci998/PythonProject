from __future__ import absolute_import
import scrapy
from spider1.items import Spider1Item
from scrapy_splash import SplashRequest

class bdsSpider(scrapy.Spider):
    name = "bds"
    start_urls = ['https://batdongsan.com.vn/tags/ban/tran-duy-hung']
    list = []

    def start_request(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse)
            # yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        homepage = 'https://batdongsan.com.vn'
        finalPage = response.xpath('//a[(((count(preceding-sibling::*) + 1) = 7) and parent::*)]/@href')[0].extract()
        totalPage = finalPage.split("/")[-1]
        # totalPage = 1
        print("Total page is : "+totalPage[-2:])
        # for page in range(int(totalPage[-2:])):
        for page in range(1):
            link = finalPage.replace(str(totalPage), 'p' + str(page + 1))
            link = homepage + link
            # yield scrapy.Request(link, callback=self.crawlDataInsidePage)
            yield SplashRequest(url=link, callback=self.crawlDataInsidePage)


    def crawlDataInsidePage(self, response):
        homepage = 'https://batdongsan.com.vn'
        for linkEachItem in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p-title", " " ))]//a/@href').extract():
            # print(homepage+"/"+linkEachItem)
            # yield scrapy.Request(homepage+"/"+linkEachItem, callback=self.crawlDataInsidePost)
            yield SplashRequest(url=homepage+"/"+linkEachItem, callback=self.crawlDataInsidePost,
                                args={"wait": 5, "runjs": "showMap()", "wait": 1})

    def crawlDataInsidePost(self, response):
        type = response.css('.div-hold > .table-detail .row:nth-child(1) .right::text').extract()
        address = response.css('.div-hold > .table-detail .row:nth-child(2) .right::text').extract()
        numberBedrooms = response.css('#LeftMainContent__productDetail_roomNumber .right::text').extract()
        numberToilets = response.css('#LeftMainContent__productDetail_toilet .right::text').extract()
        price = response.css('.mar-right-15 strong::text').extract()
        area = response.css('.mar-right-15+ .gia-title strong::text').extract()
        longitude = response.css('a .navigate-link::attr(href)')
        latitude = 1

        nameOwner = response.css('#LeftMainContent__productDetail_contactName .right::text').extract()
        mobile = response.css('#LeftMainContent__productDetail_contactMobile .right::text').extract()
        email = response.css('#contactEmail a::text').extract()


        item = Spider1Item()
        item['type'] = type
        item['address'] = address
        item['numberBedrooms'] = numberBedrooms
        item['numberToilets'] = numberToilets
        item['nameOwner'] = nameOwner
        item['mobile'] = mobile
        item['email'] = email
        item['price'] = price
        item['area'] = area
        item['longitude'] = longitude
        item['latitude'] = latitude
        item['link'] = response
        return item
