from django.conf.urls import url
from .views import search_by_name
urlpatterns = [
    url(r"^commodity$",search_by_name),
]