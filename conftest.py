import pytest
from rest_framework.test import APIClient

pytestmark = [pytest.mark.django_db]

@pytest.fixture
def api_client():
    return APIClient()