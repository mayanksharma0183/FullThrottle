from django.db import models




class activity_periods(models.Model):
   
    activity_id = models.CharField(max_length=20) 
    start_time = models.DateTimeField(auto_now_add=True,null=True)
    end_time = models.DateTimeField(auto_now_add=True,null=True)


class User(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=200)
    activity_period=models.ForeignKey(activity_periods,related_name='activity_period',on_delete=models.CASCADE)
    
    

    
    

    

