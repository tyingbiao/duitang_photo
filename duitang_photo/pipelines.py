# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class DuitangPhotoPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['path']:
            yield scrapy.Request(image_url)

