import pytest

pytestmark = [pytest.mark.unit, pytest.mark.django_db]

def test_profile_api(api_client):
    resp = api_client.get("/get-profile/")
