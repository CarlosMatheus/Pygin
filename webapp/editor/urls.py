from . import views
from django.urls import path


urlpatterns = [
    path('', views.SimpleModelListCreator.as_view()),
]
