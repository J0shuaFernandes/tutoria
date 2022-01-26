from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tutorial, TutorialSeries, Message, Profile, Comment, Like

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .forms import NewUserForm

from datetime import datetime
from random import randint
import smtplib

def homepage(request):
	return render(request, 
					template_name='home.html',
					context={"series":TutorialSeries.objects.all()})

def another_name(request, pk):
	print(pk)
	tutorial = Tutorial.objects.all().filter(id=pk)
	print(tutorial)
	like = Like.objects.all().filter(tutorial_id=pk)
	print(like)
	return render(request, 'tutorial.html', {'tutorial':tutorial, 'like':like})		

def profile(request, username):
	if User.objects.get(username=username):
		remote_user = User.objects.get(username=username)
		series = TutorialSeries.objects.all().filter(author=username)
		return render(request, 
				template_name='profile.html',
				context={"series":series, "remote_user":remote_user})
	else:
		return render(request, 'not_found.html')

def edit_profile(request):
	return render(request,
					template_name='edit_profile.html', 
					context={"profile":Profile.objects.all()})

def comment(request, pk):
	#post = get_object_or_404(Tutorial, id=request.POST.get('tutorial_id'))	
	c = Comment(name=request.user.username, body=request.POST.get('comment'), date=datetime.now(), tutorial_id=pk)
	c.save()
	return HttpResponseRedirect(reverse('tutorial', args=[str(pk)]))

def like(request, pk):
	post = get_object_or_404(Tutorial, id=request.POST.get('tutorial_id'))
	like = Likes.objects.all().filter(tutorial_id=pk, user_id=request.user.id)
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(id=request.user.id)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('tutorial', args=[str(pk)]))

def chat(request, username):
	if User.objects.get(username=username):
		remote_user = User.objects.get(username=username)
		local_user = request.user
		# get all messages
		local_remote = Message.objects.filter(sender_id=local_user.id) & Message.objects.filter(receiver_id=remote_user.id)
		remote_local = Message.objects.filter(sender_id=remote_user.id) & Message.objects.filter(receiver_id=local_user.id)
		#messages = local_remote | remote_local
		messages = local_remote.union(remote_local)		
		messages.order_by('id')

		if request.method == 'POST':
			m = Message(sender_id=local_user.id, receiver_id=remote_user.id, content=request.POST.get('msg'), timestamp=datetime.now())	
			m.save()
		return render(request, 'chat.html', 
					context={"messages":messages, "remote_user":remote_user})
	else:
		return render(request, 'not_found.html')

def search(request):
	query = request.GET.get('q')
	series = TutorialSeries.objects.all().filter(series__contains=query)
	tutorials = (Tutorial.objects.all()).filter(title__contains=query)
	users = User.objects.all().filter(username__contains=query)
	return render(request, 'search.html',
					{"series":series, "tutorials":tutorials, "users":users})

def user_logout(request):
	logout(request)
	messages.info(request, "You've been logged out")
	return redirect('/')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			#username = form.cleaned_data.get('username')
			messages.success(request, 'Account Created')
			login(request, user)
			return redirect('/')
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = NewUserForm()
	return render(request,
					template_name='register.html',
					context={"form":form})