from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from tests.test_class_base import TestBase


class TestLoginViewPostMethod(TestBase):
    def test_login_view_post_method_with_data(self):
        user = self.create_test_user(username="teste", password="teste")
        response = self.client.post(reverse("login"), {"username": "teste", "password": "teste"})
        self.assertIsNotNone(user)
        self.assertRedirects(response, reverse("my_offers"))

    def test_login_view_post_method_when_user_is_none(self):
        user = None
        response = self.client.post(reverse("login"), {"username": "naoexiste", "password": "naoexiste"})
        form = response.context.get('auth_form')
        self.assertIsNotNone(form)
        self.assertIsInstance(form, AuthenticationForm)


class TestLogoutViewRedirectUrl(TestBase):
    def test_logout_view_redirect_url(self):
        username = "teste"
        password = "teste"
        user = self.create_test_user(username=username, password=password)
        self.client.login(username=username, password=password)
        response = self.client.get(reverse("logout"), follow=True)
        self.assertRedirects(response, reverse("job_list"))
