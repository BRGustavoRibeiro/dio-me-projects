from util import page, input, menu, tools
from util.prints import print_error, system_operation_confirmation_output, prints
from datastructure.user_account import UserAccount
from datastructure.natural_person import NaturalPerson
from datastructure.legal_person import LegalPerson
from datastructure.checking_account import CheckingAccount
from datastructure.transaction_register import Transaction

#
# Checking account dashboard/operations
#
def user_checking_account_deposit(checking_account: CheckingAccount):
  page.title("Depósito")
  page.heading("Vamos fazer um depósito na sua conta-corrente!")

  value: float = input.float_number("Qual é o valor do depósito? R$")

  checking_account.register_transaction(
    Transaction(
      "deposit",
      value
    )
  )

  tools.clear()
  page.title("Depósito")
  page.heading("Depósito realizado com sucesso!")

  system_operation_confirmation_output("transaction", checking_account)
  input.skip()

  return checking_account

def user_checking_account_dashboard(checking_account: CheckingAccount, user_account: UserAccount):
  # page.title() that will display the account branch, number and balance
  page.title("Ag: " + str(checking_account.get_branch()) + " | CC: " + str(checking_account.get_account_number()) + " | Saldo: " + str(checking_account.get_formatted_balance()))
  page.heading("O que deseja fazer hoje?")
  
  options = [
    "Depositar",
    "Sacar",
    "Extrato",
    "Alterar limites"
  ]

  choice = menu.display_with_back_last(options, "Digite sua opção:", "Sair da conta")
  return choice

#
# User account dashboard
#
def user_checking_account_creation(user_account: UserAccount, database: list[CheckingAccount]):
  page.title("Abertura de conta-corrente")
  page.heading("Vamos abrir uma conta-corrente para você!")

  while True:
    branch: str = str(input.integer("Em qual agência a conta será aberta? (4 dígitos)"))
    if len(branch) != 4:
      print_error("A agência deve ter 4 dígitos numéricos. Tente novamente.")
    else:
      break
    
  max_withdrawal_value: float = input.float_number("Qual será o valor máximo de saque por operação? R$")
  max_withdrawal_operations_per_day: int = input.integer("Qual será o número máximo de saques por dia?")

  checking_account = CheckingAccount.create_checking_account(
    branch,
    user_account.get_document(),
    max_withdrawal_value,
    max_withdrawal_operations_per_day,
    database
  )

  if checking_account == None:
    print_error("Não foi possível criar a conta-corrente. Tente novamente.")
    input.skip()
    return None
  else:
    tools.clear()
    page.title("Abertura de conta-corrente")
    page.heading("Conta-corrente aberta com sucesso!")

    database.append(checking_account)
    system_operation_confirmation_output("account_info", checking_account)
    
    input.skip()

  return database

def user_checking_accounts_list(user_account: UserAccount, database: list[CheckingAccount]):
  page.title("Minhas contas-correntes")
  page.heading("Qual conta você deseja acessar?")

  options = []

  checking_accounts_in_user_account = []

  for checking_account in database:
    if checking_account.get_document() == user_account.get_document():
      checking_accounts_in_user_account.append(checking_account)
      options.append(str("Ag: " + str(checking_account.get_branch())) + " | CC: " + str(checking_account.get_account_number()) + " | Saldo: " + str(checking_account.get_formatted_balance()))

  if len(options) == 0:
    print_error("Você ainda não possui contas-correntes.")
    input.skip()
    return None

  choice = menu.display_with_back_last(options, "Escolha uma conta-corrente:")

  while True:
    if choice == 0:
      return None
    else:
      if checking_accounts_in_user_account[choice - 1] == None:
        print_error("Escolha uma opção válida.")
        continue
      else:
        return checking_accounts_in_user_account[choice - 1]

def user_account_dashboard(user_account: UserAccount, database: list[UserAccount]):
  page.title(("Bem-vindo, " if type(user_account.get_entity()) == NaturalPerson else "") + user_account.get_entity().get_name() + "!")
  page.heading("O que deseja fazer hoje?")

  options = [
    "Ver minhas contas-correntes",
    "Abrir uma nova conta-corrente",
    "Editar meus dados pessoais " if type(user_account.get_entity()) == NaturalPerson else "Editar os dados da empresa",
  ]

  return menu.display_with_back_last(options, "Digite sua opção:", "Encerrar sessão")

#
# Account creation journey
#
def create_new_account(document: str, database: list[UserAccount]):
  page.title("Criação de conta")
  page.heading("Vamos criar uma conta para você!")

  if len(document) == 11:
    name: str = input.non_empty_input("Qual é o seu nome?")
    birth_date: str = input.date("Qual é a sua data de nascimento?")
    address: str = input.non_empty_input("Qual é o seu endereço?")
    address_number: str = input.integer("E o número?")
    address_neighborhood: str = input.non_empty_input("Em que bairro você mora?")
    address_city: str = input.non_empty_input("Qual é a sua cidade?")
    address_state: str = input.state("E o estado? (digite a sigla)")
    user_password: str = input.password("Qual vai ser a sua senha? (4 dígitos)")

    user_account = UserAccount(
      NaturalPerson(
        document,
        name,
        birth_date,
        address,
        address_number,
        address_neighborhood,
        address_city,
        address_state
      ),
      user_password
    )
  elif len(document) == 14:
    name: str = input.non_empty_input("Qual é o nome da sua empresa?")
    address: str = input.non_empty_input("Qual é o seu endereço?")
    address_number: str = input.integer("E o número?")
    address_neighborhood: str = input.non_empty_input("Em que bairro você mora?")
    address_city: str = input.non_empty_input("Qual é a sua cidade?")
    address_state: str = input.state("E o estado? (digite a sigla)")
    user_password: str = input.password("Qual vai ser a sua senha? (4 dígitos)")

    user_account = UserAccount(
      LegalPerson(
        document,
        name,
        address,
        address_number,
        address_neighborhood,
        address_city,
        address_state
      ),
      user_password
    )

  database.append(user_account)

  print ([str(x) for x in database])
  input.skip()

#
# Authentication journey
#
def account_not_found_prompt():
  page.title("Acesso a conta")
  page.heading("Ainda não tem uma conta com a gente?")

  options = [
    "Criar nova conta",
    "Voltar"
  ]

  return True if menu.display(options, "O que deseja fazer?") == 2 else False

def authentication(database: list[UserAccount]):
  return_from_account_not_found_prompt = False

  while not return_from_account_not_found_prompt:
    page.title("Acesso a conta")
    page.heading("Bem-vindo ao Intrabank. Vamos começar?")

    document: str = input.cpf_or_cnpj("Qual é o seu CPF ou CNPJ?")

    while True:
      for user_account in database:
        if user_account.get_document() == document:
          password_tries = 0

          while password_tries < 3:
            password: str = input.password("Qual é a sua senha?")

            if user_account.get_password() == password:
              return user_account
            else:
              print_error("Senha incorreta. Tente novamente.")
              password_tries += 1

            if password_tries == 3:
              print_error("Você excedeu o número máximo de tentativas.")
              tools.clear()
              print("Limite de tentativas excedido.")
              print("Por segurança, o programa será encerrado.")
              quit()
      
      if account_not_found_prompt() == False:
        create_new_account(document, database)
      
      break