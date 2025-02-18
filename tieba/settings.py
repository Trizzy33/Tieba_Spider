# -*- coding: utf-8 -*-


BOT_NAME = 'tieba'

SPIDER_MODULES = ['tieba.spiders']
NEWSPIDER_MODULE = 'tieba.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 360
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'tieba.pipelines.TiebaPipeline': 300,
}
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 1,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 1,
}

LOG_LEVEL = 'WARNING'
#LOG_LEVEL = 'INFO'

COMMANDS_MODULE = 'tieba.commands'

COOKIES_ENABLED = False
