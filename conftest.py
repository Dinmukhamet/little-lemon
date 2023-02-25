import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from restaurant.tests.factories import UserFactory


@pytest.fixture
def authorized_client():
    user = UserFactory()
    token, _ = Token.objects.get_or_create(user=user)
    client = APIClient()
    client.force_authenticate(user=user, token=token.key)
    return client