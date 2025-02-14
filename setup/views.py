from rest_framework import generics
from setup.models import Movie
from setup.serializers import MovieSerializer


class MoviesListView(generics.ListAPIView): # view que lista os filmes
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get']

class MoviesCreateView(generics.CreateAPIView): # view que cria os filmes
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['post']

class MoviesDestroyView(generics.DestroyAPIView): # view que deleta os filmes
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['delete']

class MoviesUpdateView(generics.UpdateAPIView): # view que altera os filmes
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['patch']

