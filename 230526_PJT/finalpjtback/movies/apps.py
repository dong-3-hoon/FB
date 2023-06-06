from django.apps import AppConfig
# from django.core.management import call_command


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
    
    
#     def ready(self):
#         call_command('loaddata', 'C:/Users/SSAFY/Desktop/final-pjt/finalpjtback/movies/fixtures/movielist.json')
#         # call_command('loaddata', 'C:/Users/SSAFY/Desktop/final-pjt/finalpjtback/movies/fixtures/upcomming_movies.json')