from __future__ import unicode_literals
from django.db import models
from django.db import models
# Create your models here.
class blog_posts(models.Model):
    title = models.CharField(max_length=400)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title
    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})



class Topic(models.Model):

    top_name=models.CharField(max_length=100,unique=True)

    def __str__(self):

        return self.top_name

class Webpage(models.Model):

    topic=models.ForeignKey(Topic)

    name=models.CharField(max_length=100,unique=True)

    url=models.URLField(unique=True)

    def __str__(self):

        return self.name

class AccessRecord(models.Model):

    name=models.ForeignKey(Webpage)

    date=models.DateField()

    def __str__(self):

        return str(self.date)