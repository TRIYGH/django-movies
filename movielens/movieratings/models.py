from django.db import models
from django.contrib.auth.models import User
from collections import OrderedDict
# from django.core.urlresolvers import reverse
# from django.contrib.auth import get_user_model


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {}".format(self.title, self.genre)

    def genres_list(self):
        return self.genre.split('|')


class Rater(models.Model):
    gender = models.CharField(max_length=2)
    age = models.IntegerField()
    occupation = models.IntegerField()
    user = models.OneToOneField(User, null=True)
    # zipcode = models.CharField(max_length=10)

    def __str__(self):
        return "{}: {}, {}, {}".format(self.id, self.gender, self.age, self.occupation)

    def movies_not_rated(self):
        return Movie.objects.exclude(id__in=self.rating_set.all())

    def liked_movies(self):
        return [rating.movie for rating in self.rating_set.all() if rating.score >= 4]

    def disliked_movies(self):
        return [rating.movie for rating in self.rating_set.all() if rating.score <= 2]

    def favorite_genres(self):
        movies = self.liked_movies()
        genre_dict = {}
        for movie in movies:
            genre_list = movie.genres_list()
            for genre in genre_list:
                try:
                    genre_dict[genre] += 1
                except:
                    genre_dict[genre] = 1
        return list(OrderedDict(sorted(genre_dict.items(), key=lambda t: t[1])))[::-1]

    def occupation_word(self):
        context_tuple = ((0, 'other'),
                         (1, 'academic/educator'),
                         (2, 'artist'),
                         (3, 'clerical/admin'),
                         (4, 'college/grad student'),
                         (5, 'customer service'),
                         (6, 'doctor/health care'),
                         (7, 'executive/managerial'),
                         (8, 'farmer'),
                         (9, 'homemaker'),
                         (10, 'K-12 student'),
                         (11, 'lawyer'),
                         (12, 'programmer'),
                         (13, 'retired'),
                         (14, 'sales/marketing'),
                         (15, 'scientist'),
                         (16, 'self-employed'),
                         (17, 'technician/engineer'),
                         (18, 'tradesman/craftsman'),
                         (19, 'unemployed'),
                         (20, 'writer'))
        return context_tuple[self.occupation][1]

    def age_bracket(self):
        context_dictionary = {1: "Under 18",
                              18: "18-24",
                              25: "25-34",
                              35: "35-44",
                              45: "45-49",
                              50: "50-55",
                              56: "56+"}

        return context_dictionary[self.age]


class Rating(models.Model):
    score = models.IntegerField()
    # timestamp = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse('movieratings:movie_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return ("Rater: {}, Movie: {}, Score: {}".format(self.rater_id, self.movie.title, self.score))


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
