from django import forms
from django.db import models
from .models import User
from .models import Group


class user_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'group']

class group_form(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['groupname', 'description']


class UserForm(forms.Form):
	username = forms.CharField(max_length=20)
	group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

class GroupForm(forms.Form):
	groupname = forms.CharField(max_length=20)
	description = forms.CharField(max_length=200, required=False)