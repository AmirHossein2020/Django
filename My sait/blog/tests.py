from urllib import response
from django.forms import PasswordInput
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "amir",
            password = "2020"
        )
        self.post = Post.objects.create(
            title = "post title",
            body = "post body",
            author = self.user,
        )
    def test_string_model(self):
        post = Post(title="hello from test")
        self.assertEqual(str(post),post.title)

    def test_post_model(self):
        self.assertEqual(f'{self.post.title}', "post title")
        self.assertEqual(f'{self.post.body}', "post body")
        self.assertEqual(f'{self.post.author}', "amir")

    def test_post_list(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"blog/list.html")

    def test_post_detail(self):
        response = self.client.get('/blog/1/')
        no_response = self.client.get("/blog/10/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertTemplateUsed(response,"blog/detail.html")
    
    def test_get_absolute_ul(self):
        self.assertEqual(self.post.get_absolute_url(),'/blog/1/')

    def test_create_post(self):
        response = self.client.post(reverse("blog_new"),{
            'title':'new post',
            "body":"body new post",
            'author':self.user.pk,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last(),"new post")
        self.assertEqual(Post.objects.last(),"body new post")

    def test_update_post(self):
        response = self.client.post(reverse('blog_update',args="1"),{
            'title':"update title",
            'body':"update body",

        })
        self.assertEqual(response.status_code,302)

    def test_delete_post(self):
        response = self.client.post(reverse("blog_delete",args="1"))
        self.assertEqual(response.status_code,302)