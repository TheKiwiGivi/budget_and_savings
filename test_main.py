import unittest

from main import retrieve_client_info
from database.initialize_db import test_connection


class TestRetrieveClientInfo(unittest.TestCase):
    def test_retrieve_client_info(self):
        self.assertEqual(retrieve_client_info("test"), "test")

    def test_test_connection(self):
        self.assertTrue("postgres" in test_connection().lower())