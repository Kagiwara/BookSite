from django.urls import path
from . import views
from .views import BookCreate

urlpatterns = [
    path('', views.index),
    path('reviews', views.reviews),
    path('book', views.book),
    path('sign', views.sign),
    path('create/', BookCreate.as_view()),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete')
]
