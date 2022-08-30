from bs4 import BeautifulSoup
import requests
import json

from datetime import datetime

import pickle
import pandas as pd
import numpy as np
from sklearn.svm import SVC

# print(body)
def news_dataCompeleter(url ,soup):
    links = ['https://www.isna.ir/',
            'https://www.iribnews.ir',
            'https://rasanews.ir/',
            'https://roozno.com/',
            'https://www.tasnimnews.com/']
    
    if links[0] in url:
        #'https://www.isna.ir/'
        try:
            title = soup.find("h1", class_="first-title").text
            try:
                photo = soup.find("figure", class_="item-img").img['src']
            except:
                photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/ISNA_logo.jpg/250px-ISNA_logo.jpg"
            short_description = soup.find("p", class_="summary").text
            body = soup.find("div", class_="item-text").text
            time_news_wrote = "تاریخ انتشار:" + soup.find("span", class_="text-meta").text
            source = "خبرگذاری دانشجویان ایران (ایسنا)"
            
            return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}
        except:
            return None

    if links[1] in url:
        #'https://www.iribnews.ir' 
        try: 
            try:
                title = soup.find("h1", class_="title_news").span.text
                try:
                    photo = links[1] + soup.find("img", class_="image_btn")['src']
                except:
                    photo = "https://www.iribnews.ir/client/themes/fa/main/img/logo.png"

                body = soup.find("div", class_="body_media_content_show").text
                short_description = soup.find("p", class_="subtitle").text
                time_news_wrote = soup.find("div", class_="news_pdate_c").text
                source = "خبرگذاری صدا و سیما"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}

            except:
                title = soup.find("div", class_="video_title").h1.a.text 
                photo = "https://www.iribnews.ir/client/themes/fa/main/img/logo.png"
                
                short_description = "" 
                for i in soup.find_all("a", class_="tags_item_photo"): 
                    short_description = short_description + i.text + " "

                temp = soup.find_all("p") 
                body = "" 

                for i in temp:
                    if "body_media_content_show" in i.parent["class"]:
                        body = body + i.text + " "

                time_news_wrote = soup.find("div", class_="photo_pub_date").text
                source = "خبرگذاری صدا و سیما"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}

        except:
            return None

    if links[2] in url:
        #'https://rasanews.ir/', 
        try:
            try:
                title = soup.find("h1", class_="title").text 
                photo = links[2] + soup.find("img", class_="lead_image")["src"]
                short_description = soup.find("div", class_="subtitle").text
                body = soup.find("section", class_="body").text
                time_news_wrote = "تاریخ انتشار:" + soup.find("article", class_="n-data").text
                source = "خبرگذاری رسا"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}

            except:
                pass
            
            try:
                title = soup.find("h1", class_="title").a.text 
                photo = "https://static.cdn.asset.aparat.com/avt/30784580-5297-b__4105.jpg"
                short_description = soup.find("div", class_="video-news-subtitle").text
                body = soup.find("div", class_="tags_title").text
                time_news_wrote = soup.find("section", class_="video-date").text
                source = "خبرگذاری رسا"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}
            except:
                pass

            try:
                title = soup.find("h1", class_="title").a.text
                photo = links[2] + soup.find("div", class_="album_list_content").a.img["src"]
                short_description = soup.find("div", class_="subtitle").text
                body = soup.find("div", class_="tags_title").text
                time_news_wrote = "تاریخ انتشار:" + soup.find("article", class_="photo-n-data").text
                source = "خبرگذاری رسا"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}
            except:
                pass

            try:
                title = soup.find("h1", class_="title").a.text
                photo = links[2] + soup.find("div", class_="image_set").div.a.img["src"]
                short_description = soup.find("section", class_="photo-news-items").div.a.text
                body = soup.find("div", class_="tags_title").text
                temp = soup.find("section", class_="photo-news-items")
                time_news_wrote = "تاریخ انتشار:" + temp.select("div:nth-of-type(3)")[0].text
                source = "خبرگذاری رسا"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}
            except:
                pass
        
        except:
            return None

    if links[3] in url: 
        #'https://roozno.com/',
        try:
            title = soup.find("h1", class_="title").text
            try:
                photo = links[3] + soup.find("img", class_="image_btn")["src"]
            except:
                photo = "https://media-exp1.licdn.com/dms/image/C4E03AQHr_8SeDcFzMg/profile-displayphoto-shrink_200_200/0/1612090176297?e=2147483647&v=beta&t=mdUClajH5_aitPtBZkV8qaHKr_QgpXV0TDyY8akL_f8"
            
            short_description = soup.find("div", class_="subtitle").text
            temp = soup.find_all("p")  
            body = ""  
            for i in temp: 
                body = body + i.text + " "
            
            time_news_wrote = soup.find("div", class_="news_pdate_c").text
            source = "پایگاه خبری تحلیلی روزنو"
            return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}
        
        except:
            return None


    if links[4] in url:
        #'https://www.tasnimnews.com/'
        try:
            try:
                title = soup.find("article", class_ = "single-news").h1.text
                photo = soup.find("img", class_="center_position")["src"]
                short_description = soup.find("h3", class_="lead").text
                
                temp = soup.find_all("p")  
                body = ""  
                for i in temp: 
                    if "story" in i.parent["class"]: 
                        body = body + i.text + " " 

                time_news_wrote = "تاریخ انتشار:" + soup.find("li", class_="time").text
                source = "خبرگذاری تسنیم"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}

            except:
                title = soup.find("h1", class_ = "title").text 
                photo = "https://newsmedia.tasnimnews.com/Tasnim/Uploaded/Image/1394/10/01/139410011036272706762304.jpg"
                short_description = soup.find("h3", class_= "lead").text

                body = short_description
                time_news_wrote = "تاریخ انتشار:" + soup.find("time").text 
                source = "خبرگذاری تسنیم"
                return {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}

        except:
            return None


