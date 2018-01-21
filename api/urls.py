from django.conf.urls import url, include
from rest_framework import routers
from forcast import views as forcast_views   
from authorization import views as authorization_views

# route for 2 end points 
# for  bigger apps better delegate routing to its own urls.py
urlpatterns = [
    url(r'^api/auth/login/$', authorization_views.Login.as_view()),
    url(r'^api/forcast/today/(?P<city>.+)$', forcast_views.ForcastDetails.as_view()),
]
 