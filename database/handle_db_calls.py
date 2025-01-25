
from database.config import config
import psycopg2
import classes

goals = ["phone" ,"car", "house"]

params = config()

#function to check if connection to psql can be established
def db_test_connection():
    connection = None
    response = ''
    try:
        connection = psycopg2.connect(**params)

        curs = connection.cursor()
        curs.execute("SELECT version()")

        data = curs.fetchone()
        curs.close()

        if data and data[0] != None:
            response = data[0]
    except Exception as e:
        print("An error occurred in test_connection: {0}".format(e))
    finally:
        if connection is not None:
            connection.close()

    return response

def db_get_account_details(account_id):
    connection = None
    found = False
    account_details = classes.Account

    try:
        connection = psycopg2.connect(**params)
        curs = connection.cursor()

        #get highest account id
        curs.execute("SELECT id, owner, balance, currency, account_type FROM accounts WHERE id = %s" % account_id)
        data = curs.fetchone()

        #update new account id
        if data:
            account_details = data
            found = True

        connection.commit()
        curs.close()

    except Exception as e:
        print("An error occurred in db_get_account_details: {0}".format(e))
    finally:
        if connection is not None:
            connection.close()

    return account_details, found

def db_make_account(body):
    connection = None
    new_account_id = 0
    try:
        connection = psycopg2.connect(**params)
        curs = connection.cursor()

        #get highest account id
        curs.execute("SELECT max(id) from accounts")
        data = curs.fetchone()

        #update new account id
        if data and data[0] != None:
            new_account_id = data[0] + 1

        #create account
        curs.execute("INSERT INTO accounts (id, owner, balance, currency, account_type) VALUES (%s, %s, %s, %s, %s)", 
                     (new_account_id, body.owner, body.balance, body.currency, body.account_type))
        
        connection.commit()
        curs.close()

    except Exception as e:
        print("An error occurred in db_make_account: {0}".format(e))
    finally:
        if connection is not None:
            connection.close()

    return new_account_id
