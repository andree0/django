"""myFilmweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Filmwebapp.views import movies
from Filmwebapp.views import movie_details
from Filmwebapp.views import persons
from Filmwebapp.views import edit_person
from Filmwebapp.views import start_html
from Filmwebapp.views import add_person
# from Filmwebapp.views import add_movie
# from Filmwebapp.views import edit_movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_html),
    path('movies/', movies),
    path('movie_details/<int:movie_id>/', movie_details),
    path('persons/', persons),
    path('edit_person/<int:person_id>', edit_person),
    path('add_person/', add_person),
    # path('edit_movie/<int:movie_id>/', edit_movie),
    # path('add_movie/', add_movie),
]