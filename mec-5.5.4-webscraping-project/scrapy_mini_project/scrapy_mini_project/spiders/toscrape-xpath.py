import scrapy

class QuotesSpider(scrapy.Spider):
    name = "xpathscraper"

    start_urls = ['https://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14.htm?context=Jobs&clickSource=searchBox']

    def parse(self, response):
        postings = response.xpath('//*[@id="MainCol"]/div[1]/ul')
        i = 1
        while postings.xpath(f'//li[{i}]/div[2]/div[1]/a/span/text()').get() is not None:
            yield {
                'company': postings.xpath(f'//li[{i}]/div[2]/div[1]/a/span/text()').get(),
                'position': postings.xpath(f'//li[{i}]/div[2]/a/span/text()').get(),
                'location': postings.xpath(f'//li[{i}]/div[2]/div[2]/span/text()').get()
                }
            i+= 1