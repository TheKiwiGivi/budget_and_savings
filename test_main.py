import unittest

from main import *
from database.handle_db_calls import test_connection, retrieve_account_info


#class TestRetrieveAccountInfo(unittest.TestCase):
    #def test_retrieve_account_info(self):
        #account_info = retrieve_account_info(account_id="acc1")
        #self.assertEqual("Alice", account_info.owner)
        #TODO: more tests

    #def test_make_transaction(self):
        #self.assertEqual(15000.25, retrieve_account_info(account_id="acc1").balance)

        #make_transaction(account_id, )


        #TODO: more tests

class TestDatabaseConnection(unittest.TestCase):
    def test_test_connection(self):
        self.assertIn("postgres", test_connection().lower())