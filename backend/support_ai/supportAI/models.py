from django.db import models

# Create your models here.

class Customer(models.Model):

 name=models.CharField(max_length=200)

 email=models.EmailField(unique=True)

 def __str__(self):

  return self.name



class Subscription(models.Model):

 customer=models.ForeignKey(

 Customer,

 on_delete=models.CASCADE

 )

 provider=models.CharField(

 max_length=100,

 db_index=True

 )

 plan_name=models.CharField(

 max_length=200

 )

 last_renewed_date=models.DateField()

 billing_cycle=models.CharField(

 max_length=50

 )

 auto_renew=models.BooleanField()

 trial_end=models.DateField(

 null=True,

 blank=True

 )

 amount=models.FloatField()

 status=models.CharField(

 max_length=50,

 default="active"
 )

 def __str__(self):

  return self.provider