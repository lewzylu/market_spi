import scrapy
import json
from buff.items import BuffItem
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
        print data
        dt_data = json.loads(data)['data']['items']
        for obj in dt_data:
            item = BuffItem()
            item['id'] = obj['id']
            item['name'] = obj['name']
            item['game'] = obj['game']
            item['market_hash_name'] = obj['market_hash_name']
            item['sell_num'] = obj['sell_num']
            item['sell_min_price'] = obj['sell_min_price']
            item['steam_price'] = obj['goods_info']['steam_price']
            print item  