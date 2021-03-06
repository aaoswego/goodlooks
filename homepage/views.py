from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import News

def index(request):
    news = News.objects.all()
    template = loader.get_template('homepage/index.html')

    context = {

        'news':news,
    }
    
    return HttpResponse(template.render(context, request))
