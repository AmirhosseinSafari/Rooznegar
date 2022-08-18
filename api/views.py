import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from backend_news.models import News
from rest_framework import viewsets
from .serializers import NewsSersializer
from django.db.models import Q

from bs4 import BeautifulSoup
import requests

import pickle
import pandas as pd
import numpy as np
from sklearn.svm import SVC
# Create your views here.

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class NewsViewSet(viewsets.ViewSet):
    def list(self, request):
        now = datetime.now()
        three_hours_before = now - timedelta(hours=3)
        if News.objects.last():  #checking if db is empty; if not...                
            #lastObj_creation_time = News.objects.last().creation_time
            if time_difference_in_hours(now, News.objects.last().creation_time) >= 3:
                print("start time " + datetime.now())
                jsonDataHandler()
                print("end time " + datetime.now())
        else:
            print("start time " + str(datetime.now()))
            jsonDataHandler()
            print("end time " + str(datetime.now()))

        queryset = News.objects.filter( Q(creation_time__gte = three_hours_before), Q(creation_time__lte =now) )
        serializer = NewsSersializer(queryset, many=True)
        return Response(serializer.data)
        
def time_difference_in_hours(time1, time2):
    if type(time1) == str:
        time1 = datetime.strptime(time1,"%Y %m %d %X")
    if type(time2) == str:
        time2 = datetime.strptime(time2,"%Y %m %d %X")

    defference_of_time = time1 - time2
    return int(divmod(defference_of_time.total_seconds(), 60*60)[0])
    
def jsonDataHandler():
    #/final project/survey_news/backend_news/newsman/news.json
    with open("backend_news/newsman/news.json", "r") as news_file:
        data = json.load(news_file)

    failure = False

    # removing the duplicated news and empty news
    temp = [] 
    no_rep_data = [] 
    for news in data: 
        if len(news)==0 or news["b_url"] in temp: 
            continue 
        temp.append(news["b_url"]) 
        no_rep_data.append(news)

    # adding news object to database
    for news in no_rep_data:
        if len(news) == 0:
            continue
        
        try:
            source = requests.get(news["b_url"][0]).text
        except:
            continue
        soup = BeautifulSoup(source, 'lxml')
        complete_news_data = news_dataCompeleter(news["b_url"][0], soup)
        
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

        if "e_time" in news:
            news_time = news["e_time"][0]
        else:
            news_time = complete_news_data["time_news_wrote"]

        #creation_time = datetime.now().strftime("%Y %m %d %X")
        
        #predicting the category
        category_dic = {0: 'اقتصادی',
        1: 'ادبیات و هنر',
        2: 'سیاسی',
        3: 'علم و فرهنگ',
        4: 'اجتماعی'}

        #load the predition model
        with open('backend_news/my_dumped_classifier.pkl', 'rb') as fid:
            model = pickle.load(fid)

        model_input = [short_description]
        predicted_category = category_dic[int(model.predict(model_input)[0])]
        
        try:
            new = News(title=title, url=url, image=image, short_description=short_description, news_time=news_time, predicted_category=predicted_category)
            new.save()
            print(new)
            print(predicted_category)
        except Exception as e:
            print(e)
            print(title)
            failure = True
            #raise HTTPError("couldn't add the news to database")
            
    return failure

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
            time_news_wrote = soup.find("span", class_="text-meta").text

            return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
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

                short_description = soup.find("p", class_="subtitle").text
                time_news_wrote = soup.find("div", class_="news_pdate_c").text
                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}

            except:
                title = soup.find("div", class_="video_title").h1.a.text 
                photo = "https://www.iribnews.ir/client/themes/fa/main/img/logo.png"
                
                short_description = "" 
                for i in soup.find_all("a", class_="tags_item_photo"): 
                    short_description = short_description + i.text + " "

                time_news_wrote = soup.find("div", class_="photo_pub_date").text
                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
        except:
            return None

    if links[2] in url:
        #'https://rasanews.ir/',
        try:
            try:
                title = soup.find("h1", class_="title").text 
                photo = soup.find("img", class_="lead_image")["src"]
                short_description = soup.find("div", class_="subtitle").text
                time_news_wrote = soup.find("article", class_="n-data").text
                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
            except:
                pass
            
            try:
                title = soup.find("h1", class_="title").a.text 
                photo = "https://static.cdn.asset.aparat.com/avt/30784580-5297-b__4105.jpg"
                short_description = soup.find("div", class_="video-news-subtitle").text
                time_news_wrote = soup.find("section", class_="video-date").text
                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
            except:
                pass

            try:
                title = soup.find("h1", class_="title").a.text
                photo = links[2] + soup.find("div", class_="album_list_content").a.img["src"]
                short_description = soup.find("div", class_="subtitle").text
                time_news_wrote = soup.find("article", class_="photo-n-data").text
                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
            except:
                pass

            try:
                title = soup.find("h1", class_="title").a.text
                photo = links[2] + soup.find("div", class_="image_set").div.a.img["src"]
                short_description = soup.find("section", class_="photo-news-items").div.a.text
                
                temp = soup.find("section", class_="photo-news-items")

                time_news_wrote = temp.select("div:nth-of-type(3)")[0].text
                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
            except:
                pass
        
        except:
            return None

    if links[3] in url: 
        #'https://roozno.com/',
        try:
            title = soup.find("h1", class_="title").text
            try:
                photo = link[3] + soup.find("img", class_="image_btn")["src"]
            except:
                photo = "https://media-exp1.licdn.com/dms/image/C4E03AQHr_8SeDcFzMg/profile-displayphoto-shrink_200_200/0/1612090176297?e=2147483647&v=beta&t=mdUClajH5_aitPtBZkV8qaHKr_QgpXV0TDyY8akL_f8"
            
            short_description = soup.find("div", class_="subtitle").text
            time_news_wrote = soup.find("div", class_="news_pdate_c").text

            return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
        
        except:
            return None


    if links[4] in url:
        #'https://www.tasnimnews.com/'
        try:
            try:
                title = soup.find("article", class_ = "single-news").h1.text
                photo = soup.find("img", class_="center_position")["src"]
                short_description = soup.find("h3", class_="lead").text
                time_news_wrote = soup.find("li", class_="time").text

                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}

            except:
                title = soup.find("h1", class_ = "title").text 
                photo = "https://newsmedia.tasnimnews.com/Tasnim/Uploaded/Image/1394/10/01/139410011036272706762304.jpg"
                short_description = soup.find("h3", class_= "lead").text
                time_news_wrote = soup.find("time").text 
            
                return {"title":title, "photo": photo, "short_description": short_description, "time_news_wrote": time_news_wrote,}
        
        except:
            return None