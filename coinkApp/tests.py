from django.test import TestCase
from coinkApp.models import UserBasic


class UserBasicTestCase(TestCase):
    def create_user_basic(self):
        return UserBasic.objects.create(
            fullname='Pepito Perez',
            email='pepito@correo.com',
            city='Bogotá D.C.'
        )

    def test_user_basic_creation(self):
        user = self.create_user_basic()
        self.assertTrue(isinstance(user, UserBasic))
        self.assertEqual(user.__str__(), user.fullname)
