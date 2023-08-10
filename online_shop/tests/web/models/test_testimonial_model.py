from django.test import TestCase
from django.contrib.auth import get_user_model

from online_shop.web.models import Testimonial

UserModel = get_user_model()


class TestimonialModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        Testimonial.objects.create(
            user=cls.user,
            rating=5,
            comment='Great experience!'
        )

    def test_user_relationship(self):
        testimonial = Testimonial.objects.get(id=1)
        self.assertEqual(testimonial.user, self.user)

    def test_rating_choices(self):
        testimonial = Testimonial.objects.get(id=1)
        self.assertIn(testimonial.rating, [1, 2, 3, 4, 5])

    def test_comment_max_length(self):
        testimonial = Testimonial.objects.get(id=1)
        max_length = testimonial._meta.get_field('comment').max_length
        self.assertEqual(max_length, 300)
