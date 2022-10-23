from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.TextField(max_length=30,null=True,blank=True)
    lname = models.TextField(max_length=30,null=True,blank=True)
    email_id = models.TextField(max_length=50,null=True,blank=True)
    bio = models.TextField(max_length=400,null=True,blank=True)
    profileimg = models.ImageField(upload_to="profile_images/",default="default-profile-img.jpg")
    location = models.CharField(max_length=400,null=True,blank=True)

    def __str__(self):
        return self.user.username

class QuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    desc = models.ImageField(null=True,blank=True,upload_to="images/")
    category = models.CharField(max_length=200,null=True)
    marks = models.IntegerField(default=0)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    explaination = models.CharField(max_length=400,null=True,default="")
    subject = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.question

    