from django.test import TestCase

# Create your tests here.

from .models import Post


class PostModeTest(TestCase):
    def setup(self):
        Post.objects.create(text='Just a damn test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Just a damn test')