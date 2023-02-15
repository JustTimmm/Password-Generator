import random
import string

password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

with open("mdp.txt", "a") as file:
    file.write(password + "\n")

print("Mdp : ", password)