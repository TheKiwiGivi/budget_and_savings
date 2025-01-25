
from database.config import config
from database.handle_db_calls import *
from classes import *
import json
from types import SimpleNamespace

from starlette.responses import JSONResponse

goals = ["phone" ,"car", "house"]

params = config()

async def welcome(_):
    return JSONResponse({"message": "Welcome to the Budget and Savings app!"})

def is_valid_account_id(account_id):
    return True


async def handle_get_account_details(request):
    account_id = request.path_params.get('account_id')
    return get_account_details(account_id)

def format_account_details(account_details):
    return {"id": account_details[Account.id], 
            "owner": account_details[Account.owner],
            "balance": account_details[Account.balance],
            "currency": account_details[Account.currency],
            "account_type": account_details[Account.account_type]
            }

def get_account_details(account_id):
    account_found = False
    if is_valid_account_id(account_id):
        account_details, account_found = db_get_account_details(account_id)

    if not account_found:
        return JSONResponse({"message": "Account not found"}, status_code=404)
    

    return JSONResponse(format_account_details(account_details))


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
    #TODO: check if all necessary attributes are in 'body'
    return True

def make_account(body):
    #parse body
    body = parse_account_json(body)
    if not body:
        return JSONResponse({"message": "Parsing body failed"}, status_code=404)
    elif not body_is_valid(body):
        return JSONResponse({"message": "Body missing attribute(s)"}, status_code=404)
    
    #create account
    account_id = db_make_account(body)
    account_details, _ = db_get_account_details(account_id)
    
    return JSONResponse(format_account_details(account_details), status_code=201)

async def handle_make_goal(request):
    account_id = request.path_params.get('account_id')
    goal = request.path_params.get('goal')

    #error handling
    if goal.lower() not in goals:
        return JSONResponse({"message": "Goal not found"}, status_code=404)
    
    return make_goal(account_id, goal)

def make_goal(account_id, goal):
    return JSONResponse({"message": "Goal created"})


async def handle_make_transaction(request):
    return make_transaction(await request.body())


def make_transaction(body):
    #parse body
    body = parse_account_json(body)
    if not body:
        return JSONResponse({"message": "Parsing body failed"}, status_code=404)
    elif not body_is_valid(body):
        return JSONResponse({"message": "Body missing attribute(s)"}, status_code=404)
    
    #create account
    transaction_id = db_make_transaction(body)
    
    return JSONResponse({"transaction id": transaction_id})