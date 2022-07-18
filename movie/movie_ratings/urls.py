from django.urls import path

from .views import (CreateMovieRatingsView, DeleteMovieRatingsView, GetMovieRatingsByIdView,
                    UpdateMovieRatingsView,GetAllMovieRatingsView)

urlpatterns = [
    path('create', CreateMovieRatingsView.as_view(), name='create_movie_rating'),
    path('update', UpdateMovieRatingsView.as_view(), name='update_movie_rating'),
    path('', GetAllMovieRatingsView.as_view(), name='get_all_movie_ratings'),
    path('get', GetMovieRatingsByIdView.as_view(), name='get_specific_movie_rating'),
    path('delete', DeleteMovieRatingsView.as_view(), name='delete_movie_rating'),
]