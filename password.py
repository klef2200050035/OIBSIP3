import random
import string

print("----------- Random Password Generator -----------")
length = int(input("\nEnter the length of the password: "))

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

y = random.sample(characters, length)

password= ''.join(y)

print(password)
