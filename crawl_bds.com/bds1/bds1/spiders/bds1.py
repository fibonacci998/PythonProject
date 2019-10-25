from __future__ import absolute_import
import scrapy
from bds1.items import Bds1Item
from scrapy_splash import SplashRequest

class bdsSpider(scrapy.Spider):
    name = "bds1"
    start_urls = ['https://batdongsan.com.vn/tags/ban/tran-duy-hung']
    list = []

    def start_request(self):
        for url in self.start_urls:
            # yield SplashRequest(url=url, callback=self.parse)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        homepage = 'https://batdongsan.com.vn'
        finalPage = response.xpath('//a[(((count(preceding-sibling::*) + 1) = 7) and parent::*)]/@href')[0].extract()
        totalPage = finalPage.split("/")[-1]
        # totalPage = 1
        print("Total page is : "+totalPage[-2:])
        for page in range(int(totalPage[-2:])):
        # for page in range(1):
            link = finalPage.replace(str(totalPage), 'p' + str(page + 1))
            link = homepage + link
            yield scrapy.Request(link, callback=self.crawlDataInsidePage)
            # yield SplashRequest(url=link, callback=self.crawlDataInsidePage)


    def crawlDataInsidePage(self, response):
        homepage = 'https://batdongsan.com.vn'
        for linkEachItem in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p-title", " " ))]//a/@href').extract():
            # print(homepage+"/"+linkEachItem)
            yield scrapy.Request(homepage+"/"+linkEachItem, callback=self.crawlDataInsidePost)
            # yield SplashRequest(url=homepage + "/" + linkEachItem, callback=self.crawlDataInsidePost,args={"wait": 1, "runjs": 'showMap()'})

    def crawlDataInsidePost(self, response):
        type = response.css('.div-hold > .table-detail .row:nth-child(1) .right::text').extract()
        address = response.css('.div-hold > .table-detail .row:nth-child(2) .right::text').extract()

        numberBedrooms = response.css('#LeftMainContent__productDetail_roomNumber .right::text').extract()
        if (len(numberBedrooms) > 0):
            numberBedrooms = numberBedrooms[0].split()[0]

        numberToilets = response.css('#LeftMainContent__productDetail_toilet .right::text').extract()
        if (len(numberToilets) > 0):
            numberToilets = numberToilets[0].split()[0]

        price = response.css('.mar-right-15 strong::text').extract()
        area = response.css('.mar-right-15+ .gia-title strong::text').extract()[0].split('m')[0]
        longitude = response.css('#hdLong::attr(value)').extract()
        latitude = response.css('#hdLat::attr(value)').extract()
        nameOwner = response.css('#LeftMainContent__productDetail_contactName .right::text').extract()
        mobile = response.css('#LeftMainContent__productDetail_contactMobile .right::text').extract()
        email = response.css('#contactEmail a::text').extract()

        sizeFront = response.css('#LeftMainContent__productDetail_frontEnd .right::text').extract()
        if (len(sizeFront) >0):
            sizeFront = sizeFront[0].split()[0]

        numberFloors = response.css('#LeftMainContent__productDetail_floor .right::text').extract()
        if (len(numberFloors) > 0):
            numberFloors = numberFloors[0].split()[0]

        wardin = response.css('#LeftMainContent__productDetail_wardin .right::text').extract()
        if (len(wardin) > 0):
            wardin = wardin[0].split()[0]

        homeDirection = response.css('#LeftMainContent__productDetail_direction .right::text').extract()
        balconyDirection = response.css('#LeftMainContent__productDetail_balcony .right::text').extract()
        interior = response.css('#LeftMainContent__productDetail_interior .right::text').extract()
        projectSize = response.css('#LeftMainContent__productDetail_projectSize .right::text').extract()
        projectName = response.css('#project .row:nth-child(1) .right::text').extract()
        projectOwner = response.css('#LeftMainContent__productDetail_projectOwner .right::text').extract()
        codePost = response.css('.prd-more-info div div::text').extract()
        startDatePost = response.css('.prd-more-info div:nth-child(3)::text').extract()[-1]
        endDatePost = response.css('.prd-more-info div+ div::text').extract()[-1]
        typePost = response.css('.prd-more-info div+ div:nth-child(2)::text').extract()[-1]


        item = Bds1Item()
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
        item['link'] = response.request.url
        item['sizeFront'] = sizeFront
        item['numberFloors'] = numberFloors
        item['wardin'] = wardin
        item['homeDirection'] = homeDirection
        item['balconyDirection'] = balconyDirection
        item['interior'] = interior
        item['projectName'] = projectName
        item['projectSize'] = projectSize
        item['projectOwner'] = projectOwner
        item['codePost'] = codePost
        item['startDatePost'] = startDatePost
        item['endDatePost'] = endDatePost
        item['typePost'] = typePost

        return item
