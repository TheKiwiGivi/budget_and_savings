
from database.config import config
import psycopg2
import classes

params = config()

#function to check if connection to psql can be established
def test_connection():
    connection = None
    response = ''
    try:
        connection = psycopg2.connect(**params)

        curs = connection.cursor()
        curs.execute("SELECT version()")

        data = curs.fetchone()
        curs.close()

        if data:
            response = data[0]
    except Exception as e:
        print("An error occurred in test_connection: {0}".format(e))
    finally:
        if connection is not None:
            connection.close()

    return response




def get_account_details(account_id):
    return classes.Account