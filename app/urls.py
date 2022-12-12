from django.urls import path
from .views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()