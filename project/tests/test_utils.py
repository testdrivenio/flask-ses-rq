# project/server/tests/test_utils.py


import time
import unittest

from base import BaseTestCase
from project.server.main.utils import encode_token, decode_token, generate_url
from project.server.models import User



class TestUtils(BaseTestCase):

    def test_verify_token(self):
        # Ensure encode and decode behave correctly.
        token = encode_token('dummy@email.com')
        email = decode_token(token)
        self.assertEqual(email, 'dummy@email.com')

    def test_verify_invalid_token(self):
        # Ensure encode and decode behave correctly when token is invalid.
        token = 'invalid'
        email = decode_token(token)
        self.assertEqual(email, False)

    def test_verify_expired_token(self):
        # Ensure encode and decode behave correctly when token has expired.
        token = encode_token('dummy@email.com')
        time.sleep(1)
        email = decode_token(token, 0)
        self.assertEqual(email, False)

    def test_token_is_unique(self):
        # Ensure tokens are unique.
        token1 = encode_token('dummy@email.com')
        token2 = encode_token('dummy@email2.com')
        self.assertNotEqual(token1, token2)

    def test_generate_url(self):
        # Ensure generate_url behaves as expected.
        token = encode_token('dummy@email.com')
        url = generate_url('main.home', token)
        url_token = url.split('=')[1]
        self.assertEqual(token, url_token)
        email = decode_token(url_token)
        self.assertEqual(email, 'dummy@email.com')


if __name__ == '__main__':
    unittest.main()
