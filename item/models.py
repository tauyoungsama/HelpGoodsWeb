from django.db import models
from user.models import User

# Create your models here.
class Item(models.Model):
	id = models.AutoField(primary_key=True)
	categlory = models.CharField(max_length=128, default='Item')
	itemname = models.CharField(max_length=128)
	description = models.CharField(max_length=1024)
	publisher = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	email = models.EmailField()

	@classmethod
	def create(self, categlory, itemname, description, publisher, address, phone, email):
		return self(categlory=categlory, itemname=itemname, description=description, publisher=publisher, address=address, phone=phone, email=email)