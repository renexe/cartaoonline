# import pytest
# from django.test import Client
# from django.urls import reverse

# from conline.django_assertions import assert_contains


def test_test():
    return 1


# @pytest.fixture
# def resp(client, db):
#     resp = client.get(reverse('base:home'))
#     return resp
#
#
# def test_status_code(resp):
#     resp.status_code == 200
#
#
# def test_title(resp):
#     assert_contains(resp, '<title>Python Pro - Home</title>')
#
#
# def test_home_link(resp):
#     assert_contains(resp, f'href="{reverse("base:home")}">Python Pró</a>')
#
#
# def test_email_link(resp):
#     assert_contains(resp, 'href="mailto:rene.exe@gmail.com"')
