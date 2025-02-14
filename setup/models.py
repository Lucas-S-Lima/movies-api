from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)   #titulo
    description = models.TextField(null=False, blank=False)   # descrição
    gender = models.CharField(max_length=50)   # genero
    running_time = models.IntegerField(null=False, blank=False)   # tempo de duração
    year_released = models.PositiveIntegerField(null=False, blank=False)   # ano de lançamento
    indicative_rating = models.IntegerField(null=True, blank=True)   # classificação indicativa
    nationality = models.CharField(max_length=50)   # nacionalidade
    cast = models.TextField(null=True, blank=True)   # elenco

    def __str__(self):
        return self.title
    
   

