from django.db import models


# Create your models here.

def rating_choices():
    values = []
    i = round(1.0, 1)
    while i < 10.0:
        value = [round(i, 1), str(round(i, 1))]
        values.append(tuple(value))
        i += round(0.1, 1)
    return tuple(values)


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Movie(models.Model):
    RATING_CHOICES = rating_choices()
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, related_name='director', on_delete=models.CASCADE)
    screenplay = models.ForeignKey(Person, related_name='screenplay', on_delete=models.CASCADE)
    starring = models.ManyToManyField(Person, through='PersonMovie')
    year = models.IntegerField()
    rating = models.FloatField(choices=RATING_CHOICES, default=0.0)
    genre = models.ManyToManyField(Genre)


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128, null=True)

