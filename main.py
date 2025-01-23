from database.initialize_db import *
from database.handle_db_calls import *
import subprocess
from types import SimpleNamespace
import json

def read_json():
    try:
        with open("account_data/accounts.json") as file:
            data = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))
            print(data.accounts[0].owner)
    except Exception as e:
        print("Something went wrong parsing json: {0}".format(e))


def main():
    print("main started")
    subprocess.run(["python", "-m", "unittest"])

    #initialize db
    initialize_tables()
    

    print("main ended")



if __name__=="__main__":
    main()