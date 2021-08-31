from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('kizaru/base/', done),
]