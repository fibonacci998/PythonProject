import scrapy
import csv
from nhaccuatui.items import NhaccuatuiItem

class QuoteSpider(scrapy.Spider):
    name = "lyric"
    start_urls = ['https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.html']
    list = []
    def parse(self, response):

        finalPage = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="box_pageview"]/a/@href')[-1].extract()
        totalPage = int(finalPage.split(".")[-2])
        totalPage = 1
        for page in range(totalPage):
            link = finalPage.replace(str(totalPage), str(page + 1))
            list = yield scrapy.Request(link, callback=self.crawlLyric)

        f = open("lyric_text.txt", "a+b", "utf-8")
        for item in range(list):
            f.write(list['name'])
            f.write(list['lyric'])
            f.write(list['link'])
        f.close()

    def crawlLyric(self, response):
        for linkLyric in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "button_new_window", " " ))]/@href').extract():
            yield scrapy.Request(linkLyric, callback=self.saveFile)

    def saveFile(self, response):
        # print('hello world')
        lyricRaw = response.xpath('//*[(@id = "divLyric")]/text()').extract()
        lyric = "\n".join(lyricRaw[1:])
        item = NhaccuatuiItem()
        item['name'] = lyricRaw[0].encode("utf-8")
        item['lyric'] = lyric.encode("utf-8")
        item['link'] = response.url.encode("utf-8")

        print(item['name'])

        # f = open("lyric_text.txt", "w", "utf-8")
        # f.write(lyricRaw[0].encode("utf-8"))
        # f.write(lyric.encode("utf-8"))
        # f.write(response.url.encode("utf-8"))

        yield item
