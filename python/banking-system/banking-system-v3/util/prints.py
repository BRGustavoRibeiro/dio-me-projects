from datastructure.checking_account import CheckingAccount

def prints(text):
  print("  " + str(text))

def print_error(text):
  print("  └─ " + str(text) + "\n")

def system_operation_confirmation_output(type: str, checking_account: CheckingAccount):
  if type == "account_info":
    prints("Documento: " + str(checking_account.get_document()))
    print()
    prints("Agência: " + str(checking_account.get_branch()))
    prints("Número da conta: " + str(checking_account.get_account_number()))
    prints("Saldo: " + str(checking_account.get_formatted_balance()))
    print()
    prints("Valor máximo de saque por operação: R$ " + format(checking_account.get_max_withdrawal_value(), ".2f"))
    prints("Número máximo de saques por dia: " + str(checking_account.get_max_withdrawal_operations_per_day()))

  elif type == "only_limits":
    prints("Valor máximo de saque por operação: R$ " + format(checking_account.get_max_withdrawal_value(), ".2f"))
    prints("Número máximo de saques por dia: " + str(checking_account.get_max_withdrawal_operations_per_day()))
    
  elif type == "transaction":
    prints("Valor: " + str(checking_account.get_transactions()[-1].get_formatted_value()))
    prints("Tipo: " + str(checking_account.get_transactions()[-1].get_formatted_type()))
    prints("Data: " + str(checking_account.get_transactions()[-1].get_date()))
    print()
    prints("Saldo atual: " + str(checking_account.get_formatted_balance()))

  print()