# project/server/tests/test_main.py


import unittest

from base import BaseTestCase
from project.server import db
from project.server.models import User



class TestMainBlueprint(BaseTestCase):

    def test_index(self):
        # Ensure Flask is setup.
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flask + Redis Queue + Amazon SES', response.data)
        self.assertIn(b'Registered Users', response.data)

    def test_user_registration(self):
        # Ensure registration behaves correctly.
        with self.client:
            response = self.client.post(
                '/',
                data=dict(email="test@tester.com"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Thank you for registering.', response.data)
            self.assertIn(b'<td>1</td>', response.data)
            self.assertIn(b'<td>test@tester.com</td>', response.data)
            self.assertIn(b'<td>False</td>', response.data)
            self.assertNotIn(
                b'Sorry. That email already exists.', response.data)

    def test_user_registration_invalid_email(self):
        # Ensure registration behaves correctly with an invalid email.
        with self.client:
            response = self.client.post(
                '/',
                data=dict(email="notvalid"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                b'<p class="help-block">Invalid email address.</p>',
                response.data)
            self.assertNotIn(b'Thank you for registering.', response.data)
            self.assertNotIn(
                b'Sorry. That email already exists.', response.data)
            self.assertNotIn(b'<td>1</td>', response.data)
            self.assertNotIn(b'<td>notvalid</td>', response.data)
            self.assertNotIn(b'<td>False</td>', response.data)

    def test_user_registration_duplicate_email(self):
        # Ensure registration behaves correctly with a duplicate email.
        db.session.add(User(email="test@test.com"))
        db.session.commit()
        with self.client:
            response = self.client.post(
                '/',
                data=dict(email="test@test.com"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                b'Sorry. That email already exists.', response.data)
            self.assertNotIn(b'<td>2</td>', response.data)
            self.assertNotIn(b'Thank you for registering.', response.data)

if __name__ == '__main__':
    unittest.main()
