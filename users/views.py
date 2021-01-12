from django.shortcuts import render

# Create your views here.
from .models import User, Group
from .forms import UserForm, GroupForm, user_form, group_form
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.views.generic import UpdateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.db.models import ProtectedError

from django.http import HttpResponse, HttpResponseRedirect

# framework 

from .serializers import UserSerializer, GroupSerializer
from rest_framework import generics

class api_user_create(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class api_group_create(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class user_create(CreateView):
	template_name = "user_create.html"
	form_class = user_form
	success_url = '/users'

class group_create(CreateView):
	template_name = "group_create.html"
	form_class = group_form
	success_url = '/groups'




class user_edit(UpdateView):
	template_name = "user_edit.html"
	form_class = user_form
	success_url = '/users'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(User, id=id_)

class group_edit(UpdateView):
	template_name = "group_edit.html"
	form_class = group_form
	success_url = '/groups'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Group, id=id_)

class user_delete(DeleteView):
	template_name = "user_delete.html"
	success_url = '/users'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(User, id=id_)

	def get_success_url(self):
		return "/users"

class group_delete(DeleteView):
	template_name = "group_delete.html"
	success_url = '/groups'


	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Group, id=id_)

	def post(self, request, *args, **kwargs):
		try:
			return self.delete(request, *args, **kwargs)
		except ProtectedError:
			return redirect('/error')

	def get_success_url(self):
		return "/groups"



def user_list(request):
	queryset = User.objects.all()

	context = {"object_list": queryset}
	return render(request, "user_list.html", context)

def group_list(request):
	queryset = Group.objects.all()

	context = {"object_list": queryset}
	return render(request, "group_list.html", context)


def error_page(request):
	return render(request, "error.html")


def user_show(request):
	names = {}
	dates = {}
	groups = {}

	for e in User.objects.all():
		uid = getattr(e, 'id')
		names[uid] = getattr(e, 'username')
		dates[uid] = getattr(e, 'date_joined')
		groups[uid] = getattr(e, 'group')

	context = {
	'username': names,
	'created': dates,
	'group': groups
	}

	return render(request,'users.html', context)




