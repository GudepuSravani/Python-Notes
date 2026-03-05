import random
import string

print("=== PASSWORD GENERATOR ===")

# Ask user for password length
length = int(input("Enter password length: "))

# Ask how many passwords to generate
num = int(input("How many passwords do you want? "))

# Character set (letters + numbers + symbols)
characters = string.ascii_letters + string.digits + string.punctuation

print("\nGenerated Passwords:\n")

for i in range(num):
    password = ""

    for j in range(length):
        password += random.choice(characters)

    print("Password", i+1, ":", password)