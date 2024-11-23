from django.urls import re_path as url
from runcard.views import barcodepage, search_for_runcard

urlpatterns = [
    url(r'search', search_for_runcard, name='search'),
    url(r'', barcodepage, name='barcodepage'),
]