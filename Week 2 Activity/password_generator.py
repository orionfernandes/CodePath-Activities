import random as r
import string 

print('Welcome to random password generator \n')

length = 8

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

results = lowercase + uppercase + numbers + symbols

random_string = r.sample(results, length)

password = "".join(random_string)


print(f"Your password is {password} \n")
