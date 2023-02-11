from django.contrib.auth import get_user
from django.test import TestCase
from django.urls import reverse

from users.models import Profile


class RegistrationsTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse('register'),
            data={
                'username': 'abdulbosit',
                'email': 'email@mail.com',
                'password1': 'some password',
                'password2': 'some password',
            }
        )
        user = Profile.objects.get(username='abdulbosit')
        self.assertEqual(user.email, 'email@mail.com')
        self.assertNotEqual(user.password, 'some password')
        self.assertTrue(user.check_password('some password'))


    def test_required_fields(self):
        response_without_password2 = self.client.post(
            reverse('register'),
            data={
                'username': 'abdulbosit',
                'email': 'email@mail.com',
                'password1': 'some password',
            }
        )
        response_without_password1 = self.client.post(
            reverse('register'),
            data={
                'username': 'abdulbosit',
                'email': 'email@mail.com',
                'password2': 'some password',
            }
        )
        response_without_username = self.client.post(
            reverse('register'),
            data={
                'email': 'email@mail.com',
                'password1': 'some password',
                'password2': 'some password',
            }
        )
        user_count = Profile.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response_without_username, 'form', 'username', 'This field is required.')
        self.assertFormError(response_without_password1, 'form', 'password1', 'This field is required.')
        self.assertFormError(response_without_password2, 'form', 'password2', 'This field is required.')

    def test_no_required_fields(self):
        self.client.post(
            reverse('register'),
            data={
                'username': 'abdulbosit',
                'password1': 'some password',
                'password2': 'some password',
            }
        )
        user_count = Profile.objects.count()
        self.assertEqual(user_count, 1)

    def test_invalid_email(self):
        invalid_email = self.client.post(
            reverse('register'),
            data={
                'username': 'abdulbosit',
                'email': 'invalid-email',
                'password1': 'some password',
                'password2': 'some password',
            }
        )
        user_count = Profile.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(invalid_email, 'form', 'email', 'Enter a valid email address.')

    def test_unique_username(self):
        self.client.post(
            reverse('register'),
            data={
                'username': 'abdulbosit',
                'password1': 'some password',
                'password2': 'some password',
            }
        )
        secondary_username = self.client.post(
            reverse('register'),
            data={
                'username': 'abdulbosit',
                'password1': 'some password',
                'password2': 'some password',
            }
        )
        user_count = Profile.objects.count()

        self.assertEqual(user_count, 1)
        self.assertFormError(secondary_username, 'form', 'username', 'A user with that username already exists.')


class LoginTestCase(TestCase):
    def test_successful_user(self):
        Profile.objects.create_user('abdulbosit', password='some password')

        self.client.post(
            reverse('login'),
            data={
                'username': 'abdulbosit',
                'password': 'some password'
            }
        )

        user = get_user(self.client)
        self.assertEqual(user.is_authenticated, True)

    def test_wrong_credentials(self):
        Profile.objects.create_user('abdulbosit', password='some password')

        self.client.post(
            reverse('login'),
            data={
                'username': 'wrong-username',
                'password': 'some password'
            }
        )

        user = get_user(self.client)
        self.assertEqual(user.is_authenticated, False)

        self.client.post(
            reverse('login'),
            data={
                'username': 'abdulbosit',
                'password': 'wrong password'
            }
        )

        user = get_user(self.client)
        self.assertEqual(user.is_authenticated, False)
