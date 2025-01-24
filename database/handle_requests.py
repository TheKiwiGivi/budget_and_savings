
from database.config import config
from database.handle_db_calls import *
import classes
import json
from types import SimpleNamespace

from starlette.responses import JSONResponse

goals = ["phone" ,"car", "house"]

params = config()


async def handle_get_account_details(request):
    account_id = request.path_params.get('account_id')
    return get_account_details(account_id)

def get_account_details(account_id):
    return classes.Account


def parse_account_json(body):
    data = None
    try:
        data = json.loads(body, object_hook=lambda d: SimpleNamespace(**d))
    except Exception as e:
        print("Something went wrong parsing json: {0}".format(e))
    return data
    

async def handle_make_account(request):
    return make_account(await request.body())

def body_is_valid(body):
    #check if all necessary attributes are in 'body'
    return True

def make_account(body):
    #parse body
    body = parse_account_json(body)
    if not body:
        return JSONResponse({"response": "Parsing body failed"}, status_code=404)
    elif not body_is_valid(body):
        return JSONResponse({"response": "Body missing attribute(s)"}, status_code=404)
    
    #create account
    account_id = db_make_account(body)
    
    return JSONResponse({"response": f"Account created for {body.owner} and was given account id: {account_id}."})

async def handle_make_goal(request):
    account_id = request.path_params.get('account_id')
    goal = request.path_params.get('goal')

    #error handling
    if goal.lower() not in goals:
        return JSONResponse({"response": "Goal not found"}, status_code=404)
    
    return make_goal(account_id, goal)

def make_goal(account_id, goal):
    return JSONResponse({"response": "Goal created"})
