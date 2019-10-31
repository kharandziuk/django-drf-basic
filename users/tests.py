from django.urls import reverse

import pytest

from . import models, factories

pytestmark = pytest.mark.django_db

def test_create_user_and_set_password(django_app):
    response = django_app.post_json(
        reverse('users-list'),
        {
            'username': '\ud83d',
        }
    )
    assert response.status_code == 201
    assert models.User.objects.count() == 1

