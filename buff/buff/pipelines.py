# -*- coding: utf-8 -*-
import time
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BuffPipeline(object):
    def __init__(self):
        _time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        try:
            os.makedirs(os.path.expanduser('~/SteamData/'))
        except:
            pass
        self.file = codecs.open(os.path.expanduser(('~/SteamData/{_time}.csv'.format(_time)), 'wb', encoding='utf-8')
    def process_item(self, item, spider):   
        n = len(item['name'])
        #n = len(item['url'])
        for i in range(n):
            self.file.write(item['game'][i].decode("utf-8") + '||')
            self.file.write(item['id'][i].decode("utf-8")  + '||')
            self.file.write(item['name'][i].decode("utf-8") + '||')
            self.file.write(item['market_hash_name'][i].decode("utf-8")  + '||')
            self.file.write(item['sell_min_price'][i].decode("utf-8")  + '||')
            self.file.write(item['sell_num'][i].decode("utf-8")  + '||')
            self.file.write(item['steam_price'][i].decode("utf-8")  + ('\n').decode("utf-8"))
        return item
