from django.db import models

# Create your models here.
class adform(models.Model):
        firstname = models.CharField(max_length=10)
        lastname = models.CharField(max_length=10)
        fathername = models.CharField(max_length=50)
        mothername = models.CharField(max_length=50)
        mobile= models.IntegerField()
        types = models.CharField(max_length=10)

        def __str__(self): 
         return "Admission"

class feedback(models.Model):
        firstname = models.CharField(max_length=10)
        lastname = models.CharField(max_length=10)
        mobile_no = models.IntegerField()
        type = models.CharField(max_length=10)
        textcomment= models.TextField()

        def __str__(self): 
         return "Enquiryfrom"

class ragister(models.Model):
                username =models.CharField(max_length=10)
                email = models.EmailField(max_length=20)
                password = models.CharField(max_length=20)
                # password = models.CharField(max_length=20)

                def __str__(self): 
                 return "signup"
                