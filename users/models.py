from django.db import models
from django.conf import settings

# Create your models here.

class Group(models.Model):
	#ID, Name, Description, Actions
	groupname = models.CharField(max_length=20)
	description = models.CharField(max_length=200, blank=True, null=True)
	#To make in name, not objXXX
	def __str__(self):
		return self.groupname

class User(models.Model):
	#username, created, group, actions
	username = models.CharField(max_length=20)
	date_joined = models.DateField(auto_now=False, auto_now_add=True)
	group = models.ForeignKey(Group, on_delete=models.PROTECT, blank=True, null=True)
	#To make in name, not objXXX
	def __str__(self):
		return self.username

