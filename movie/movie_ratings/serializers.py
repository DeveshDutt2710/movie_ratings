from dataclasses import field
from rest_framework import serializers
from .models import MovieRatings



class MovieRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieRatings
        fields='__all__'
