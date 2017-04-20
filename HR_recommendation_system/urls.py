from django.conf.urls import url

from HR_recommendation_system import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^recs$', views.recs, name='recs'),
    url(r'v1/login$', views.login),
    url(r'v1/register$', views.register),
    url(r'v1/getchallenges$', views.getChallenges),
    url(r'v1/getallrecs$', views.getAllRecs),
    url(r'v1/submission$', views.processSubmisson),
]
