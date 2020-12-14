from django.urls import path
from . import views

app_name = 'theatre'

urlpatterns = [
    path('', views.index, name='index'),
    path('theatre/allMovies/', views.allMovies, name='allMovies'),
    path('theatre/checkAvailability/<str:movieTitle>',
         views.checkAvailability, name='checkAvailability'),
    path('theatre/buyMovie/<str:movieTitle>', views.buyMovie, name='buyMovie'),
    path('theatre/myMovies/', views.myMovies, name='myMovies'),
    path('theatre/movie/<path:clip>', views.movieView, name='movieView'),
    path('theatre/register/', views.registerPage, name='register'),
    path('theatre/login/', views.loginPage, name='login'),
    path('theatre/logout/', views.logoutUser, name='logout'),
]
