import scrapy
from scrapy.spiders import CSVFeedSpider

# Spider
# CrawlSpider
# CSVFeedSpider

class VinosArania(CSVFeedSpider):
    name = 'vinos'

    start_urls = [
        'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
    ]
    
    delimiter = ';'

    quotechar = '"'

    headers = [
        'fixed density',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol',
        'quality'
    ]

    def parse_row(self, response, row):
        print('ph = ',row['pH'])
