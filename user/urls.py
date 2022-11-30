from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.login_view, name='login'),
	path('logout', views.logout_view, name='logout'),
	path('register', views.register, name='register'),
	path('detail', views.detail, name='detail'),
]