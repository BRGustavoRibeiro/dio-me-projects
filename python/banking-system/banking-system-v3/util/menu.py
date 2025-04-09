from .prints import *
from .input import integer_between

# This is a function that will create a menu for the user to select from.
# It will return the index of the selected option.

def display(options, choose_text):
  for i in range(len(options)):
    prints(str(i + 1).rjust(2, " ") + " › " + options[i])
  
  prints("")

  return integer_between(choose_text, 1, len(options))

def display_with_back_last(options, choose_text, text_back = "Voltar"):
  for i in range(len(options)):
    prints(str(i + 1).rjust(2, " ") + " › " + options[i])

  prints(" 0 › " + text_back)
  prints("")

  return integer_between(choose_text, 0, len(options))