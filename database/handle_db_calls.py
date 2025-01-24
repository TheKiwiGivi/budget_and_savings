
from database.config import config
import psycopg2
import classes

from starlette.responses import JSONResponse, HTMLResponse

goals = ["phone" ,"car", "house"]

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


def get_account_details(request):
    return classes.Account

def get_account_transactions(request):
    transactions = list()
    transactions.append(classes.Transaction)
    return transactions

def make_account(request):
    new_account_id = 0
    return JSONResponse({"response": f"{new_account_id} created."})

def make_goal(request):
    account_id = request.path_params.get('account_id')
    goal = request.path_params.get('goal')

    #error handling
    #TODO: check account id
    if goal.lower() not in goals:
        return JSONResponse({"response": "Goal not found"}, status_code=404)
    
    return JSONResponse({"response": "Goal created!"})