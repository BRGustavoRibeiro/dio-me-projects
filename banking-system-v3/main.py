from datastructure.user_account import UserAccount
from datastructure.checking_account import CheckingAccount
from datastructure.natural_person import NaturalPerson
from datastructure.legal_person import LegalPerson
from util import page, prints, tools
import pages

def TEMPORARIO_INICIO_DE_CARALHO():
  return_data = []

  return_data.append(
    UserAccount(
      NaturalPerson(
        "36206935876",
        "JOÃO DA SILVA",
        "11/09/2001",
        "AVENIDA PAULISTA",
        "01",
        "JARDIM PAULISTA",
        "SÃO PAULO",
        "SP"
      ),
      "1234"
    )
  )

  return_data.append(
    UserAccount(
      LegalPerson(
        "31979011000199",
        "EMPRESA MUITO EMPRESARIAL LTDA",
        "AVENIDA PAULISTA",
        "02",
        "JARDIM PAULISTA",
        "SÃO PAULO",
        "SP"
      ),
      "1234"
    )
  )

  return return_data

user_accounts: list[UserAccount] = TEMPORARIO_INICIO_DE_CARALHO()
checking_accounts: list[CheckingAccount] = []

def main():
  global user_accounts

  currentUser: UserAccount = pages.authentication(user_accounts)

  while True:
    choice = pages.user_account_dashboard(currentUser, user_accounts)

    if choice == 0:
      tools.end()
    elif choice == 1:
      checking_account = pages.user_checking_accounts_list(currentUser, checking_accounts)
      if checking_account == None or 0:
        continue
      else:
        while True:
          choice = pages.user_checking_account_dashboard(checking_account, currentUser)
          
          if choice == 0:
            break
          elif choice == 1:
            checking_account = pages.user_checking_account_deposit(checking_account)
          elif choice == 2:
            pages.user_checking_account_withdraw(checking_account)
          elif choice == 3:
            pages.user_checking_account_statement(checking_account)
          elif choice == 4:
            pages.user_checking_account_edit_limits(checking_account)
    elif choice == 2:
      user_accounts = pages.user_checking_account_creation(currentUser, checking_accounts)
    elif choice == 3:
      pages.edit_user_account(currentUser)
    
main()