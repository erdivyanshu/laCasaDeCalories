from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "laCasaDeCalories Portal"
admin.site.site_title = "laCasaDeCalories"
admin.site.index_title = "Welcome!In laCasaDeCalories Portal"

urlpatterns = [
    path("home",views.index, name='home'),
    path("catalog",views.catalog, name='catalog'),
     path('signup', views.signup, name="signup"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('contact', views.contact, name="contact"),
]
