from .prints import prints
from .tools import clear

def title(title):
  clear()
  print("┌──────────────────────────────────────────────────────┐")
  print("│ ♦ Intrabank " + str(title).rjust(40, " ") + " │")
  print("└──────────────────────────────────────────────────────┘\n")

def heading(text):
  prints("" + text)
  prints("".rjust(len(text) + 3, "¯"))