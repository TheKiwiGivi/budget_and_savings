import unittest

from main import retrieve_client_info


class TestRetrieveClientInfo(unittest.TestCase):
    def test_retrieve_client_info(self):
        self.assertEqual(retrieve_client_info("test"), "test")