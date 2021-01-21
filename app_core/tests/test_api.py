from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAPI(TestBase):
    
    def  test_generate_role(self):
        with patch('requests.get')as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('generate_role'))
            self.assertIn(b'1',response.data)

    def test_generate_race(self):
         with patch('requests.get')as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('generate_race'))
            self.assertIn(b'1',response.data)

    def test_generate_weapon(self):
        with patch('requests.get')as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('generate_weapon'))
            self.assertIn(b'1',response.data)

    def test_generate_rating(self):

