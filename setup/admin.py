from django.contrib import admin
from setup.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'running_time', 'year_released', 'gender')
    search_fields = ('title', 'gender')
    list_filter = ('year_released', 'gender', 'indicative_rating', 'nationality')

admin.site.register(Movie, MovieAdmin)



