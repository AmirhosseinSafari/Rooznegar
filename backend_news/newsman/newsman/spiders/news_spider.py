import scrapy
from newsman.items import IsnaNewsItem, IribnewsItem, RasanewsItem, RooznonewsItem, TasnimnewsItem
from scrapy.loader import ItemLoader

class news_spider(scrapy.Spider):
    name = 'newsman'
    start_urls = ['https://www.isna.ir/',
                'https://www.iribnews.ir',
                'https://rasanews.ir/',
                'https://roozno.com',
                'https://www.tasnimnews.com/']

                #'https://www.hamshahrionline.ir'
                #'https://www.mehrnews.com/',
                #'https://www.khabaronline.ir'
    
    def parse(self, response):
        if response.url == 'https://www.isna.ir/': 
            yield scrapy.Request(response.url, callback=self.parse_isna)
        
        if response.url == 'https://www.iribnews.ir':
            yield scrapy.Request(response.url, callback=self.parse_iribnews)

        if response.url == 'https://rasanews.ir/':
            yield scrapy.Request(response.url, callback=self.parse_rasanews)

        if response.url == 'https://roozno.com':
            yield scrapy.Request(response.url, callback=self.parse_roozno)

        if response.url == 'https://www.tasnimnews.com/':
            yield scrapy.Request(response.url, callback=self.parse_tasnimnews)


#================================
#   https://www.isna.ir/
#================================
    def parse_isna(self, response):
        list_of_classes = ['trans', 'talk', 'report', 'coverage', 'received',  'text']
        for className in list_of_classes:        
            for news in response.css(f"li.{className}"):
                l = ItemLoader(item = IsnaNewsItem(), selector = news)

                l.add_css('a_title', 'div.desc>h3>a::text')
                l.add_css('b_url', 'div.desc>h3>a::attr(href)')
                l.add_css('c_image', 'figure>a>img::attr(src)')
                l.add_css('d_short_description', 'div.desc>p')
                l.add_css('e_time', 'div.desc>h3>a::attr(title)')

                yield l.load_item()


#================================
#   https://www.iribnews.ir
#================================
    def parse_iribnews(self, response):
                
        for news in response.css('div.h_news_item'):
            l = ItemLoader(item = IribnewsItem(), selector = news)

            l.add_css('a_title', 'div>div.khv_right_text>h2>a::text')
            l.add_css('b_url', 'div>div.khv_right_text>h2>a::attr(href)')
            l.add_css('c_image', 'div>a.picLink>img::attr(src)')
            l.add_css('d_short_description', 'div>div.khv_right_text>div.subtitle_khv')
            #l.add_css('e_time', 'div.desc>h3>a::attr(title)')
            
            yield l.load_item()

        list_of_classes = ['leftnews', 'rightnews']
        for className in list_of_classes:
            for news in response.css(f'div.{className}'):
                l = ItemLoader(item = IribnewsItem(), selector = news)

                l.add_css('a_title', 'div.row>div>h3.Htags>a::text')
                l.add_css('b_url', 'div.row>div>a.picLink::attr(href)')
                l.add_css('c_image', 'div.row>div>a.picLink>img::attr(src)')
                l.add_css('d_short_description', 'div.row>div>div.lead1')
                #l.add_css('time', 'div.desc>h3>a::attr(title)')
                
                yield l.load_item()

        for news in response.css('div.sp_linear_news'):
            l = ItemLoader(item = IribnewsItem(), selector = news)

            l.add_css('a_title', 'div.h_sp_linear_news_bg>h3>a::text')
            l.add_css('b_url', 'div.h_sp_linear_news_bg>h3.Htags>a::attr(href)')
            #l.add_css('image', '')
            #l.add_css('short_description', '')
            #l.add_css('time', 'div.desc>h3>a::attr(title)')
            
            yield l.load_item()

        for news in response.css('div.fav_sections_cont'):
            l = ItemLoader(item = IribnewsItem(), selector = news)

            l.add_css('a_title', 'div.txt_fav>a::text')
            l.add_css('b_url', 'div.txt_fav>a::attr(href)')
            l.add_css('c_image', 'a.picLink>img::attr(src)')
            #l.add_css('short_description', '')
            #l.add_css('time', 'div.desc>h3>a::attr(title)')
            
            yield l.load_item()

