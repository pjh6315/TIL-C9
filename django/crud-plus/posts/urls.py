from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('naver/<str:q>/', views.naver),
    path('github/<str:username>/', views.github),
    path('', views.index, name='list'),
    path('create/',views.create, name='create'),
    path('write/',views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    
]