from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Webtoon(models.Model):
    # id,title,day,genre,story,webtoon_url,thumbnail_url
    title = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    story = models.TextField()
    # field_name = models.URLField(max_length=200, **options) / options link [ https://www.geeksforgeeks.org/urlfield-django-models/#field-options ]
    webtoon_url = models.URLField(max_length=300)  # a href = "webtoon_url"
    thumbnail_url = models.URLField(max_length=300)  # img src = "thumbnail_url"
    bookmark = models.ManyToManyField(User, related_name='bookmark_set', blank=True)

    def __str__(self):
        return str(self.title)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_user")
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    my_score = models.FloatField(validators=[MinValueValidator(0,5),MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment)