with open("./news.json", "r") as news_file:
    data = json.load(news_file)

# removing the duplicated news and empty news
temp = [] 
no_rep_data = [] 
for news in data: 
    if len(news)==0 or news["b_url"] in temp: 
        continue 
    temp.append(news["b_url"]) 
    no_rep_data.append(news)

json_object = []

for news in no_rep_data:
    if len(news) == 0:
        continue
    
    try:
        source = requests.get(news["b_url"][0]).text
    except:
        continue
    soup = BeautifulSoup(source, 'lxml')
    complete_news_data = news_dataCompeleter(news["b_url"][0], soup)


# {"title":title, "photo": photo, "body": body, "short_description": short_description, "time_news_wrote": time_news_wrote, "source": source}
    if complete_news_data == None:
        continue

    if "a_title" in news:
        title = news["a_title"][0]
    else:
        title = complete_news_data["title"]
    
    if "b_url" in news:
        url = news["b_url"][0]
    else:
        url = None
    
    if "c_image" in news:
        image = news["c_image"][0]
    else:
        image = complete_news_data["photo"]
    
    if "d_short_description" in news:
        short_description = news["d_short_description"][0]
    else:
        short_description = complete_news_data["short_description"]

    body = complete_news_data["body"]

    if "e_time" in news:
        news_time = news["e_time"][0]
    else:
        news_time = complete_news_data["time_news_wrote"]

    source = complete_news_data["source"]
    category_dic = {
        0: 'اقتصادی',
        1: 'ادبی/اجتماعی',
        2: 'سیاسی',
        3: 'علم و فرهنگ',
        4: 'اجتماعی'}

    #load the predition model
    with open('../my_dumped_classifier.pkl', 'rb') as fid:
        model = pickle.load(fid)

    model_input = [short_description]
    predicted_category = category_dic[int(model.predict(model_input)[0])]

    print(title)
    print()
    print()

    #title=title, url=url, image=image, short_description=short_description, body=body, news_time=news_time, predicted_category=predicted_category, source=source
    json_object.append({"title":title, "url":url, "image":image, "short_description": short_description, "body": body, "news_time": news_time, "predicted_category": predicted_category, "source": source})


print(len(json_object))
jsonString = json.dumps(json_object)
with open("./100_news.json", "w") as f:  
    f.write( jsonString )

with open("./lastNewsUpdate.txt", "w") as f:
    f.write(datetime.now().strftime("%Y %m %d %X"))