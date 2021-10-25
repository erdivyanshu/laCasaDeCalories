from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=100)
     email= models.CharField(max_length=100)
     need= models.CharField(max_length=255)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return 'Contact for ' + self.need

class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     bio = models.TextField()
     profile_pic= models.ImageField(null=True, blank=True, upload_to="static/images/profile" )
     def __str__(self):
          return str(self.user)
#      # CATEGORY = (('Vaccine','Vaccine'), ('General-Bed','General-Bed'), ('Oxygen-Bed','Oxygen-Bed'),('Bed With-Ventilator','Bed With-Ventilator'))
#      sno= models.AutoField(primary_key=True)
#      first_name= models.CharField(max_length=200)
#      last_name= models.CharField(max_length=200)
#      email= models.IntegerField(null=True)
#      #for contact details
#      gender = models.TextField()
#      address = models.TextField()

#      timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

#      def __str__(self):
#           return self.first_name
