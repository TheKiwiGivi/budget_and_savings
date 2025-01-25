import unittest

from main import *
from database.handle_requests import *
import classes
from database.handle_db_calls import *


class TestGetAndChangeAccountInfo(unittest.TestCase):
    def test_db_get_account_details(self):
        #requires at least one account
        _, found = db_get_account_details(account_id=0)
        self.assertTrue(found)

    def test_db_make_account(self):

        body = '''{"account_type": "Checking",
                "balance": 15000.25,
                "currency": "NOK",
                "owner": "Stian"
                }'''
        
        parsed_body = parse_account_json(body)
        account_id = db_make_account(parsed_body)

        account_details, found = db_get_account_details(account_id=account_id)

        self.assertTrue(found)
        self.assertTrue(isinstance(account_details, tuple))
        self.assertEqual("Stian", account_details[classes.Account.owner])
        self.assertEqual(15000.25, account_details[classes.Account.balance])
        self.assertEqual("NOK", account_details[classes.Account.currency])
        self.assertEqual("Checking", account_details[classes.Account.account_type])


        #check ID was newest
        account_details, found = db_get_account_details(account_id=account_id+1)

        self.assertFalse(found)
        self.assertFalse(isinstance(account_details, tuple))
        

    #def test_make_goal(self):



class TestDatabaseConnection(unittest.TestCase):
    def test_test_connection(self):
        self.assertIn("postgres", db_test_connection().lower())
