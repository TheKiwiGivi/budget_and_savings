from database.initialize_db import *
from database.handle_db_calls import *
import subprocess
from types import SimpleNamespace
import json
import uvicorn
import asyncio

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


def read_json():
    try:
        with open("account_data/accounts.json") as file:
            data = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))
            print(data.accounts[0].owner)
    except Exception as e:
        print("Something went wrong parsing json: {0}".format(e))


async def welcome(_):
    return JSONResponse({"message": "Welcome to the Budget and Savings app!"})

#async def main():
print("App started")

    #run unit tests
    #await subprocess.run(["python", "-m", "unittest"])

#initialize db
initialize_tables()

#create server
routes = [
    Route("/", endpoint=welcome),
    Route("/account/{account_id}/details", endpoint=handle_get_account_details, methods=["GET"]),
    Route("/account/{account_id}/make_goal/{goal}", endpoint=handle_make_goal, methods=["POST"]),
    Route("/make_transaction/{account_id}", endpoint=welcome, methods=["POST"]),
    Route("/make_account", endpoint=handle_make_account, methods=["POST"]),
]

app = Starlette(routes=routes)


    #await uvicorn.run(app, host='0.0.0.0', port=8501)


#if __name__=="__main__":
    #asyncio.run(main())