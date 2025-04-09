from os import system, name
import time

#
# Constantes
#
BANK_BRANCH_NUMBER: str = "0001"

#
# Classes
#
class User:
  def __init__(self, cpf: str, name: str, birthdate: str, address: str, address_number: str, address_neighborhood: str, address_city: str, address_state: str):
    self.cpf = cpf
    self.name = name
    self.birthdate = birthdate
    self.address = address
    self.address_number = address_number
    self.address_neighborhood = address_neighborhood
    self.address_city = address_city
    self.address_state = address_state

class CheckingAccount:
  def __init__(self, branch: str, account_number: str, cpf: str, balance: float, transactions: list, max_withdrawals_per_day: int, max_withdrawal_value: float, withdrawals_today: int = 0):
    self.branch = branch
    self.account_number = account_number
    self.cpf = cpf
    self.balance = balance
    self.transactions = transactions
    self.max_withdrawals_per_day = max_withdrawals_per_day
    self.max_withdrawal_value = max_withdrawal_value
    self.withdrawals_today = withdrawals_today

#
# BANCO DE DADOS ???
#
# Todos sabem que o uso de variáveis globais (não constantes) são uma má prática de programação.
# No entanto, como não possuo um banco de dados a fim de criar um sistema de cadastro de usuários
# e conta-corrente, optei por utilizar variáveis globais para simular o comportamento de um banco
# de dados, armazenando os dados por aqui e que serão obtidos por variável global.
#
# Se eu estivesse optado por fazê-lo por argumentos, o resultado seria um código mais verboso e
# menos legível, pois teria que passar os dados de uma função para outra, e outra, e outra...
# 
# Por favor, não me julgue. :(

#users: list = [
#  User("11111111111", "JOÃO DA SILVA", "01/01/1990", "RUA DOS BOBOS", "0", "CENTRO", "SÃO PAULO", "SP")
#]
users: list = []

#checking_accounts: list = [
#  CheckingAccount("0001", "0001", "11111111111", 0.00, [], 3, 500.00, 0)
#]
checking_accounts: list = []

#
# Utilitários
#
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def isfloat(num):
  try:
    float(num)
    return True
  except ValueError:
    return False
  
def prints(text):
  print("  " + text)

#
# Funções para abstração e padronização da consistência da experiência do usuário
#
def quit_program():
  clear()
  print("Obrigado por ser cliente do Banco IT. Volte sempre!\n")
  quit()

def print_heading(text):
  return_text = "  " + text

  print(return_text)
  print("  ─".ljust(len(return_text), "─"))

def display_header(title):
  clear()
  print("╔══════════╦═══════════════════════════════════════════════════════╗")
  print("║ Banco IT ║ {} ".format(title).ljust(67, " ") + "║")
  print("╚══════════╩═══════════════════════════════════════════════════════╝\n")

def display_menu(question, menu_items):
  print_heading(question)

  for item in menu_items:
    print("  " + str(item[0]).rjust(4, " ") + "  » " + item[1])

def menu_input(menu_items, option_text = "Digite a opção desejada"):
  while True:
    return_text = "  " + option_text + " »"
    user_input = input("\n" + return_text + " ").strip().upper()
  
    if user_input == "":
      prints("Opção inválida. Tente novamente.")
      continue
    
    if user_input not in [item[0] for item in menu_items]:
      prints("Opção inválida. Tente novamente.")
      continue
    
    return user_input

def validateable_input(text):
  while True:
    return_text = "  " + text + " »"
    user_input = input(return_text + " ").strip().upper()
  
    if user_input == "":
      prints("Por favor, insira um valor válido. Tente novamente.\n")
      continue
    
    return user_input

def validateable_number_input(text):
  while True:
    return_text = "  " + text + " »"
    user_input = input(return_text + " ").strip().upper()
  
    if user_input == "":
      prints("Por favor, insira um número válido. Tente novamente.\n")
      continue
    
    if not isfloat(user_input):
      prints("Por favor, insira um número válido. Tente novamente.\n")
      continue

    if int(user_input) < 0:
      prints("Por favor, insira um número válido. Tente novamente.\n")
      continue

    return user_input

