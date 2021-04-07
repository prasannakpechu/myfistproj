import glob,os,io,csv,time,datetime,json,re    
from rest_framework.views import APIView  
from django.conf import settings
import shutil,ast
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings as djangoSettings
from .models import detemployee


# class genderdata(APIView):
#     @csrf_exempt

def mflist(request):
    if request.method == 'GET':
        finaldata = detemployee.objects.filter(sex)