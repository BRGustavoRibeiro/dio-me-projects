from .entity import Entity

#
# This is a class that represents a brazilian natural person. It inherits from entity.
#
# A natural person has the following data structure:
# - cpf: str - CPF acts like a primary key for the natural person.
# - name: str - The natural person's full name. It needs to have at least two names.
# - birthday: str - The natural person's birthday. It needs to be in the format DD/MM/YYYY.
#
# It has the following methods:
# - change_cpf: changes the natural person's CPF.
# - change_name: changes the natural person's name.
# - change_birthday: changes the natural person's birthday.
# - get_cpf: returns the natural person's CPF.
# - get_name: returns the natural person's name.
# - get_birthday: returns the natural person's birthday.

class NaturalPerson(Entity):
  def __init__(self, cpf, name, birthday, address, address_number, address_neighborhood, address_city, address_state):
    super().__init__(name, address, address_number, address_neighborhood, address_city, address_state)
    self.__cpf = cpf
    self.__birthday = birthday

  def change_cpf(self, new_cpf):
    self.__cpf = new_cpf

  def change_name(self, new_name):
    super().change_name(new_name)

  def change_birthday(self, new_birthday):
    self.__birthday = new_birthday

  def get_cpf(self):
    return self.__cpf

  def get_name(self):
    return super().get_name()

  def get_birthday(self):
    return self.__birthday