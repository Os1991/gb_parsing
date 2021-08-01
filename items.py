import scrapy


class LeruaItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    images = scrapy.Field()
    params = scrapy.Field()
    pass
