from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
]
# assigning a view called post_list to ^$ URL. This
# regular expression will match ^ (a beginning) followed by $(an end) - so 
# only an empty string will match.