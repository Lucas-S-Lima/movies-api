from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MoviesListView.as_view(), name='movies-list'),
    path('movies/create/', views.MoviesCreateView.as_view(), name='movies-create'),
    path('movies/delete/<int:pk>/', views.MoviesDestroyView.as_view(), name='movies-delete'),
    path('movies/update/<int:pk>/', views.MoviesUpdateView.as_view(), name='movies-update'),

]
