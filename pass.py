import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_@#$%^&*!~"
length=int(input("\n Enter the length:"))
password=""
for a in range(length):
    password+=random.choice(chars)
print(password)