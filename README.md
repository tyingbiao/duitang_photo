# duitang_photo
 第一次使用Scrapy框架爬取动态加载网页的图片，接触到Scrapy内置的ImagePipeline用法，调试过程中遇到“ValueError: Missing scheme in request url: h”
 报错，了解到使用ImagesPipeline传入的url地址必须是一个list，需要修改一下传入的url格式
