from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        cls.post1 = Post.objects.create(
            title="First Blog Post",
            text="This is my first blog post.",
            author=user,
            status=Post.Status.PUBLISHED,
        )

        cls.post2 = Post.objects.create(
            title="Second Blog Post",
            text="This is a draft blog post.",
            author=user,
            status=Post.Status.DRAFT,
        )

    def test_post_list_direct_url(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_post_list_named_url(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_list_contains_title(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertContains(response, self.post1.title)

    def test_post_list_uses_correct_template(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_post_detail_direct_url(self):
        response = self.client.get(f"/blog/{self.post1.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_post_detail_named_url(self):
        url = reverse("blog:post_detail", args=[self.post1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_contains_title_and_text(self):
        url = reverse("blog:post_detail", args=[self.post1.pk])
        response = self.client.get(url)
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_detail_uses_correct_template(self):
        url = reverse("blog:post_detail", args=[self.post1.pk])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "blog/post_detail.html")

    def test_post_detail_returns_404_if_post_missing(self):
        url = reverse("blog:post_detail", args=[999999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_shown_in_list(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_page(self):
        response = self.client.get(reverse("blog:post_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_create.html")
        self.assertContains(response, "Add New Post")

    def test_post_create_contains_form(self):

        response = self.client.get(
            reverse("blog:post_create")
        )

        self.assertContains(
            response,
            "name=\"title\""
        )

        self.assertContains(
            response,
            "name=\"text\""
        )
    def test_create_post(self):

        response = self.client.post(
            reverse("blog:post_create"),
            {
                "title": "Form Post",
                "text": "Created with ModelForm",
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            Post.objects.filter(
                title="Form Post"
            ).exists()
        )

    def test_create_post_redirects(self):

        response = self.client.post(
            reverse("blog:post_create"),
            {
                "title": "New Post",
                "text": "Testing redirect",
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )