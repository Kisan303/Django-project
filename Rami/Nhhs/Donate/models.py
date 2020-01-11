from django.db import models
from django.db import models
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import DateField
from django.db.models import BooleanField
from django.db.models import TextField


# Create your models here.
class User(models.Model):
	user_id=models.CharField(max_length=50)
	user_password=models.CharField(max_length=50)
	user_fullname=models.CharField(max_length=250)
	user_DOB=models.DateField()
	user_address=models.CharField(max_length=50)
	user_contact=models.IntegerField(10)
	user_age=models.IntegerField(10)
	
	def __str__(self):
		return self.user_id


class Donor(models.Model):
	email=models.CharField(max_length=250)
	donor_Firstname=models.CharField(max_length=250)
	donor_Middlename=models.CharField(max_length=250)
	donor_Lastname=models.CharField(max_length=250)
	address=models.CharField(max_length=250)
	contact=models.IntegerField(10)
	country=models.CharField(max_length=250)
	postal_code=models.IntegerField(50)
	state=models.CharField(max_length=250)
	city=models.CharField(max_length=250)
	donate_amt=models.IntegerField(50)
	donor_cartType=models.CharField(max_length=250)
	donor_acc=models.IntegerField(50)
	donate_date=models.DateField(50)
	card_id=models.IntegerField(10)
	card_expirationDate=models.DateField()
	comment=models.TextField()
	verify=models.BooleanField(10)
	users=models.ManyToManyField(User)
	
def __str__(self):
	return self.donor_acc

class Receiver(models.Model):
	email=models.CharField(max_length=250)
	full_name=models.CharField(max_length=250)
	address=models.CharField(max_length=250)
	contact=models.IntegerField(10)
	distribute_catagories=models.CharField(max_length=250)
	distribute_amt=models.IntegerField(15)
	distribute_date=models.DateField(50)
	receiver_acc=models.IntegerField(50)
	distribute_handcash=models.IntegerField(50)

	def __str__(self):
		return self.receiver_acc

class Organization(models.Model):
	email=models.CharField(max_length=250)
	password=models.CharField(max_length=250)
	address=models.CharField(max_length=250)
	contact=models.IntegerField(10)
	totalAmt=models.IntegerField(50)
	bankAcc=models.IntegerField(50)
	donors=models.ForeignKey(Donor, on_delete=models.CASCADE)
	receivers=models.ForeignKey(Receiver, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.email