def validateable_float_input(text):
  while True:
    return_text = "  " + text + " »"
    user_input = input(return_text + " ").strip().upper()
  
    if user_input == "":
      prints("Por favor, insira um número válido. Tente novamente.\n")
      continue
    
    if not isfloat(user_input):
      prints("Por favor, insira um número válido. Tente novamente.\n")
      continue

    if float(user_input) < 0.00:
      prints("Por favor, insira um número válido. Tente novamente.\n")
      continue

    return user_input

def validateable_date_input(text):
  while True:
    return_text = "  " + text + " »"
    user_input = input(return_text + " ").strip().upper()
  
    if user_input == "":
      prints("Por favor, insira uma data válida. Tente novamente.\n")
      continue

    if len(user_input) != 10:
      prints("Por favor, insira uma data válida. Tente novamente.\n")
      continue

    if user_input[2] != "/" or user_input[5] != "/":
      prints("Por favor, insira uma data válida. Tente novamente.\n")
      continue

    if user_input[0:2].isdigit() == False or user_input[3:5].isdigit() == False or user_input[6:10].isdigit() == False:
      prints("Por favor, insira uma data válida. Tente novamente.\n")
      continue

    if int(user_input[0:2]) > 31 or int(user_input[0:2]) < 1:
      prints("Por favor, insira uma data válida. Tente novamente.\n")
      continue

    if int(user_input[3:5]) > 12 or int(user_input[3:5]) < 1:
      prints("Por favor, insira uma data válida. Tente novamente.\n")
      continue

    if int(user_input[6:10]) > 2021 or int(user_input[6:10]) < 1900:
      prints("Por favor, insira uma data válida. Tente novamente.\n")
      continue

    return user_input

def validateable_brazilian_states_input(text):
  while True:
    return_text = "  " + text + " »"
    user_input = input(return_text + " ").strip().upper()
  
    if user_input == "":
      prints("Por favor, insira um estado válido. Tente novamente.\n")
      continue
    
    if user_input not in ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RR", "RO", "RJ", "RN", "RS", "SC", "SP", "SE", "TO"]:
      prints("Por favor, insira um estado válido. Tente novamente.\n")
      continue

    return user_input

def skip():
  input("\n  » Aperte [ENTER] para continuar...")

#
# Funções para filtragem e validação e dados, reutilizáveis em algumas áreas do sistema
#
def validate_cpf(cpf):
  if len(cpf) != 11 or not cpf.isdigit():
    return False

  if cpf == "00000000000" or cpf == "11111111111" or cpf == "22222222222" or cpf == "33333333333" or cpf == "44444444444" or cpf == "55555555555" or cpf == "66666666666" or cpf == "77777777777" or cpf == "88888888888" or cpf == "99999999999":
    return False

  sum = 0
  weight = 10

  for n in range(9):
    sum += int(cpf[n]) * weight
    weight -= 1

  verifying_digit = 11 - sum % 11

  if verifying_digit > 9:
    first_digit = 0
  else:
    first_digit = verifying_digit

  sum = 0
  weight = 11

  for n in range(10):
    sum += int(cpf[n]) * weight
    weight -= 1

  verifying_digit = 11 - sum % 11

  if verifying_digit > 9:
    second_digit = 0
  else:
    second_digit = verifying_digit

  if cpf[-2:] == "%s%s" % (first_digit, second_digit):
    return True
  else:
    return False

def validate_account_number(account_number):
  if account_number.isdigit() and len(account_number) == 4:
    return True
  else:
    return False

#
# Páginas do sistema
#
def no_user_account_found(user_cpf):
  display_header("Criar nova conta de usuário")

  menu_items = [
    ["1", "Criar uma conta"],
    ["2", "Voltar"]
  ]

  display_menu("Não existe uma conta de usuário encontrada no seu CPF.", menu_items)
  option = menu_input(menu_items)

  if option == "1":
    create_user_account(user_cpf)
  elif option == "2":
    initial_auth()
  else:
    quit_program()

def create_user_account(user_cpf):
  global users

  display_header("Criar nova conta de usuário")

  print_heading("Insira seus dados abaixo.")

  user_name = validateable_input("Nome completo ".ljust(31, "·"))
  user_birthdate = validateable_date_input("Data de nascimento (dd/mm/aaaa)".ljust(31, " "))
  user_address = validateable_input("Endereço ".ljust(31, "·"))
  user_address_number = validateable_number_input("Número ".ljust(31, "·"))
  user_address_neighborhood = validateable_input("Bairro ".ljust(31, "·"))
  user_address_city = validateable_input("Cidade ".ljust(31, "·"))
  user_address_state = validateable_brazilian_states_input("Estado (sigla) ".ljust(31, "·"))

  users.append(User(user_cpf, user_name, user_birthdate, user_address, user_address_number, user_address_neighborhood, user_address_city, user_address_state))

  create_checking_account(user_cpf)

