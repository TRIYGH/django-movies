from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

app_name = 'movieratings'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^toprated', views.TopRated.as_view(), name='toprated'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^allmovies', views.AllMovies.as_view(), name='all_movies'),
    url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieDetail.as_view(), name='movie_detail'),
    url(r'^rater/(?P<pk>[0-9]+)/$', views.RaterDetail.as_view(), name='rater_detail'),
    url(r'^register/$', views.register, name='register'), # these 3: conflicting with prior auths urls?
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^index/$', views.index, name='index'),

    ]
# user auth urls
# url(r'^accounts/auth/$', views.auth_view),
# url(r'^accounts/login/$', views.signin),
# url(r'^accounts/logout/$', views.signout, {'next_page': '/accounts/signin'})]
# url(r'^accounts/loggedin/$', views.signedin),
# url(r'^accounts/invalid/$', views.invalid_login)]
