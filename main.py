from database.initialize_db import *
import subprocess
from types import SimpleNamespace
import json


def main():
    print("main started")
    subprocess.run(["python", "-m", "unittest"])


    with open("client_data/accounts.json") as file:
        data = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))
        print(data.accounts[0].owner)
    print("main ended")


def retrieve_client_info(client_id):
    return client_id


if __name__=="__main__":
    main()