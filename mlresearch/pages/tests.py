from django.test import SimpleTestCase
from django.urls import resolve, reverse


from .views import HomePageView


class HomepageTest(SimpleTestCase):

    def setUp(self):  # new
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


