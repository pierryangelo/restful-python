from django.urls import path, include
from games import views

urlpatterns = [
    path(r'game-categories/', views.GameCategoryList.as_view(),
         name=views.GameCategoryList.name),
    path(r'game-categories/<int:pk>/', views.GameCategoryDetail.as_view(),
         name=views.GameCategoryDetail.name),
    path(r'games/', views.GameList.as_view(),
         name=views.GameList.name),
    path(r'games/<int:pk>/', views.GameDetail.as_view(),
         name=views.GameDetail.name),
    path(r'players/', views.PlayerList.as_view(),
         name=views.PlayerList.name),
    path(r'players/<int:pk>/', views.PlayerDetail.as_view(),
         name=views.PlayerDetail.name),
    path(r'player-scores/', views.PlayerScoreList.as_view(),
         name=views.PlayerScoreList.name),
    path(r'player-scores/<int:pk>/', views.PlayerScoreDetail.as_view(),
         name=views.PlayerScoreDetail.name),
    path(r'users/', views.UserList.as_view(),
         name=views.UserList.name),
    path(r'users/<int:pk>/', views.UserDetail.as_view(),
         name=views.UserDetail.name),
    path(r'', views.ApiRoot.as_view(),
         name=views.ApiRoot.name),
]
