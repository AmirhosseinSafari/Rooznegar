import json

#from django.shortcuts import render
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from datetime import datetime, timedelta
#from django.views.generic import TemplateView
#from django.views.decorators.cache import never_cache
from backend_news.models import News
from rest_framework import viewsets
from .serializers import NewsSersializer
from django.db.models import Q

from rest_framework.pagination import PageNumberPagination

import jdatetime
import convert_numbers
# Create your views here.

#index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class StandardResultsSetPagination(PageNumberPagination):
    page_size=30
    page_size_query_param = 'page_size'
    max_page_size = '100'

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSersializer
    pagination_class = StandardResultsSetPagination
    def list(self, request):
        now = datetime.now()
        two_hours_before = now - timedelta(hours=2)
        if News.objects.last():  #checking if db is empty; if not...                
            #lastObj_creation_time = News.objects.last().creation_time
            # old=>rand date; b=> the lastNewsUpdate date; a==b ? pass: read news file then set the new old and b
            if time_difference_in_hours(now, News.objects.last().creation_time) >= 2:
                print("start time " + str(datetime.now()))
                jsonDataHandler()
                print("end time " + str(datetime.now()))
        else:
            print("start time " + str(datetime.now()))
            jsonDataHandler()
            print("end time " + str(datetime.now()))
        self.queryset = News.objects.filter( Q(creation_time__gte = two_hours_before), Q(creation_time__lte =now) )
        page = self.paginate_queryset(self.queryset)
        
        # trasfering the hearder date into farsi (even numbers)
        jdatetime.set_locale('fa_IR')

        persion_date = jdatetime.datetime.now()
        
        persion_date_str = persion_date.strftime("%a") + " " + convert_numbers.english_to_persian(int(persion_date.strftime("%d"))) + " " + persion_date.strftime("%B،") + " " +  convert_numbers.english_to_persian(persion_date.strftime("%Y"))
        
        page_total_count = int(len(self.queryset)/30 + 1)
        #  print(page_total_count)

        content = {
            "news": self.serializer_class(page, many=True).data,
            "today_date": persion_date_str,
            "page_total_count": page_total_count
        }

        return Response(
            content, 200
        )


def time_difference_in_hours(time1, time2):
    if type(time1) == str:
        time1 = datetime.strptime(time1,"%Y %m %d %X")
    if type(time2) == str:
        time2 = datetime.strptime(time2,"%Y %m %d %X")

    defference_of_time = time1 - time2
    return int(divmod(defference_of_time.total_seconds(), 60*60)[0])
    
def jsonDataHandler():
    #/final project/survey_news/backend_news/newsman/news.json
    with open("backend_news/newsman/100_news.json", "r") as news_file:
        data = json.load(news_file)

    failure = False

    # adding news object to database
    for news in data:      
        
        title = news["title"]
        url = news["url"]
        image = news["image"]
        short_description = news["short_description"]
        body = news["body"]
        news_time = news["news_time"]
        source = news["source"]
        #creation_time = datetime.now().strftime("%Y %m %d %X")
        predicted_category  = news["predicted_category"]
        
        try:
            new = News(title=title, url=url, image=image, short_description=short_description, body=body, news_time=news_time, predicted_category=predicted_category, source=source)
            new.save()
            print(new)
            print(predicted_category)
        except Exception as e:
            print(e)
            print(title)
            failure = True
            #raise HTTPError("couldn't add the news to database")
            
    return failure