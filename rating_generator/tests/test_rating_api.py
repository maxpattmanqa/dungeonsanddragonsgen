import pytest
import unittest
from flask import url_for
from flask_testing import TestCase
from api import app
from unittest.mock import patch
import requests_mock


class TestBase(TestCase):
    def create_app(self):
      return app

class TestRatingApi(TestBase):
    def test_generate_rating_num(self):
        with patch('requests.post') as values:
            values.return_value.json = {"race_num":1,"role_num":1,"weapon_num":1}
            response = self.client.get(url_for('generate_rating_num'))

            print(response)
            self.assertIn(b'3',response.data)
    
