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
    path('<int:post_id>/comments/create/', views.comments_create, name="comments_create"),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name="comments_delete"),
    path('question/', views.go_question,name='go_question'),
    
]