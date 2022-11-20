from django.urls import path
from apps.profiles.views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
	path('home/',home_view, name='home'),

]