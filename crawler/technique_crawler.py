import scrapy
from bs4 import BeautifulSoup

class BlogSpider(scrapy.Spider):
    name = 'narutospider'
    start_urls = ['https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu?limit=250&offset=0&_cat=Jutsu']

    def parse(self, response):
        for href in response.css('.smw-columnlist-container')[0].css("a::attr(href)").extract(): # interation over part of the page we need to scar
            extracted_data = scrapy.Request("https://naruto.fandom.com/"+href,
                           callback=self.parse_technique)
            yield extracted_data

        for next_page in response.css('a.mw-nextlink'):
            yield response.follow(next_page, self.parse) # recursive
            
    def parse_technique(self, response):
        technique_name = response.css("span.mw-page-title-main::text").extract()[0]
        technique_name = technique_name.strip()
        
        div_selected = response.css("div.mw-parser-output")[0]
        div_html = div_selected.extract()
        soup = BeautifulSoup(div_html).find("div")
        
        technique_type = ""
        if soup.find("aside"):
            aside = soup.find("aside")
            
            for cell in aside.find_all("div", {"class": "pi-data"}):
                if cell.find('h3'):
                    cell_name = cell.find('h3').text.strip()
                    if cell_name == "Classification":
                        technique_type = cell.find('div').text.strip()
                
        soup.find("aside").decompose()
        
        technique_decription = soup.text.strip()
        technique_decription= technique_decription.split("Trivia").strip()
        
                    
        
        return dict(
            technique_name = technique_name,
            technique_type = technique_type,
            technique_decription = technique_decription
        )
            