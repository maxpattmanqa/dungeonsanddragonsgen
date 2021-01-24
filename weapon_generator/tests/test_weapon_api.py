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


class TestAPI(TestBase):
    def test_get_weapon_id(self):
        with patch('requests.get') as g:
            g.return_value.text = "1"
            response = self.client.get(url_for('get_text'))
            self.assertTrue(int(response.data) <6 and int(response.data) >=0 )
            