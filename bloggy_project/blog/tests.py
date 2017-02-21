from django.test import TestCase
from blog.models import Post

class PostTests(TestCase):
    def test_str(self):
        my_title = Post(title="Basic title for test case")
        self.assertEquals(str(my_title), 'Basic title for test case',)
