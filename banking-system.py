from os import system, name
import time

WITHDRAWAL_VALUE_LIMIT = float(500)
WITHDRAWAL_DAILY_LIMIT = 3
current_balance = float(0)
withdrawals_today = 0
statement_history = []

# 
# LIMPA O TERMINAL DEPENDENDO DO SISTEMA OPERACIONAL
#
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

#
# VERIFICA SE UM NÚMERO É FLOAT
#
def isfloat(num):
  try:
    float(num)
    return True
  except ValueError:
      return False

# 
# DEPÓSITO
#
def deposit():
  global current_balance
  global statement_history
  clear()
  print("".center(50, "-"))
  print(" BEI | Depósito ".center(50, "="))
  print("".center(50, "-"))

  while True:
    deposit_value = input("\n Quanto você deseja depositar? -> ")

    if str(deposit_value).strip() == "" or not isfloat(str(deposit_value)):
      print(" Valor inválido. Tente novamente.")
      continue

    deposit_value = float(deposit_value)

    if deposit_value <= 0.00 or deposit_value == "0":
      print(" Você precisa depositar pelo menos R$ 0.01. Tente novamente.")
      continue

    current_balance += deposit_value
    statement_history.append(["D", time.strftime("%d/%m/%Y %H:%M:%S"), deposit_value])

    print(" > Depósito realizado com sucesso. Seu novo saldo é de R$ {}.".format(format(current_balance, '.2f')))
    input("\n > Aperte [ENTER] para continuar...")
    return

# 
# SAQUE
#
def withdraw():
  global WITHDRAWAL_VALUE_LIMIT
  global WITHDRAWAL_DAILY_LIMIT
  global current_balance
  global withdrawals_today
  global statement_history
  clear()
  print("".center(50, "-"))
  print(" BEI | Saque ".center(50, "="))
  print("".center(50, "-"))
  print(" Você pode sacar até R$ {} por operação.".format(format(WITHDRAWAL_VALUE_LIMIT, '.2f')))
  print(" Você usou {0} dos seus {1} saques disponíveis ao dia.".format(withdrawals_today, WITHDRAWAL_DAILY_LIMIT))

  if withdrawals_today == WITHDRAWAL_DAILY_LIMIT:
    print("\n Você atingiu o limite de saques diários. Tente novamente amanhã.\n")   
    input("\n > Aperte [ENTER] para continuar...")
    return
  else:
    while True:
      withdrawal_value = input("\n Quanto você deseja sacar? -> ")

      if str(withdrawal_value).strip() == "" or not isfloat(str(withdrawal_value)):
        print(" Valor inválido. Tente novamente.")
        continue

      withdrawal_value = float(withdrawal_value)

      if withdrawal_value <= 0.00 or withdrawal_value == "0":
        print(" Você precisa sacar pelo menos R$ 0.01. Tente novamente.")
        continue

      if withdrawal_value > WITHDRAWAL_VALUE_LIMIT:
        print(" Você não pode sacar mais que R$ {} por operação. Tente novamente.".format(format(WITHDRAWAL_VALUE_LIMIT, '.2f')))
        continue

      if withdrawal_value > current_balance:
        print(" Saldo insuficiente. Seu saldo atual é de R$ {}.".format(format(current_balance, '.2f')))
        continue

      current_balance -= withdrawal_value
      withdrawals_today += 1
      statement_history.append(["S", time.strftime("%d/%m/%Y %H:%M:%S"), withdrawal_value])

      print(" > Saque realizado com sucesso. Seu novo saldo é de R$ {}.".format(format(current_balance, '.2f')))
      input("\n > Aperte [ENTER] para continuar...")
      return

# 
# EXTRATO
#
def statement():
  global WITHDRAWAL_VALUE_LIMIT
  global WITHDRAWAL_DAILY_LIMIT
  global current_balance
  global withdrawals_today
  global statement_history
  clear()
  print("".center(50, "-"))
  print(" BEI | Extrato ".center(50, "="))
  print("".center(50, "-"))
  print(" > SALDO ATUAL: R$ {}.".format(format(current_balance, '.2f')))
  print(" > LIMITE DE SAQUES POR DIA: {}".format(WITHDRAWAL_DAILY_LIMIT - withdrawals_today))
  print(" > LIMITE DIÁRIO DE SAQUE: R$ {}".format(WITHDRAWAL_VALUE_LIMIT))
  print("")
  print(" Operações desta conta ".center(50, "-"))
  print("")

  if len(statement_history) == 0:
    print(" Nenhuma operação realizada nesta conta.")
  else:
    for operation in statement_history:
      if operation[0] == "D":
        print(" [{}] | DEPÓSITO | + R$ {}".format(operation[1], format(operation[2], '.2f')))
      else:
        print(" [{}] | SAQUE    | - R$ {}".format(operation[1], format(operation[2], '.2f')))

  print("")
  print("".center(50, "-"))
  input("\n > Aperte [ENTER] para continuar...")

# 
# MENU - FUNÇÃO PRINCIPAL
#
def menu():
  global WITHDRAWAL_VALUE_LIMIT
  global WITHDRAWAL_DAILY_LIMIT
  global current_balance

  while True:
    clear()
    print("".center(50, "-"))
    print(" BEI | Banco Estrela Ionatário ".center(50, "="))
    print("".center(50, "-"))
    print(" | SEU SALDO ATUAL: R$ {}".format(format(current_balance, '.2f')))
    print(" > Escolha uma das opções abaixo")
    print(" [D] Depósito")
    print(" [S] Saque")
    print(" [E] Extrato")
    print(" [X] Sair")

    option = input(" Opção -> ")

    if option.upper() == "D":
      deposit()
    elif option.upper() == "S":
      withdraw()
    elif option.upper() == "E":
      statement()
    elif option.upper() == "X":
      clear()
      print(" Obrigado por usar o BEI. Volte sempre!")
      quit()
    else:
      print(" Opção inválida. Tente novamente.\n")
      time.sleep(1)

    continue
  
menu()