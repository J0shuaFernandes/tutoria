from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime
from tinymce.widgets import TinyMCE

class Profile(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()

	def __str__(self):
		return str(self.user)

class TutorialSeries(models.Model):
	series = models.CharField(max_length=200)
	date = models.DateTimeField("Date Published", default=datetime.now())
	author = models.TextField(default='', editable=True)
	description = models.CharField(max_length=200)
	slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Series"

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.series

class Tutorial(models.Model):
	title = models.CharField(max_length=45)
	date = models.DateTimeField("Date Published", default=datetime.now())
	author = models.TextField(default='', editable=True)
	content = models.TextField()

	series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", related_name="tutorials", on_delete=models.SET_DEFAULT)
	slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.title

class Like(models.Model):
	tutorial = models.ForeignKey(Tutorial, default=1, related_name="likes", on_delete=models.CASCADE)	
	user = models.ForeignKey(User, default=1, related_name="user_likes", on_delete=models.CASCADE)	

class Comment(models.Model):
	tutorial = models.ForeignKey(Tutorial, default=1, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField("Date Published", auto_now_add=True)

	def __str__(self):
		return self.tutorial.title

class CommentChildren(models.Model):
	Comment = models.ForeignKey(Comment, default=1, related_name="children", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField("Date Published", auto_now_add=True)

	def __str__(self):
		return self.tutorial.title

class Message(models.Model):
	sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
	receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
	#sender = models.TextField(default='user123', editable=True)
	#receiver = models.TextField(default='joshuaf319', editable=True)

	timestamp = models.DateTimeField("Date Published", default=datetime.now())
	content = models.TextField()

	def __str__(self):
		return self.sender

class ResetPassword(models.Model):
	email = models.TextField()
	OTP = models.IntegerField()

	def __str__(self):
		return self.email


"""
make user return a string 
def get_first_name(self):
    return self.username
User.add_to_class("__str__", get_first_name)
"""