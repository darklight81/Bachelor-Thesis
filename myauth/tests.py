import os

from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import UsersView
# Create your tests here.
from myauth.models import User
if __name__ == "__main__":
    DJANGO_SETTINGS_MODULE = 'bachelorthesis_v2.settings'
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bachelorthesis_v2.settings")
    user = User.objects.get(username='lolskiller')
    view = UsersView.as_view()
    factory = APIRequestFactory()
    request = factory.get('/api/users')
    force_authenticate(request, user=user)
    response = view(request)
