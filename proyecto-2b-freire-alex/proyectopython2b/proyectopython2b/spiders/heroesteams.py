import scrapy
import urllib

def xPathFor(title):
    return "//table[@class='table profile-table']//td[text()='%s']/following-sibling::td/text()" % title


class QuotesSpider(scrapy.Spider):
    name = "superheroesteams"

    start_urls = ["https://www.superherodb.com/characters/?page_nr=%d" % x for x in range(1,26)]


    def parse(self, response):
        for region in response.xpath("//ul[@class='list']//li//a"):
            charPage = region.xpath("@href").extract_first()
            charName = region.xpath("text()").extract_first()
            yield scrapy.Request(
                urllib.parse.urljoin(response.url, charPage),
                callback = self.parseHero,
                meta = {'charName': charName}
            )

    def parseHero(self, response):
        name = response.meta['charName']
        teams = response.xpath("//div[@class='cblock back_blue'][3]/ul/li/a/@href").extract()
        gender = response.xpath(xPathFor("Gender")).extract_first()
        race = response.xpath("/html/body/main/div/div[6]/div[2]/table/tbody/tr[2]/td[2]/a/text()").extract_first()
        heights = response.xpath(xPathFor("Height")).re(".* (\d+) cm")

        
        
        
        
        
        if len(heights) > 0:
        	height = int(heights[0])
        else:
    	    height = 0
        superPowers = response.xpath("//div[@class='column col-12']//a[@class='chip']/text()").getall()
        yield {
                'name': name,
                'teams': teams,
                'gender': gender,
                'height': height,
                'race' : race,
                'superPowers': superPowers,
                
            }