def view_user_account_info(user_cpf):
  global users

  display_header("Editar informações pessoais")

  user_info = [user for user in users if user.cpf == user_cpf][0]

  print_heading(user_info.name)

  print("""  CPF: {0}
  Data de nascimento: {1}
  Endereço: {2}, {3} - {4} - {5}\n""".format(user_info.cpf, user_info.birthdate, user_info.address, user_info.address_number, user_info.address_neighborhood, user_info.address_city, user_info.address_state))

  menu_items = [
    ["1", "Editar"],
    ["2", "Voltar"]
  ]
  display_menu("O que você deseja fazer?", menu_items)
  
  while True:
    option = menu_input(menu_items)

    if option == "1":
      prints("Esta opção ainda não foi implementada.")
      continue
    elif option == "2":
      user_account_dashboard(user_cpf)
    else:
      quit_program()

def user_account_dashboard(user_cpf):
  global users

  display_header("Olá, {}!".format([user.name for user in users if user.cpf == user_cpf][0]))

  menu_items = [
    ["1", "Minhas contas-correntes"],
    ["2", "Abrir nova conta"],
    ["3", "Minhas informações pessoais\n"],
    ["4", "Encerrar sessão"],
    ["0", "Fechar o programa"]
  ]

  display_menu("O que você deseja fazer?", menu_items)
  option = menu_input(menu_items)

  if option == "1":
    select_checking_account(user_cpf)
  elif option == "2":
    create_checking_account(user_cpf)
  elif option == "3":
    view_user_account_info(user_cpf)
  elif option == "4":
    initial_auth()
  elif option == "0":
    quit_program()

def display_checking_account_info(checking_account, type = "balance"):
  info_receipt = """  Agência: {0}
  Conta-corrente: {1}""".format(checking_account.branch, checking_account.account_number)

  if type == "balance":
    info_receipt += """\n
  SALDO ATUAL: R$ {0}""".format(format(float(checking_account.balance), '.2f'))
    
  if type == "limits":
    info_receipt += """\n
  Limite de saques diários: {0}
  Valor máximo por saque: R$ {1}""".format(checking_account.max_withdrawals_per_day, format(float(checking_account.max_withdrawal_value), '.2f'))

  return info_receipt

def deposit(checking_account):
  global checking_accounts

  display_header("Depósito")

  print_heading("Agência: {0} | Conta-corrente: {1} | Saldo: R$ {2}".format(checking_account.branch, checking_account.account_number, format(float(checking_account.balance), '.2f')))

  deposit_value = validateable_float_input("Qual o valor do depósito?".ljust(31, "·"))

  if not float(deposit_value) == 0:
    checking_account.balance += float(deposit_value)
    checking_account.transactions.append(["D", time.strftime("%d/%m/%Y %H:%M"), float(deposit_value)])

  clear()
  display_header("Depósito » Finalização")
  print_heading("Depósito realizado com sucesso!")

  print(display_checking_account_info(checking_account, "balance"))
  skip()

  checking_account_menu(checking_account)

def withdraw(checking_account):
  global checking_accounts

  display_header("Saque")

  print_heading("Agência: {0} | Conta-corrente: {1} | Saldo: R$ {2}".format(checking_account.branch, checking_account.account_number, format(float(checking_account.balance), '.2f')))

  print("  Você pode sacar até R$ {} por operação.".format(format(float(checking_account.max_withdrawal_value), '.2f')))
  print("  Você usou {0} dos seus {1} saques disponíveis ao dia.\n".format(checking_account.withdrawals_today, checking_account.max_withdrawals_per_day))

  if checking_account.withdrawals_today == checking_account.max_withdrawals_per_day:
    prints("Você atingiu o limite de saques diários. Tente novamente amanhã.")   
    skip()
    checking_account_menu(checking_account)
  else:
    while True:
      withdrawal_value = validateable_float_input("Quanto você deseja sacar? ".ljust(31, "·"))

      if float(withdrawal_value) < 0.00:
        prints("Você precisa sacar pelo menos R$ 0.01. Tente novamente.\n")
        continue

      if float(withdrawal_value) > float(checking_account.max_withdrawal_value):
        prints("Você não pode sacar mais que R$ {} por operação. Tente novamente.\n".format(format(float(checking_account.max_withdrawal_value), '.2f')))
        continue

      if float(withdrawal_value) > float(checking_account.balance):
        prints("Saldo insuficiente. Seu saldo atual é de R$ {}.\n".format(format(float(checking_account.balance), '.2f')))
        continue

      if not float(withdrawal_value) == 0:
        checking_account.balance -= float(withdrawal_value)
        checking_account.transactions.append(["S", time.strftime("%d/%m/%Y %H:%M"), float(withdrawal_value)])
        checking_account.withdrawals_today += 1

      clear()
      display_header("Saque » Finalização")
      print_heading("Saque realizado com sucesso!")

      print(display_checking_account_info(checking_account, "balance"))
      skip()

      checking_account_menu(checking_account)
            
