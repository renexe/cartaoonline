import pytest
from django.urls import reverse

from conline.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Procure um cartãO Online</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">cartãOOnline</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:renelima.dev@gmail.com"')
