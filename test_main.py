import unittest

from main import retrieve_client_info
from database.initialize_db import test_connection


class TestRetrieveClientInfo(unittest.TestCase):
    def test_retrieve_client_info(self):
        client_info = retrieve_client_info(client_id="acc1")
        self.assertEqual("Alice", client_info.owner)
        #TODO: more tests

class TestDatabaseConnection(unittest.TestCase):
    def test_test_connection(self):
        self.assertIn("postgres", test_connection().lower())