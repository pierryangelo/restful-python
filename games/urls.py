from django.urls import path, include
from games import views

urlpatterns = [
    path(r'games/', views.game_list),
    path(r'games/<int:pk>', views.game_detail),
]