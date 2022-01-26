from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

from django.views.generic import ListView, DetailView
from home.models import Tutorial, TutorialSeries

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Tutorial, 
		template_name="tutorial.html"), name='tutorial'),
	url(r'manage/', admin.site.urls, name='manage'),
	#path(r'tutorial/<int:pk>', views.another_name, name="tutorial"),
	path(r'like/<int:pk>', views.like, name="like"),
	path(r'comment/<int:pk>', views.comment, name="comment"),
	url(r'register/', views.register, name='register'),
	url(r'login/', views.user_login, name='login'),
	url(r'logout/', views.user_logout, name='logout'),
	path(r'chat/<str:username>', views.chat, name='chat'),
	#path(r'chat/<str:username>', views.save_msg, name='save_msg'),
	path(r'profile/<str:username>', views.profile, name='profile'),
	url(r'edit_profile/', views.edit_profile, name='edit_profile'),
	url(r'search/', views.search, name='search'),
	path(r'reset_password/', auth_views.PasswordResetView.as_view(), 
			name="password_reset"),
	path(r'reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), 
					name="password_reset_done"),
	path(r'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
					name="password_reset_confirm"),
	path(r'reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), 
					name="password_reset_conmplete"),
]

"""

	"""

"""
'django.contrib.auth.views.password_reset_confirm'
'reset/<uidb64>/<token>/'
url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(),
	name='password_reset_confirm'),
"""
"""

"""

"""
	url(r'reset_password/', views.reset_password, name='reset_password'),
	url(r'reset_password_done/', views.reset_password_done, name='reset_password_done'),
	url(r'reset_password_confirm/', views.reset_password_confirm, name='reset_password_confirm'),
	url(r'reset_password_complete/', views.reset_password_complete, name='reset_password_complete'),
"""