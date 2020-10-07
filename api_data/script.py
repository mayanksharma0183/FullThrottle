import django
django.setup()
from faker import Faker
from api_data.models import activity_periods,User
import random
import string
from datetime import datetime

def custome_script():
 
 for i in range(0,10):
    fake = Faker()
    random_name = fake.name()
    random_address = fake.address()
    random_id = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(7))
    date1 = datetime.now() 
    activity_periods.objects.create(activity_id=random_id,start_time=date1,end_time=date1)
    User.objects.create(id=random_id,real_name=random_name,tz=random_address,activity_period=activity_periods.objects.get(activity_id=random_id))
    
   


if __name__== '__main__':
    custome_script()
    print('script run successfully')
    