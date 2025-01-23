
from database.config import config
import psycopg2

params = config()

#function to check if connection to psql can be established
def test_connection():
    connection = None
    response = ''
    try:
        connection = psycopg2.connect(**params)

        curs = connection.cursor()
        curs.execute("SELECT version()")

        response = curs.fetchone()
        curs.close()
    except Exception as e:
        print("An error occurred in test_connection: {0}".format(e))
    finally:
        if connection is not None:
            connection.close()

    return response[0]


def retrieve_account_info(account_id):
    return account_id