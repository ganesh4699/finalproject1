import os
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudapp.settings')

import django
django.setup()

#populate my script

import random
from blog_posts.models import Topic, Webpage, AccessRecord

from faker import Faker
fakegen = Faker()

topics=['News','Social','marketplace','games','search']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpage=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        accessrecord=AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

if __name__ == '__main__':
    print("populating my script using faker library")
    populate(20)
    print("Populating of the script is done")
