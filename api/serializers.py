from rest_framework import serializers
from backend_news.models import News

class NewsSersializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'