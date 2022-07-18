from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse

from .movie_ratings_service import MovieRatingsService




class CreateMovieRatingsView(APIView):

    def post(self, request, *args, **kwargs):
        
        manager = MovieRatingsService()
        response = manager.create_movie_rating(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class UpdateMovieRatingsView(APIView):

    def post(self, request, *args, **kwargs):
        
        manager = MovieRatingsService()
        response = manager.update_movie_rating(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


class GetAllMovieRatingsView(APIView):

    def get(self, request, *args, **kwargs):
        
        manager = MovieRatingsService()
        response = manager.get_all_movie_ratings()

        return JsonResponse(response, status=status_codes.HTTP_200_OK)

class GetMovieRatingsByIdView(APIView):

    def get(self, request, *args, **kwargs):
        
        manager = MovieRatingsService()
        response = manager.get_movie_rating_by_id(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)

class DeleteMovieRatingsView(APIView):

    def post(self, request, *args, **kwargs):
        
        manager = MovieRatingsService()
        response = manager.delete_movie_rating(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)


