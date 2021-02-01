from django.db import models
# from django.contrib.auth.models import User
from account.models import Account
from cloudinary.models import CloudinaryField
import cloudinary

import uuid

# Create your models here.
class CustomizeQuiz(models.Model):
    title = models.CharField(max_length=200, default="Empty")
    description = models.TextField(max_length=2000, default=" ")

    def __str__(self):
        return (self.title)

    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'CustomizeQuiz'

class Tquestion(models.Model):
    that_Quiz = models.ForeignKey(CustomizeQuiz, on_delete=models.CASCADE,default="")
    no = models.PositiveIntegerField(primary_key=True)
    question = models.CharField(max_length=1000, default=" ")
    A = models.CharField(max_length=500, default=" ")
    B = models.CharField(max_length=500, default=" ")
    C = models.CharField(max_length=500,default=" ")
    D = models.CharField(max_length=500, default=" ")
    answer = models.CharField(max_length=500, default=" ")
    def __str__(self):
        return str("("+str(self.no)+")"+self.question)

    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'Tquestion'

class Myself(models.Model):
    # id = models.AutoField(primary_key=True,default=None)
    me = models.ForeignKey(Account, on_delete=models.CASCADE, default="")
    answer = models.CharField(max_length=100, default="")
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    urlhash = models.UUIDField(default=uuid.uuid4, editable=False)
    timeStamp = models.DateTimeField(auto_now_add=True)
    
    def urlH(self):
        urlH = int(self.urlhash)
        return urlH

    def __str__(self):
        return str(str(self.me)+"("+self.answer+")")

    def total(self):
        total = self.correct + self.wrong
        return total

    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'Myself'

class Slide(models.Model):
    no = models.PositiveIntegerField(default=None)
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(max_length=4000,blank=True)
    # image = models.ImageField(blank=True)
    image = cloudinary.models.CloudinaryField('image',blank=True)

    def __str__(self):
        return ("("+ str(self.no) +")"+ self.title)
    
    objects = models.Manager()

class Department_or_branch(models.Model):
    Department_or_branch_name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.Department_or_branch_name
    
    objects = models.Manager()