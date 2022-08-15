import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from backend_news.models import News
from rest_framework import viewsets
from .serializers import NewsSersializer
# Create your views here.

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class NewsViewSet(viewsets.ViewSet):
    one_time_db_insert_counter = 0
    def list(self, request):
        if self.one_time_db_insert_counter == 0:
            jsonDataHandler()
        queryset = News.objects.all()
        serializer = NewsSersializer(queryset, many=True)
        return Response(serializer.data)

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

        if "a_title" in news:
            title = news["a_title"]
        else:
            title = None
        
        if "b_url" in news:
            url = news["b_url"]
        else:
            url = None
        
        if "c_image" in news:
            image = news["c_image"]
        else:
            image = None
        
        if "d_short_description" in news:
            short_description = news["d_short_description"]
        else:
            short_description = None

        if "e_time" in news:
            news_time = news["e_time"]
        else:
            news_time = datetime.now().strftime("%Y %m %d %X")

        try:
            new = News(title=title, url=url, image=image, short_description=short_description, news_time=news_time)
            new.save()
            #print(new)
        except Exception as e:
            print(e)
            print(title)
            failure = True
            #raise HTTPError("couldn't add the news to database")
            
    return failure