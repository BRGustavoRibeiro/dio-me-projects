from .prints import *
from .tools import *

#
# Inputs básicos
#
def non_empty_input(text: str):
  while True:
    value: str = input("  » " + text + " ").upper().strip()

    if value:
      return value
    else:
      print_error("Este campo não pode ser vazio. Tente novamente.")

def integer(text: str):
  while True:
    value: str = non_empty_input(text)

    try:
      return int(value)
    except ValueError:
      print_error("Este campo deve ser um número inteiro. Tente novamente.")

def float_number(text: str):
  while True:
    value: str = non_empty_input(text)

    try:
      return float(value)
    except ValueError:
      print_error("Este campo deve ser um número. Tente novamente.")
      
#
# Inputs especiais
#
def password(text: str):
  while True:
    password: str = str(integer(text))

    if len(password) == 4:
      return password
    else:
      print_error("A senha deve ter 4 dígitos numéricos. Tente novamente.")

def cpf(text: str):
  while True:
    cpf: str = non_empty_input(text)

    if validate_cpf(cpf):
      return cpf
    else:
      print_error("CPF inválido. Tente novamente.")

def cnpj(text: str):
  while True:
    cnpj: str = non_empty_input(text)

    if validate_cnpj(cnpj):
      return cnpj
    else:
      print_error("CNPJ inválido. Tente novamente.")

def cpf_or_cnpj(text: str):
  while True:
    document: str = non_empty_input(text)

    if validate_cpf(document) or validate_cnpj(document):
      return document
    else:
      print_error("CPF ou CNPJ inválido. Tente novamente.")

def date(text: str):
  while True:
    date: str = non_empty_input(text)

    if validate_date(date):
      return date
    else:
      print_error("Data inválida. Tente novamente.")

def state(text: str):
  while True:
    state: str = non_empty_input(text)

    if validate_state(state):
      return state
    else:
      print_error("Estado inválido. Tente novamente.")

def integer_between(text: str, min: int, max: int):
  while True:
    value: int = integer(text)

    if min <= value <= max:
      return value
    else:
      print_error("Este campo deve ser um número entre " + str(min) + " e " + str(max) + ". Tente novamente.")

def skip(clear_screen: bool = True):
  input("  » Pressione ENTER para continuar...")
  if clear_screen:
    clear()