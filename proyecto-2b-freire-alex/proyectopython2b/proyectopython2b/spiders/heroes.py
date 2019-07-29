import scrapy
import urllib

def xPathFor(title):
    return "//table[@class='table profile-table']//td[text()='%s']/following-sibling::td/text()" % title


class QuotesSpider(scrapy.Spider):
    name = "superheroes"

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
        weight = response.xpath(xPathFor("Weight")).re(".* (\d+) kg")
        eyecolor = response.xpath(xPathFor("Eye color")).extract_first()
        haircolor = response.xpath(xPathFor("Hair color")).extract_first()
        fullname = response.xpath(xPathFor("Full name")).extract_first()
        alteregos = response.xpath(xPathFor("Alter Egos")).extract_first()
        aliases = response.xpath(xPathFor("Aliases")).extract_first()
        placeofbirth = response.xpath(xPathFor("Place of birth")).extract_first()
        firstappearance = response.xpath(xPathFor("First appearance")).extract_first()
        creator = response.xpath(xPathFor("Creator")).extract_first()
        occupation = response.xpath(xPathFor("Occupation")).extract_first()
        base = response.xpath(xPathFor("Base")).extract_first()
        relatives = response.xpath(xPathFor("Relatives")).extract_first()
        intelligence = response.xpath("/html/body/main/div/div[4]/div[1]/div/div[1]/div[1]").extract_first()
        strength = response.xpath("/html/body/main/div/div[4]/div[1]/div/div[2]/div[1]").extract_first()
        speed = response.xpath("/html/body/main/div/div[4]/div[1]/div/div[3]/div[1]").extract_first()
        durability = response.xpath("/html/body/main/div/div[4]/div[1]/div/div[4]/div[1]").extract_first()
        power = response.xpath("/html/body/main/div/div[4]/div[1]/div/div[5]/div[1]").extract_first()
        combat = response.xpath("/html/body/main/div/div[4]/div[1]/div/div[6]/div[1]").extract_first()
        speed = response.xpath("/html/body/main/div/div[4]/div[1]/div/div[3]/div[1]").extract_first()
        
        
        
        
        
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
                'weight' : weight,
                'eyecolor' : eyecolor,
                'haircolor' : haircolor,
                'fullname' : fullname,
                'alteregos' : alteregos,
                'aliases' : aliases,
                'placeofbirth' : placeofbirth,
                'firstappearance' : firstappearance,
                'creator' : creator,
                'occupation' : occupation,
                'base' : base,
                'relatives' : relatives,
                'intelligence' : intelligence,
                'strength' : strength,
                'speed' : speed,
                'durability' : durability,
                'power' : power,
                'combat' : combat,
                'speed' : speed,
                'superPowers': superPowers,
                
            }