from django.test import TestCase
from .models import post


class blogTests(TestCase):
    def setUp(self):
        post.objects.create(
            title="My title",
            body="Just a test",
        )

    def test_string_represantation(self):
        Post = post(title="My entry title")
        self.assertEqual(str(Post), Post.title)

    def test_post_list_view(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My title")
        self.assertTemplateUsed(response, "blog/blog.html")

    def test_post_detail_view(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My title")
        self.assertTemplateUsed(response, "blog/post.html")
