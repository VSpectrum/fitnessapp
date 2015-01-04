from django.conf.urls import patterns, include, url
from django.contrib import admin
from FitnessApp import views

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^dashboard$', views.dashboard),
    
    url(r'^dataVisualization$', views.datavisualization),

    url(r'^manageUsers$', views.userman),
    url(r'^createUser$', views.usercreate),
    url(r'^searchUser$', views.searchuser),
    url(r'^deleteUser$', views.deleteuser),
    url(r'^showAllUsers$', views.showallusers),

    url(r'^manageEquipment$', views.equipman),
    url(r'^createEquip$', views.equipcreate),
    url(r'^searchEquip$', views.equipsearch),
    url(r'^deleteEquip$', views.equipdelete),
    url(r'^showAllEquip$', views.showallequip),
)
