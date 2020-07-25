
from django.urls import path,include
from . import views

from .views import save_data, index

urlpatterns=[
    path('',views.index,name='index'),
    path('myblog',views.save_data,name='save_data'),
    path('getdata',views.get_data,name='getdata'),

]