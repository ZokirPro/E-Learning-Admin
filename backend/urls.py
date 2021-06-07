from django.urls import path,re_path
from . import views
urlpatterns=[
    # The home page
    path('', views.index, name='index'),
    re_path(r'^.*', views.other_html, name='template'),

  
]
