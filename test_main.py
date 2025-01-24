import unittest

from main import *
from database.handle_db_calls import *
import classes


class TestRetrieveAccountInfo(unittest.TestCase):
    def test_get_account_details(self):
        account_details = get_account_details(account_id="acc1")
        self.assertEqual("Alice", account_details.owner)
        #TODO: more tests

    def test_get_account_transactions(self):
        transactions_details = get_account_transactions(account_id="acc1")
        self.assertEqual(-75.5, transactions_details[0].amount)

        #make_transaction(account_id, )
    #def test_get_account_recommendations(self):



        #TODO: more tests

class TestDatabaseConnection(unittest.TestCase):
    def test_test_connection(self):
        self.assertIn("postgres", test_connection().lower())
