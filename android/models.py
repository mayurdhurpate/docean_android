from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	token=models.CharField(unique=True,max_length=1000)
	def __str__(self):
		return "%s" % (self.name)
	def __unicode__(self):
		return "%s" % (self.name)
	
class Noti(models.Model):
	api_key=models.CharField(max_length=1000)
	def __str__(self):
                return "%s" % (self.api_key)
	def __unicode__(self):
                return "%s" % (self.api_key)


class Message(models.Model):
    sender = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    token = models.CharField(max_length=1000)
    message_id = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
                return "%s %s %s %s " % (self.message,self.sender,self.token,self.message_id)
    def __unicode__(self):
                return "%s %s %s %s" % (self.message,self.sender,self.token,self.message_id)
