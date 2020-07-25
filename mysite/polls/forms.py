from django import forms

from .models import movie_data


class MovieForm(forms.Form):


    # class Meta:
    #     model= movie_data
    #     fields= '__all__'
    movie_name=forms.CharField()
    movie_poster=forms.ImageField()
    movie_description = forms.CharField()
    movie_created_date= forms.DateField(help_text = "must be in YYYY-MM-DD format")
    movie_release_date=forms.DateField(help_text = "must be in YYYY-MM-DD format")