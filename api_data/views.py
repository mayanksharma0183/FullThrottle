from django.shortcuts import render
from .models import activity_periods,User
from .serializers import userserializer,activityserializer
from rest_framework import viewsets



class userviewset(viewsets.ModelViewSet):
   
   queryset = User.objects.all()
   serializer_class = userserializer
   
class activityviewset(viewsets.ModelViewSet):
   
   queryset = activity_periods.objects.all()
   serializer_class = activityserializer
     
    
 