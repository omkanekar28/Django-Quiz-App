from django.db import models

# Create your models here.


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

    