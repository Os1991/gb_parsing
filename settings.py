BOT_NAME = 'lerua'

SPIDER_MODULES = ['lerua.spiders']
NEWSPIDER_MODULE = 'lerua.spiders'

USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94')

ROBOTSTXT_OBEY = False
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

IMAGES_STORE = 'images'

ITEM_PIPELINES = {
   'lerua.pipelines.DataBasePipeline': 300,
   'lerua.pipelines.LeruaPipeline': 200,
}