def statement(checking_account):
  global checking_accounts

  display_header("Extrato bancário")

  print_heading("Agência: {0} | Conta-corrente: {1}".format(checking_account.branch, checking_account.account_number))

  if len(checking_account.transactions) == 0:
    prints("Nenhuma transação encontrada.")
    skip()
    checking_account_menu(checking_account)
  else:
    print("  ─────────┬──────────────────┬───────────────────")
    print("  Tipo     │ Data e hora      │ Valor             ")
    print("  ─────────┴──────────────────┴───────────────────")

    for transaction in checking_account.transactions:
      if transaction[0] == "D":
        print("  Depósito │ {0} │ R$ {1}".format(transaction[1], format(float(transaction[2]), '.2f')))
      elif transaction[0] == "S":
        print("  Saque    │ {0} │ R$ {1}".format(transaction[1], format(float(transaction[2]), '.2f')))

    print("  ────────────────────────────────────────────────")
    print("  SALDO CORRENTE: R$ {0}".format(format(float(checking_account.balance), '.2f')))
    print("  ────────────────────────────────────────────────")

    skip()
    checking_account_menu(checking_account)

def update_account_limits(checking_account):
  global checking_accounts

  display_header("Alterar limites")

  print_heading("Agência: {0} | Conta-corrente: {1} | Saldo: R$ {2}".format(checking_account.branch, checking_account.account_number, format(float(checking_account.balance), '.2f')))

  print("  Você pode sacar até R$ {} por operação.".format(format(float(checking_account.max_withdrawal_value), '.2f')))
  print("  Você usou {0} dos seus {1} saques disponíveis ao dia.\n".format(checking_account.withdrawals_today, checking_account.max_withdrawals_per_day))

  menu_items = [
    ["1", "Alterar limite de saque por operação"],
    ["2", "Alterar limite de saques diários"],
    ["3", "Voltar"]
  ]

  display_menu("O que você deseja fazer?", menu_items)
  option = menu_input(menu_items)

  if option == "1":
    update_withdrawal_value_limit(checking_account)
  elif option == "2":
    update_withdrawals_per_day_limit(checking_account)
  elif option == "3":
    checking_account_menu(checking_account)
  else:
    quit_program()

def update_withdrawal_value_limit(checking_account):
  global checking_accounts

  display_header("Alterar limite de saque por operação")

  new_limit = validateable_float_input("Qual o novo limite de saque por operação?".ljust(31, "·"))

  checking_account.max_withdrawal_value = format(float(new_limit), '.2f')

  clear()
  display_header("Alterar limite de saque por operação » Finalização")
  print_heading("Limite de saque por operação alterado com sucesso!")

  print(display_checking_account_info(checking_account, "limits"))
  skip()

  update_account_limits(checking_account)

def update_withdrawals_per_day_limit(checking_account):
  global checking_accounts

  display_header("Alterar limite de saques diários")

  new_limit = validateable_number_input("Qual o novo limite de saques diários?".ljust(31, "·"))

  checking_account.max_withdrawals_per_day = int(new_limit)

  clear()
  display_header("Alterar limite de saques diários » Finalização")
  print_heading("Limite de saques diários alterado com sucesso!")

  print(display_checking_account_info(checking_account, "limits"))
  skip()

  update_account_limits(checking_account)

