import imp
from .serializers import MovieRatingSerializer
from .models import MovieRatings


class MovieRatingsService():
    account_id = None
    page = 1
    page_size = 10

    def __init__(self, account_id: str = None, page: int = 1, page_size: int = 10):
        self.set_account_id(account_id)
        self.page = page
        self.page_size = page_size

    def set_account_id(self, account_id):
        self.account_id = (str)(account_id)

    def get_profile_id(self):
        return self.account_id
     

    def _save_profile(self, account):
        
        saved_account = account.save()
        return saved_account
        

    

    def create_movie_rating(self,data) -> dict:
        saved_movie_rating = MovieRatings(**data).save()
        movie_rating_details = MovieRatingSerializer(saved_movie_rating)

        
    
      
        response = {
            'success': True,
            'non_serializer_respons':{
                "id":saved_movie_rating.uuid,
                "name":saved_movie_rating.name,
                "description":saved_movie_rating.description,
                "rating":saved_movie_rating.rating
            },
            "movie_rating":movie_rating_details.data
        }

        return response

    
    def update_movie_rating(self,data) -> dict:
        

        response = {
            'success': True,
            'message':"an OTP has been successfully sent to your mobile number"
        }

        return response

    
    def get_all_movie_ratings(self) -> dict:
        movie_ratings = MovieRatings.objects.all()
        movie_ratings_details = MovieRatingSerializer(movie_ratings,many=True)
        

        response = {
            'success': True,
            "movie_ratings":movie_ratings_details.data
        }

        return response

    def get_movie_rating_by_id(self,data) -> dict:
        uuid = data['uuid']

        movie_rating = MovieRatings.objects.get(pk = uuid)

        movie_rating_details = MovieRatingSerializer(movie_rating)
        

        response = {
            'success': True,
            "movie_rating":movie_rating_details.data
        }

        return response

    def delete_movie_rating(self,data) -> dict:
        

        response = {
            'success': True,
            'message':"an OTP has been successfully sent to your mobile number"
        }

        return response