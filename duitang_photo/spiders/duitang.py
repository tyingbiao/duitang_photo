# -*- coding: utf-8 -*-
import json

import os
from hashlib import md5

from scrapy import Spider, Request
from duitang_photo.items import PhotoItem

class DuitangSpider(Spider):
    name = 'duitang'
    allowed_domains = ['www.duitang.com']
    start_urls = ['http://www.duitang.com/']


    begin_url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={keyword}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum&_type=&start={start}'

    def start_requests(self):
        yield Request(self.begin_url.format(keyword='血界战线', start='0'), self.next_page)

    def next_page(self, response):
        result = json.loads(response.text)
        item = PhotoItem()
        path = []
        if 'data' in result.keys():
            if 'next_start' in result.get('data'):
                for srcs in result.get('data').get('object_list'):
                    path.append(srcs.get('photo').get('path'))
                item['path'] = path
                yield item
                if result.get('data').get('next_start') <= result.get('data').get('total'):
                    yield Request(self.begin_url.format(keyword='血界战线', start=result.get('data').get('next_start')), self.next_page)






