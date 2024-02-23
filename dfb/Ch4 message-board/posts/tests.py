from django.test import TestCase
from .models import Post

class PostsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, "just a test")



# Create your tests here.
