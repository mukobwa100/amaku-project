from django.urls import path
from . import views

urlpatterns=[
    path('amakuru/' ,views.amakuru),
    path('imikino/' ,views.imikino)
]
