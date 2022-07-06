import pytest

pytestmark = [pytest.mark.unit, pytest.mark.django_db]


def test_profile_api(api_client):
    resp = api_client.get("http://localhost:8000/api/get-profile/")
    assert "profile_image" in resp.data
    assert "backprofile_image" in resp.data
    assert "profession" in resp.data

    # resp = api_client.post(
    #     "http://localhost:8000/api/get-profile/", data=dict(about_user="this is about"), format="json"
    # )
    # assert resp.data['about_user'] == 'this is about'