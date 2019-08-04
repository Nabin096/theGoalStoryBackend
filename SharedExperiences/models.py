from django.db import models
import datetime

# Create your models here.
"""UI usable"""
class Elements(models.Model):
    blogId=models.IntegerField(default=0)
    sequenceNo=models.IntegerField()
    tag=models.CharField(max_length=15)
    innerHTML=models.CharField(max_length=5000)
    img=models.ImageField(null=True,blank=True)

    def ___str__(self):
        self.img.get_directory_name()
        return self.blogId+" " + self.tag+" "+ self.sequenceNo




"""System usable"""
class BlogsMetaData(models.Model):
    blogId=models.IntegerField(primary_key=True)
    genre=models.CharField(max_length=50,null=True,blank=True)
    rating=models.FloatField(default=0)
    previewText=models.CharField(max_length=100,default="N/A")
    previewImage=models.URLField(null=True,blank=True)
    date=models.DateTimeField(default=datetime.datetime.now())
    author=models.CharField(max_length=50,default="Team TGS")
    title=models.CharField(max_length=100,default="Lorem ipsum set amore")


    def __str__(self):
        return self.previewText

