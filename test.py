# -*- coding: utf-8 -*-
import sys
import unittest
from mock import Mock

get_songs_mock = Mock()
get_songs_mock.return_value = "[1,2,3]"

import db
sys.modules['db'].get_songs = get_songs_mock

from app import app


class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.result = self.app.get('/')

    def test_status_should_be_ok(self):
        self.assertEqual(self.result.status_code, 200)

    def test_body_should_include_mocked_data(self):
        print(self.result.data);
        self.assertEqual(self.result.data, b'[1,2,3]')
