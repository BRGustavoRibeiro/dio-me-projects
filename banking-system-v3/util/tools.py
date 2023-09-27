from os import system, name

def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def end():
  clear()
  print("Obrigado por ser cliente do Intrabank. Volte sempre!")
  quit()

def validate_state(state: str):
  states = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
    "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
  ]

  if state.upper() in states:
    return True
  else:
    return False

def validate_date(date: str):
  if len(date) != 10:
    return False

  if date[2] != "/" or date[5] != "/":
    return False

  day: int = int(date[0:2])
  month: int = int(date[3:5])
  year: int = int(date[6:10])

  if day < 1 or day > 31:
    return False

  if month < 1 or month > 12:
    return False

  if year < 1900 or year > 2100:
    return False

  return True

def validate_cpf(cpf: str):
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

def validate_cnpj(cnpj: str):
  if len(cnpj) != 14 or not cnpj.isdigit():
    return False

  if cnpj == "00000000000000" or cnpj == "11111111111111" or cnpj == "22222222222222" or cnpj == "33333333333333" or cnpj == "44444444444444" or cnpj == "55555555555555" or cnpj == "66666666666666" or cnpj == "77777777777777" or cnpj == "88888888888888" or cnpj == "99999999999999":
    return False

  sum = 0
  weight = 5

  for n in range(12):
    sum += int(cnpj[n]) * weight
    weight -= 1

    if weight < 2:
      weight = 9

  verifying_digit = 11 - sum % 11

  if verifying_digit > 9:
    first_digit = 0
  else:
    first_digit = verifying_digit

  sum = 0
  weight = 6

  for n in range(13):
    sum += int(cnpj[n]) * weight
    weight -= 1

    if weight < 2:
      weight = 9

  verifying_digit = 11 - sum % 11

  if verifying_digit > 9:
    second_digit = 0
  else:
    second_digit = verifying_digit

  if cnpj[-2:] == "%s%s" % (first_digit, second_digit):
    return True
  else:
    return False

def validate_cpf_or_cnpj(document: str):
  if len(document) == 11:
    return validate_cpf(document)
  elif len(document) == 14:
    return validate_cnpj(document)
  else:
    return False