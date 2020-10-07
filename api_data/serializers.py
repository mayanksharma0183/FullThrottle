from rest_framework import serializers

from .models import activity_periods,User

    
        
class activityserializer(serializers.ModelSerializer):
    class Meta:
        model = activity_periods
        fields = ['start_time','end_time']
 
 
         
class userserializer(serializers.ModelSerializer):
    activity_period = activityserializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','real_name','tz','activity_period']       
        
