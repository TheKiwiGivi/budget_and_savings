from database.config import config
import psycopg2

params = config()

def initialize_tables():
    connection = None
    try:
        print("Attempting to create tables")
        connection = psycopg2.connect(**params)

        curs = connection.cursor()

        curs.execute("""CREATE TABLE IF NOT EXISTS accounts (
                     id int primary key, 
                     account_type text, 
                     balance float, 
                     currency text,
                     owner text);""")
        
        curs.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
                     id int primary key, 
                     date timestamp without time zone, 
                     description text, 
                     amount float,
                     currency text,
                     account_id int);""")
        
        {
}
        connection.commit()

        curs.close()
    except Exception as e:
        print("An error occurred in initialize_tables: {0}".format(e))
    finally:
        if connection is not None:
            connection.close()
