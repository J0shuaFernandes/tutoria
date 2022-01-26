from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .models import Comment, Message

class ChatForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['sender', 'receiver', 'timestamp']
        widgets = {

        }
"""
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['sender', 'receiver', 'timestamp']
        model.is_staff = True
        fields = ("user", "email", "body")
"""
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        model.is_staff = True
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.is_staff = True
            user.save()
            group = Group.objects.get(name='Contributor')
            user.groups.add(group) 
        return user