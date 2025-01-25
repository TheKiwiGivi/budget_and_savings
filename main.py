from database.initialize_db import *
from database.handle_requests import *
from test_main import *
import subprocess


from starlette.applications import Starlette
from starlette.routing import Route


def create_app():
    print("App started")

    #initialize db
    initialize_tables()

    #run tests
    subprocess.run(["python", "-m", "unittest"])

    #create server
    routes = [
        Route("/", endpoint=welcome),
        Route("/account/{account_id}/details", endpoint=handle_get_account_details, methods=["GET"]),
        Route("/account/{account_id}/make_goal/{goal}", endpoint=handle_make_goal, methods=["POST"]),
        Route("/make_transaction", endpoint=handle_make_transaction, methods=["POST"]),
        Route("/make_account", endpoint=handle_make_account, methods=["POST"]),
    ]

    app = Starlette(routes=routes)
    return app