from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Test group name',
            slug='test_slug',
            description='Test description',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Test post',
        )

    def test_models_have_correct_object_names(self):
        value_posts = self.post.text[:15]
        self.assertEqual(str(self.post), value_posts, value_posts)

    def test_models_have_correct_object_title(self):
        value_groups = self.group.title
        self.assertEqual(str(self.group), value_groups)
