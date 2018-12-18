# -*- coding: utf-8 -*-
import time
import codecs
import os
class BuffPipeline(object):
    
    def __init__(self):
        _time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        try:
            os.makedirs(os.path.expanduser('~/SteamData/'))
        except:
            pass
        file_path = os.path.expanduser(('~/SteamData/{_time}.csv'.format(_time=_time)))
        self.file = codecs.open(file_path, 'wb', encoding='utf-8')


    def process_item(self, item, spider):   
        print item
        n = len(item['name'])
        #n = len(item['url'])
        for i in range(n):
            print i
            self.file.write(item['game'][i].decode("utf-8") + '||')
            self.file.write(item['id'][i].decode("utf-8")  + '||')
            self.file.write(item['name'][i].decode("utf-8") + '||')
            self.file.write(item['market_hash_name'][i].decode("utf-8")  + '||')
            self.file.write(item['sell_min_price'][i].decode("utf-8")  + '||')
            self.file.write(item['sell_num'][i].decode("utf-8")  + '||')
            self.file.write(item['steam_price'][i].decode("utf-8")  + ('\n').decode("utf-8"))
        return item
