import scrapy


class QuoteSpider(scrapy.Spider):
    name = "lyric"
    start_urls = ['https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.html']

    def parse(self, response):
        print('hello world')
        finalPage = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="box_pageview"]/a/@href')[-1].extract();
        totalPage = int(finalPage.split(".")[-2])
        for page in range(totalPage):
            link = finalPage.replace(str(totalPage), str(page+1))
            yield scrapy.Request(link, callback=self.crawlLyric)

    def crawlLyric(self, response):
        for linkLyric in response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="list_music_full"]/div[@class="fram_select"]/ul[@class="list_item_music"]/li/a[@class="button_new_window"]/@href').extract():
            yield scrapy.Request(linkLyric, callback=self.saveFile)

    def saveFile(self, response):
        lyricRaw = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="lyric"]/p[@id="divLyric"]/text()').extract()
        lyric = "\n".join(lyricRaw[1:])
        print(lyric)