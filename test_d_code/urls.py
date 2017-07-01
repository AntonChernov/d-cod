from django.conf.urls import url
from .views import return_empty_page, return_charts

urlpatterns = [
    url(r'^$', return_empty_page),
    url(r'^charts/', return_charts),
]