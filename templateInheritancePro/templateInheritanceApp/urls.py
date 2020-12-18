from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'templateInheritanceApp'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
