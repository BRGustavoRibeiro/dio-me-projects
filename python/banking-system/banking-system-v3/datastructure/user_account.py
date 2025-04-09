from .entity import Entity
from .legal_person import LegalPerson
from .natural_person import NaturalPerson

#
# This is a class that represents a user account.
#
# An user account has the following data structure:
# - entity: Entity - The user's entity. It can be a natural person or a legal person. The user will login with CPF or CNPJ, according to the entity type.
# - password: str - The user's password. It is composed of 4 digits, mandatory.
#
# It has the following methods:
# - change_password: changes the user's password.
# - get_entity: returns the user's entity.
# - get_password: returns the user's password.
# - get_document: returns the user's CPF or CNPJ, according to the entity type.
# - authenticate: this should be a class method. It gets a CPF or a CNPJ and a password. It returns True if the authentication is successful, False otherwise.

class UserAccount:
  def __init__(self, entity, password):
    self.__entity = entity
    self.__password = password

  def change_password(self, new_password):
    self.__password = new_password

  def get_entity(self):
    return self.__entity

  def get_password(self):
    return self.__password

  def get_document(self):
    if isinstance(self.__entity, NaturalPerson):
      return self.__entity.get_cpf()
    elif isinstance(self.__entity, LegalPerson):
      return self.__entity.get_cnpj()
    
  @classmethod
  def authenticate(cls, document, password):
    if len(document) == 11:
      for user_account in cls.__user_accounts:
        if user_account.get_document() == document and user_account.get_password() == password:
          return True
    elif len(document) == 14:
      for user_account in cls.__user_accounts:
        if user_account.get_document() == document and user_account.get_password() == password:
          return True
    return False