from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('register/', views.register, name='register'),
  path('login/', views.user_login, name= 'login'),
  path('logout/', views.user_logout, name='logout'),
  path("list", views.room_list, name="room_list"),
  path("book/<int:room_id>/", views.book_room, name="book_room"),
  path("delete/<int:booking_id>/", views.delete_booking, name="delete_booking"),
  path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
]