from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('new/',views.create,name='create'),   
    path('new2/',views.new,name='new'),
    path('<int:article_id>/', views.detail,name='detail'),
    path('<int:article_id>/edit/', views.update,name='update'),

]