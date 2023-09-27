#
# This is a class that represents an entity. It is a parent class for 2 other classes: natural_person and legal_person.
#
# An entity has the following data structure:
# - name: str - The entity's full name. It needs to have at least two names.
# - address: str - The entity's address. It needs to have at least 10 characters.
# - address_number: str - The entity's address number. It needs to have between 1-5 characters.
# - address_neighborhood: str - The entity's address neighborhood. It needs to have at least 5 characters.
# - address_city: str - The entity's address city. It needs to have at least 5 characters.
# - address_state: str - The entity's address state. It needs to have 2 characters. It needs to match one element in a list of all brazilian states acronym, composed of 2 letters.
#
# It has the following methods:
# - change_name: changes the entity's name.
# - change_address: changes the entity's address.
# - change_address_number: changes the entity's address number.
# - change_address_neighborhood: changes the entity's address neighborhood.
# - change_address_city: changes the entity's address city.
# - change_address_state: changes the entity's address state.
# - get_name: returns the entity's name.
# - get_address: returns the entity's address. It will return a string composed of the address, address number, address neighborhood, address city and address state.

class Entity:
  def __init__(self, name, address, address_number, address_neighborhood, address_city, address_state):
    self.__name = name
    self.__address = address
    self.__address_number = address_number
    self.__address_neighborhood = address_neighborhood
    self.__address_city = address_city
    self.__address_state = address_state

  def change_name(self, new_name):
    self.__name = new_name

  def change_address(self, new_address):
    self.__address = new_address

  def change_address_number(self, new_address_number):
    self.__address_number = new_address_number

  def change_address_neighborhood(self, new_address_neighborhood):
    self.__address_neighborhood = new_address_neighborhood

  def change_address_city(self, new_address_city):
    self.__address_city = new_address_city

  def change_address_state(self, new_address_state):
    self.__address_state = new_address_state

  def get_name(self):
    return self.__name

  def get_address(self):
    return self.__address + ", " + self.__address_number + ", " + self.__address_neighborhood + ", " + self.__address_city + ", " + self.__address_state