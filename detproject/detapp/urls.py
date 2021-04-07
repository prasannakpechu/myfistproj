from django.contrib import admin  
from django.urls import path  
from detapp import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [  
    path('mflist/',views.genderdata.as_view()),
    path('relationlist/',views.relationdata.as_view()),
    path('fulllist/',views.alldata.as_view()),
    path('filterlist/',views.filterdata.as_view()),
]  