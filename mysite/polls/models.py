from django.db import models


class movie_data(models.Model):
    movie_name=models.CharField(max_length=20,null=False)
    movie_poster=models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=100,null=False)
    movie_description = models.TextField(null=True)
    movie_created_date= models.DateField(null=False)
    movie_release_date=models.DateField(null=False)

    def __str__(self):
        return self.movie_name