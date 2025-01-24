
from database.config import config
import psycopg2
import classes
import json
from types import SimpleNamespace

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


def handle_get_account_details(request):
    account_id = request.path_params.get('account_id')
    return get_account_details(account_id)

def get_account_details(account_id):
    return classes.Account

async def handle_make_account(request):
    return make_account(await request.body())


def parse_account_json(body):
    print(type(body))
    data = None
    try:
        data = json.loads(body, object_hook=lambda d: SimpleNamespace(**d))
        print(data)
        print(data.owner)
    except Exception as e:
        print("Something went wrong parsing json: {0}".format(e))
    return data
        

def make_account(body):
    #parse body
    body = parse_account_json(body)
    if not body:
        return JSONResponse({"response": "Parsing body failed"}, status_code=404)
    
    new_account_id = 0
    return JSONResponse({"response": f"{new_account_id} created."})

def handle_make_goal(request):
    account_id = request.path_params.get('account_id')
    goal = request.path_params.get('goal')

    #error handling
    if goal.lower() not in goals:
        return JSONResponse({"response": "Goal not found"}, status_code=404)
    
    return make_goal(account_id, goal)

def make_goal(account_id, goal):
    return JSONResponse({"response": "Goal created"})
