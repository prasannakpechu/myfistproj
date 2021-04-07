from django.shortcuts import render

# Create your views here.

from .models import detemployee
import pandas as pd

filename = r'C:\Users\PC\Downloads\adult_dataset.csv'

try:
    if not detemployee.objects.exists():
        df = pd.read_csv(filename)
        for index, row in df.iterrows():
            detemployee.objects.create(age = row[0], work = row[1] , fwt = row[2] , education = row[3] ,
            edu_no = row[4] , marital_status = row[5] ,  occupation = row[6] ,relationship = row[7],
            race = row[8] , sex = row[9] , cap_gain = row[10] , cap_loss = row[11] , hours_pw = row[12] ,
            native_country = row[13] ,salary = row[14])
            print("Data successfully imported to data base !")


except Exception as e:
    print("Data already exists in Database !",e)


import glob,os,io,csv,time,datetime,json,re    
from rest_framework.views import APIView  
from django.conf import settings
import shutil,ast
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings as djangoSettings
from .models import detemployee
from .serializers import adultSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404



class genderdata(APIView):
    @csrf_exempt
    def get(self,request):
        try:
            maledata = detemployee.objects.filter(sex__contains='Male').count()
            femaledata = detemployee.objects.filter(sex__contains='Female').count()
            total = maledata + femaledata
            serializer = adultSerializer(maledata,femaledata,many=True)
            return Response({"StatusMessage":"Successfully listed count",
            "StatusCode":200,"data":{"male":maledata,"female":femaledata},"total_population":total},status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception at displaying gender numbers :::::",e)
            return Response({"StatusMessage":"Something went wrong !","StatusCode":404},status=status.HTTP_400_BAD_REQUEST)


class relationdata(APIView):
    @csrf_exempt
    def get(self,request):
        try:
            notinfamily = detemployee.objects.filter(relationship__contains='Not-in-family').count()
            husband = detemployee.objects.filter(relationship__contains='Husband').count()
            wife = detemployee.objects.filter(relationship__contains='Wife').count()
            ownchild = detemployee.objects.filter(relationship__contains='Own-child').count()
            unmarried = detemployee.objects.filter(relationship__contains='Unmarried').count()
            otherrelative = detemployee.objects.filter(relationship__contains='Other-relative').count()

            total = notinfamily + husband + wife + ownchild + unmarried + otherrelative

            return Response({"StatusMessage":"Successfully listed relationship count",
            "StatusCode":200,"data":{"Notinfamily":notinfamily,"Husband":husband,"Wife":wife,"Ownchild":ownchild,
            "Unmarried":unmarried,"Otherrelative":otherrelative},"total_population":total},status=status.HTTP_200_OK)

        except Exception as e:
            print("Exception at displaying relationship numbers :::::",e)
            return Response({"StatusMessage":"Something went wrong !","StatusCode":404},status=status.HTTP_400_BAD_REQUEST)


class alldata(APIView):
    @csrf_exempt
    def get(self,request):
        try:
            alldata = detemployee.objects.all()

            mylis = []

            for myd in alldata:
                mydict = {}
                mydict['age']=myd.age
                mydict['work']=myd.work
                mydict['fwt']=myd.fwt
                mydict['education']=myd.education
                mydict['edu_no']=myd.edu_no
                mydict['marital_status']=myd.marital_status
                mydict['occupation']=myd.occupation
                mydict['relationship']=myd.relationship
                mydict['race']=myd.race
                mydict['sex']=myd.sex
                mydict['cap_gain']=myd.cap_gain
                mydict['cap_loss']=myd.cap_loss
                mydict['hours_pw']=myd.hours_pw
                mydict['native_country']=myd.native_country
                mydict['salary']=myd.salary

                mylis.append(mydict)

            return Response({"StatusMessage":"Successfully listed all datas",
            "StatusCode":200,"data":mylis},status=status.HTTP_200_OK)

        except Exception as e:
            print("Exception at displaying all datas :::::",e)
            return Response({"StatusMessage":"Something went wrong !","StatusCode":404},status=status.HTTP_400_BAD_REQUEST)




class filterdata(APIView):
    @csrf_exempt
    def post(self,request):
        try:
            sex = request.data['sex']
            race = request.data['race']
            relationship = request.data['relationship']

            getval = detemployee.objects.filter(sex="sex")
            if getval.values == " Male" or " Female":
                print(getval)

            getval1 = detemployee.objects.filter(race="race")
            if getval1.values == "White" or "Black" or " Asian-Pac-Islander" or " Amer-Indian-Eskimo":
                print(getval1)


            getval2 = detemployee.objects.filter(relationship="relationship")
            if getval2.values == "Not-in-family" or "Husband" or "Wife" or "Own-child" or "Unmarried" or "Other-relative":
                print(getval2)

            return Response({"StatusMessage":"Successfully listed filter values",
            "StatusCode":200,"data":{"sex":getval,"race":getval,"relationship":getval2}},status=status.HTTP_200_OK)

        except Exception as e:
            print(e)




