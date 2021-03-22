import random
from string import digits, punctuation, ascii_letters

l = 20
symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()

password = "".join(secure_random.choice(symbols) for i in range(l))

print(password)
