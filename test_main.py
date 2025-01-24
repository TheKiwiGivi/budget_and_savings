import unittest

from main import *
from database.handle_db_calls import *
import classes


class TestGetAndChangeAccountInfo(unittest.TestCase):
    def test_get_account_details(self):
        account_details = get_account_details(account_id="acc1")
        self.assertEqual("Alice", account_details.owner)
        #TODO: more tests

    def test_make_account(self):

        body = '''{"account_type": "Checking",
                "balance": 15000.25,
                "currency": "NOK",
                "owner": "Stian"
                }'''
        account_id = make_account(body)

        account_details = get_account_details(account_id=account_id)
        self.assertEqual("Stian", account_details.owner)
        

    #def test_make_goal(self):



class TestDatabaseConnection(unittest.TestCase):
    def test_test_connection(self):
        self.assertIn("postgres", test_connection().lower())
