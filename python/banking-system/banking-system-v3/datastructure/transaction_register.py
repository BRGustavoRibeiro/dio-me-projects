#
# This is a class that represents a transaction. It can be a deposit, a withdrawal or a transfer.
#
# A transaction has the following data structure:
# - type: str - The transaction type. It can be "deposit", "withdrawal" or "transfer". It is private and cannot be changed.
# - value: float - The transaction value. It is private and cannot be changed.
# - date: str - The transaction date. It contains the date and time in the "DD/MM/YYYY HH:MM" format. It is private and cannot be changed.
# - source_account_number: str - The source account number. It is optional and doesn't exist if the type isn't "transfer". It is private and cannot be changed.
#
# It has the following methods:
# - get_type: returns the transaction type.
# - get_value: returns the transaction value.
# - get_date: returns the transaction date.
# - get_source_account_number: returns the source account number.

from datetime import datetime

class Transaction():
  def __init__(self, type, value, source_account_number = None):
    self.__type = type
    self.__value = value
    self.__date = datetime.now().strftime("%d/%m/%Y %H:%M")
    self.__source_account_number = source_account_number

  def get_type(self):
    return self.__type
  
  def get_formatted_type(self):
    if self.__type == "deposit":
      return "Depósito"
    elif self.__type == "withdrawal":
      return "Saque"
    elif self.__type == "transfer":
      return "Transferência"
    else:
      return self.__type

  def get_value(self):
    return self.__value
  
  def get_formatted_value(self):
    return "R$ " + format(self.__value, ".2f")

  def get_date(self):
    return self.__date

  def get_source_account_number(self):
    return self.__source_account_number