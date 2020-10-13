from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import dataSerializer

from bs4 import BeautifulSoup
import requests



class datalist(generics.ListAPIView):
    serializer_class = dataSerializer
    queryset = data.objects.all()

def action(request):
    print(request.GET.__getitem__('query'))
    query = request.GET.__getitem__('query')
    url = "https://www.jumia.com.ng/catalog/?q="+query
    response = requests.get(url)
    dat = response.text
    soup = BeautifulSoup(dat,'html.parser')
    a = soup.find_all("a",{"class":"core"})
    i = 0
    while i < len(a): 
        title = str(a[i].get('data-name')) + str(i)
        img = str(a[i].find('img').get('data-src'))
        link ="https://jumia.com.ng" + str(a[i].get('href'))

        data.objects.get_or_create(title = title, url = link , img_link = img , description = title)
        
        i = i + 1
    context = {'message': 'Done'}
    return render(request,'index.html')

def index(request):

    context = {}
    return render(request,'index.html')
