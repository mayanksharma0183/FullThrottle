# FullThrottle
This is the Rest-Api Assignment for FullThrottle:

This project is developed using Django-framework, Django-Rest_Framework with Python 3.7 and MysqlDB.
The end-point is production ready and deployed on pythonanywhere free account.
you can check the end-point using Postman as well as get the data into your project by the api link.
The format of data is in a Json Format.
Eclipse IDLE used to build the whole project.

##########################################   PROJECT DESCRIPITION   #####################################################################

NOTE: Extra library used is Faker library in custom script to generate fake or random data.


There are one app which is api_data which contains models file, view file, script file, serializers file.

1. Models file,
   it contains two model class which is User and activity_periods.
   
2. View file,
   it contains two view fuction which contain one query set and on serializer class and provides a modelviewset
   
3. Script file,
   it contain custom script which fill database with some random data. For this i used Faker library which can generate some random or fake values.
   
4. serializers file,
   it contains two serializers one is userserializer and second is activity.
   In this i used Django-Rest_Framwork serilaizers to serialize the data.
   

