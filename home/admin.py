from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from .models import Tutorial, TutorialSeries, Comment, CommentChildren, Message, Profile 

class TutorialAdmin(admin.ModelAdmin):
	list_display = ('title','date','series')
	list_filter = ('date',)
	fieldsets = [
		("Tutorial Detials", {"fields":["title","date"]}),
        ("URL", {'fields': ["slug"]}),
        ("Series", {'fields': ["series","date"]}),
		("Content", {"fields":["content"]}),
	]

	formfield_overrides = {
		models.TextField: {'widget':TinyMCE()}
	}

admin.site.site_header = 'tutoria'
admin.site.index_title = 'Add/Change/Remove Tutorials'
admin.site.content = 'Sample'

admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Comment)
admin.site.register(CommentChildren)
admin.site.register(Message)
admin.site.register(Profile)