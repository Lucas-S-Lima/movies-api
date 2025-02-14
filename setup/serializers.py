from rest_framework import serializers
from setup.models import Movie

class MovieSerializer(serializers.ModelSerializer): # classe que irá serializar os dados 
    
    class Meta:
        model = Movie
        fields = '__all__'