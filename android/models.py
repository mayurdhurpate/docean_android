from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	token=models.CharField(unique=True,max_length=1000)
	def _str_(self):
		return "%s" % (self.name)
	def _unicode_(self):
		return "%s" % (self.name)
	
class Noti(models.Model):
	api_key=models.CharField(max_length=1000)
	def _str_(self):
                return "%s" % (self.api_key)
        def _unicode_(self):
                return "%s" % (self.api_key)


class Message(models.Model):
    sender = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    sender_id = models.CharField(max_length=1000)
