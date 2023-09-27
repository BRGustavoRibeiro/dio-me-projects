from .entity import Entity

#
# This is a class that represents a legal person. It inherits from entity.
#
# A legal person has the following data structure:
# - cnpj: str - CNPJ acts like a primary key for the legal person.
# - name: str - The legal person's full name. It needs to have at least two names.
#
# It has the following methods:
# - change_cnpj: changes the legal person's CNPJ.
# - change_name: changes the legal person's name.
# - get_cnpj: returns the legal person's CNPJ.
# - get_name: returns the legal person's name.

class LegalPerson(Entity):
  def __init__(self, cnpj, name, address, address_number, address_neighborhood, address_city, address_state):
    super().__init__(name, address, address_number, address_neighborhood, address_city, address_state)
    self.__cnpj = cnpj

  def change_cnpj(self, new_cnpj):
    self.__cnpj = new_cnpj

  def change_name(self, new_name):
    super().change_name(new_name)

  def get_cnpj(self):
    return self.__cnpj

  def get_name(self):
    return super().get_name()