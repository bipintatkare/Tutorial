from django.urls import path
from .views import index, create_form


urlpatterns = [
    path('', index, name="index"),
    path('create/', create_form, name="create")
]
