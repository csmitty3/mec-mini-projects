import scrapy

class QuotesSpider(scrapy.Spider):
    name = "cssscraper"

    start_urls = ['https://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14.htm?context=Jobs&clickSource=searchBox']

    def parse(self, response):
        postings = response.css('#MainCol').css('div ul li')
        for posting in postings:
            yield {
                'company': posting.css('div')[1].css('span::text')[0].get(),
                'position': posting.css('div')[1].css('span::text')[1].get(),
                'location': posting.css('div')[1].css('span::text')[2].get(),
                }
