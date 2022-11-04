from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    class Meta:
        db_table = "genre"
    name = models.CharField(max_length=70, default="")


class Webtoon(models.Model):
    class Meta:
        db_table = "webtoon"
    # id,title,day,genre,story,webtoon_url,thumbnail_url
    title = models.CharField(max_length=50, default="")
    day = models.CharField(max_length=50, default="")
    genre = models.ManyToManyField(Genre, related_name="genre_set")
    story = models.TextField(max_length=500, default="")
    webtoon_url = models.URLField(max_length=300, default="")  # a href = "webtoon_url"
    thumbnail_url = models.URLField(max_length=300, default="")  # img src = "thumbnail_url"
    bookmark = models.ManyToManyField(User, related_name='bookmark_set', blank=True)

    def __str__(self):
        return str(self.title)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    my_score = models.FloatField(validators=[MinValueValidator(0,5),MaxValueValidator(5.0)]) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment)
