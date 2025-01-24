class Account:
    id = None
    account_type = None
    balance = None
    currency = None
    owner = None

class Transaction:
    id = None
    date = None
    description = None
    amount = None
    currency = None
    account_id = None