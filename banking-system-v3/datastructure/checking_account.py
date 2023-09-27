from datetime import date

#
# This is a class that represents a checking account.
#
# A checking account belongs to an user, which can have multiple checking accounts.
# The relation between a checking account and a user is done by the CPF.
#
# A checking account has the following data structure:
# - branch: int - The branch number. It's a 4-digit sequential number stored within a str. It starts with 0001. It is private and cannot be changed.
# - account_number: int - The account number. It's a 4-digit sequential number stored within a str. It starts with 0001 for each branch. It is private and cannot be changed. It is unique for each branch.
# - document: str - This is the CPF or the CNPJ of the user that owns the account. It is private and cannot be changed.
# - balance: float - The user's balance. It starts with 0. Balance is a private property and can't be changed except by the method register_transaction.
# - transactions: list - A list of transactions. Each transaction is an instance of transaction_register. It starts empty. It is private and cannot be changed, except by the method register_transaction.
# - max_withdrawal_value: float - The maximum value that can be withdrawn from the account. It starts with 1000. It is private and cannot be changed, except by the method change_max_withdrawal_value.
# - max_withdrawal_operations_per_day: int - The maximum number of withdrawals that can be made in a day. It starts with 3. It is private and cannot be changed, except by the method change_max_withdrawal_operations_per_day.
#
# It has the following methods:
# - change_max_withdrawal_value: changes the maximum value that can be withdrawn from the account.
# - change_max_withdrawal_operations_per_day: changes the maximum number of withdrawals that can be made in a day.
# - register_transaction: registers a transaction. It can be a deposit or a withdrawal. It changes the balance and the number of withdrawal operations made today.
# - get_branch: returns the branch number.
# - get_account_number: returns the account number.
# - get_document: returns the CPF or the CNPJ of the user that owns the account.
# - get_balance: returns the balance.
# - get_formatted_balance: returns the balance formatted as a currency.
# - get_transactions: returns the list of transactions.
# - get_max_withdrawal_value: returns the maximum value that can be withdrawn from the account.
# - get_max_withdrawal_operations_per_day: returns the maximum number of withdrawals that can be made in a day.
# - get_withdrawal_operations_made_today: it calculates the number of withdrawal operations made today according to the current date and the transaction history and returns it.

class CheckingAccount:
  def __init__(self, branch, account_number, document, balance, transactions, max_withdrawal_value, max_withdrawal_operations_per_day):
    self.__branch = branch
    self.__account_number = account_number
    self.__document = document
    self.__balance = balance
    self.__transactions = transactions
    self.__max_withdrawal_value = max_withdrawal_value
    self.__max_withdrawal_operations_per_day = max_withdrawal_operations_per_day

  def change_max_withdrawal_value(self, new_max_withdrawal_value):
    self.__max_withdrawal_value = new_max_withdrawal_value

  def change_max_withdrawal_operations_per_day(self, new_max_withdrawal_operations_per_day):
    self.__max_withdrawal_operations_per_day = new_max_withdrawal_operations_per_day

  def register_transaction(self, transaction):
    if transaction.get_type() == "deposit":
      self.__balance += transaction.get_value()
    elif transaction.get_type() == "withdrawal":
      self.__balance -= transaction.get_value()
    
    self.__transactions.append(transaction)

  def get_branch(self):
    return self.__branch

  def get_account_number(self):
    return self.__account_number

  def get_document(self):
    return self.__document

  def get_balance(self):
    return self.__balance

  def get_formatted_balance(self):
    return "R$ " + format(self.__balance, ".2f")

  def get_transactions(self):
    return self.__transactions

  def get_max_withdrawal_value(self):
    return self.__max_withdrawal_value

  def get_max_withdrawal_operations_per_day(self):
    return self.__max_withdrawal_operations_per_day

  def get_withdrawal_operations_made_today(self):
    today = date.today()
    withdrawal_operations_made_today = 0

    for transaction in self.__transactions:
      if transaction.get_type() == "withdrawal" and transaction.get_date() == today:
        withdrawal_operations_made_today += 1

    return withdrawal_operations_made_today

  # this is a create checking account function (it will probably be a class method) that will receive branch, document, max_withdrawal_value and max_withdrawal_operations_per_day.
  # this function will also receive a database: list[CheckingAccount] that will be used to do the following:
  # the function will need to return a CheckingAccount object, which will have an account_number that will start at 0001 and will be sequential.
  # the account_number will be unique for each branch. it cannot be repeated. if the function tries to create an account with an account_number that already exists, it will return None.
  # the account number is a string, not an integer, and it mandatory needs to have 0 on the left if it is a number smaller than 1000.
  @classmethod
  def create_checking_account(cls, branch: str, document: str, max_withdrawal_value: float, max_withdrawal_operations_per_day: int, database: list):
    account_number = str(len(database) + 1).rjust(4, "0")

    for checking_account in database:
      if checking_account.get_branch() == branch and checking_account.get_account_number() == account_number:
        return None

    return cls(branch, account_number, document, 0, [], max_withdrawal_value, max_withdrawal_operations_per_day)