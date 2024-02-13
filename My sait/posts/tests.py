from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        excepted_objects_name = f'{post.text}'
        self.assertEqual(excepted_objects_name,"just a test")

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is another test')

    def text_view_url_location(self):
        resp = self.client.get('posts')
        self.assertEqual(resp.status_code,200)

    def test_view_url_name(self):
        resp = self.client.get(reverse('post_list'))
        self.assertEqual(resp.status_code,200)

    def test_view_template(self):
        resp = self.client.get(reverse('post_list'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateNotUsed(resp,'posts/list_html')