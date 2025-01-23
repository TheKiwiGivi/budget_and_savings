from database.config import config
import psycopg2

#function to check if connection to psql can be established
def test_connection():
    connection = None
    response = ''

    try:
        params = config()
        connection = psycopg2.connect(**params)

        curs = connection.cursor()
        curs.execute("SELECT version()")

        response = curs.fetchone()
        curs.close()
    except Exception as e:
        print("An error occurred in initialize.db: {0}".format(e))
    finally:
        if connection is not None:
            connection.close()

    return response[0]
