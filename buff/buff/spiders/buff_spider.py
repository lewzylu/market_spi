import scrapy
import json

class DmozSpider(scrapy.Spider):
    name = "buff"
    allowed_domains = ["163.com"]
    start_urls = []
    with open("buff/spiders/game_list.csv") as f:
        for line in f:
            tmpstr = line.split(',')
            game = tmpstr[0]
            pagenum = int(tmpstr[1])
            for i in range(pagenum):
                start_urls.append("https://buff.163.com/api/market/goods?game={game}&page_num={page}&sort_by=price.asc".format(game=game, page=i+1))

    def parse(self, response):
        data = response.xpath("/html/body/p/text()").extract()[0]
        # print data
        dt_data = json.loads(data)['data']['items']
        for item in dt_data:
            print item['name']
        # for info in response.xpath('//*[@id="j_list_card"]/ul/li'):
        #     item = BuffItem()
        #     name = info.xpath('li/h3/a').extract()
        #     print name  
            # price = info.xpath('li[@class="selling"]/p[@class="info"]/span/span[@class="price"]/text()').extract()
            # num = info.xpath('li[@class="selling"]/p[@class="info"]/span[@class="num"]/text()').extract()
             
        #     item['name'] = [n.encode('utf-8') for n in name]
        #     item['price'] = [p[2:].encode('utf-8') for p in price]  
        #     item['num'] = [n[:-3].encode('utf-8') for n in num]
        #     yield item
        # next_page = response.xpath('//li[@class="next"]/a/@href')
        # if next_page:
        #     url = response.urljoin(next_page[0].extract())
        #     yield scrapy.Request(url, self.parse)