#================================
#   'https://rasanews.ir'
#================================
    def parse_rasanews(self, response):
        for news in response.css('div.kh_vije_oth'):
            l = ItemLoader(item = RasanewsItem(), selector = news)
    
            l.add_css('a_title', 'h2>a::text')
            l.add_css('b_url', 'h2>a::attr(href)')
            l.add_css('d_short_description', 'div.kh_vije_sub')
            #l.add_css('c_image', '')
            #l.add_css('e_time', 'div.desc>h3>a::attr(title)')
        
            yield l.load_item()

        for news in response.css('article.im-news-content'):
            l = ItemLoader(item = RasanewsItem(), selector = news)
    
            l.add_css('a_title', 'article>h3>a::text')
            l.add_css('b_url', 'article>h3>a::attr(href)')
            l.add_css('c_image', 'article>a.picLink>img::attr(src)')
            l.add_css('d_short_description', 'article>div.im-news-sub')
            #l.add_css('e_time', 'div.desc>h3>a::attr(title)')
        
            yield l.load_item()

        for news in response.css('article.sec-news1-content'):
            l = ItemLoader(item = RasanewsItem(), selector = news)
    
            l.add_css('a_title', 'h3>a::text')
            l.add_css('b_url', 'h3>a::attr(href)')
            #l.add_css('c_image', '')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', 'div.desc>h3>a::attr(title)')
        
            yield l.load_item()

        for news in response.css('article.sec-new2-content'):
            l = ItemLoader(item = RasanewsItem(), selector = news)
    
            l.add_css('a_title', 'h3>a::text')
            l.add_css('b_url', 'h3>a::attr(href)')
            #l.add_css('c_image', '')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', 'div.desc>h3>a::attr(title)')
        
            yield l.load_item()

        for news in response.css('div.multisec-content'):
            l = ItemLoader(item = RasanewsItem(), selector = news)
    
            l.add_css('a_title', 'h3>a::text')
            l.add_css('b_url', 'h3>a::attr(href)')
            l.add_css('c_image', 'a.picLink>img::src')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', 'div.desc>h3>a::attr(title)')
        
            yield l.load_item()

        for news in response.css('div.ax-r-item'):
            l = ItemLoader(item = RasanewsItem(), selector = news)
    
            l.add_css('a_title', 'h3>a::text')
            l.add_css('b_url', 'h3>a::attr(href)')
            l.add_css('c_image', 'a.picLink>img::attr(src)')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', 'div.desc>h3>a::attr(title)')
        
            yield l.load_item()


#================================
#   'https://roozno.com'
#================================
    def parse_roozno(self, response):
              
        for news in response.css("a.imgs"):
            l = ItemLoader(item = RooznonewsItem(), selector = news)
        
            l.add_css('a_title', '::attr(title)')
            l.add_css('b_url', '::attr(href)')
            l.add_css('c_image', 'img.imgs::attr(src)')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', '')
        
            yield l.load_item()
        
        for news in response.css("section.vijeh-rooz"):
            l = ItemLoader(item = RooznonewsItem(), selector = news)
        
            l.add_css('a_title', 'div>div.viewport>div.overview>div>article>h4>a::text')
            l.add_css('b_url', 'div>div.viewport>div.overview>div>article>h4>a::attr(href)')
            #l.add_css('c_image', '')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', '')
        
            yield l.load_item()
        
        for news in response.css("section.c-box-cover.box1-cover.c-box-cover2"):
            l = ItemLoader(item = RooznonewsItem(), selector = news)
        
            l.add_css('a_title', 'div>article.box1>h4>a::text')
            l.add_css('b_url', 'div>article.box1>h4>a::attr(href)')
            #l.add_css('c_image', '')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', '')
        
            yield l.load_item()

        for news in response.css("atricle.c-box.box2"):
            l = ItemLoader(item = RooznonewsItem(), selector = news)
        
            l.add_css('a_title', 'div.box2-in>a::attr(title)')
            l.add_css('b_url', 'div.box2-in>a::attr(href)')
            l.add_css('c_image', 'div.box2-in>a.img-pd-brdr>img.imgs::attr(src)')
            l.add_css('d_short_description', 'div.subtitle1')
            #l.add_css('e_time', '')
        
            yield l.load_item()

#================================
#   https://www.tasnimnews.com/
#================================
    def parse_tasnimnews(self, response):     
        for news in response.css("article.first"):
            l = ItemLoader(item = TasnimnewsItem(), selector = news)
        
            l.add_css('a_title', 'a>div.details>h1.title')
            l.add_css('b_url', 'a::attr(href)')
            l.add_css('c_image', 'a>figure>img::attr(src)')
            l.add_css('d_short_description', 'a>div.details>h3.lead')
            #l.add_css('e_time', '')
        
            yield l.load_item()
        
        for news in response.css("article.list-item"):
            l = ItemLoader(item = TasnimnewsItem(), selector = news)
        
            l.add_css('a_title', 'a>div>h2.title')
            l.add_css('b_url', 'a::attr(href)')
            l.add_css('c_image', 'a>div>figure>img::attr(src)')
            l.add_css('d_short_description', 'a>div>h4.lead')
            l.add_css('e_time', 'a>div>time>time.fa-clock-o')
        
            yield l.load_item()

        for news in response.css("section.news-box:nth-child(4)>section.content>article.box-item"):
            l = ItemLoader(item = TasnimnewsItem(), selector = news)
        
            l.add_css('a_title', 'a>div.numbered-item>div.row>h5.title')
            l.add_css('b_url', 'a::attr(href)')
            #l.add_css('c_image', '')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', '')
        
            yield l.load_item()
        
        for news in response.css("section.news-container:nth-child(5)>section.content>article.box-item"):
            l = ItemLoader(item = TasnimnewsItem(), selector = news)
        
            l.add_css('a_title', 'a>div.normal_weight>h5.title')
            l.add_css('b_url', 'a::attr(href)')
            l.add_css('c_image', 'a>div.image-container>figure>img::attr(src)')
            #l.add_css('d_short_description', '')
            #l.add_css('e_time', '')
        
            yield l.load_item()