from random import sample
from string import ascii_letters, digits


# Print a long unreadable password using a compbination of letters and digits
size = 25
password = sample(ascii_letters + digits, size)
print("".join(password))