def checking_account_menu(checking_account):
  global checking_accounts

  display_header("Olá, {}!".format([user.name for user in users if user.cpf == checking_account.cpf][0]))

  print_heading("Agência: {0} | Conta-corrente: {1} | Saldo: R$ {2}".format(checking_account.branch, checking_account.account_number, format(float(checking_account.balance), '.2f')))

  menu_items = [
    ["1", "Depósito"],
    ["2", "Saque"],
    ["3", "Extrato\n"],
    ["4", "Alterar limites"],
    ["5", "Sair desta conta"],
    ["0", "Fechar o programa"]
  ]

  display_menu("O que você deseja fazer?", menu_items)
  option = menu_input(menu_items)

  if option == "1":
    deposit(checking_account)
  elif option == "2":
    withdraw(checking_account)
  elif option == "3":
    statement(checking_account)
  elif option == "4":
    update_account_limits(checking_account)
  elif option == "5":
    select_checking_account(checking_account.cpf)
  elif option == "0":
    quit_program()

def create_checking_account(user_cpf):
  global checking_accounts

  display_header("Abrir nova conta-corrente » Passo 1")

  print_heading("Qual será o máximo de saques autorizados ao dia?")  
  
  while True:
    option = input("  Insira a quantidade » ").strip()

    if option.isdigit() and int(option) > 0:
      max_withdrawals_per_day = int(option)
      break
    else:
      prints("Por favor, insira um valor válido. Tente novamente.\n")
      continue

  clear()
  display_header("Abrir nova conta-corrente » Passo 2")

  print_heading("Qual será o valor máximo por saque?")

  while True:
    option = input("  Insira o valor » R$ ").strip()

    if isfloat(option) and float(option) > 0:
      max_withdrawal_value = format(float(option), '.2f')
      break
    else:
      prints("Por favor, insira um valor válido. Tente novamente.\n")
      continue

  checking_account_number = ""

  if len(checking_accounts) == 0:
    checking_account_number = "0001"
  else:
    checking_account_number = str(int(checking_accounts[-1].account_number) + 1).zfill(4)

  checking_accounts.append(CheckingAccount(BANK_BRANCH_NUMBER, checking_account_number, user_cpf, 0.00, [], max_withdrawals_per_day, format(float(max_withdrawal_value), '.2f')))

  clear()
  display_header("Abrir nova conta-corrente » Finalização")
  print_heading("Conta aberta com sucesso!")

  print(display_checking_account_info([account for account in checking_accounts if account.account_number == checking_account_number][0], "limits"))
  skip()

  select_checking_account(user_cpf)

def select_checking_account(user_cpf):
  global checking_accounts

  display_header("Olá, {}!".format([user.name for user in users if user.cpf == user_cpf][0]))

  checking_accounts_for_this_user = [account for account in checking_accounts if account.cpf == user_cpf]

  menu_items = []

  if len(checking_accounts_for_this_user) == 0:
    menu_items = [
      ["1", "Sim"],
      ["2", "Não"]
    ]

    display_menu("Nenhuma conta-corrente encontrada no seu nome. Deseja criar uma?", menu_items)
    option = menu_input(menu_items)

    if option == "1":
      create_checking_account(user_cpf)
    else:
      quit_program()
  else:
    for account in checking_accounts_for_this_user:
      menu_items.append([account.account_number, "Agência: {0} | Conta-corrente: {1} | Saldo: R$ {2}".format(account.branch, account.account_number, format(float(account.balance), '.2f'))])

    menu_items.append(["0", "Voltar"])

    display_menu("Selecione uma conta-corrente ou digite 0 para voltar", menu_items)
    option = menu_input(menu_items)

    if option == "0":
      user_account_dashboard(user_cpf)

    selected_checking_account = [account for account in checking_accounts_for_this_user if account.account_number == option][0]

    checking_account_menu(selected_checking_account)

def initial_auth():
  global users, checking_accounts

  display_header("Bem-vindo! Acesse sua conta")

  while True:
    user_cpf = validateable_input("Digite seu CPF")

    if(user_cpf == "0"):
      quit_program()
    
    if not validate_cpf(user_cpf):
      prints("Por favor, insira um CPF válido. Tente novamente.\n")
      continue

    if user_cpf not in [user.cpf for user in users]:
      no_user_account_found(user_cpf)
      continue
    else:
      user_account_dashboard(user_cpf)
      continue

#
# Inicialização do sistema
#
def main():
  initial_auth()

main()