import random
import string
import time

chars = (
    string.punctuation
    + string.digits
    + string.ascii_lowercase
    + string.ascii_uppercase
    + " "
)
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

plainText = input("Enter a message to be encrypted: ")
cipherText = ""

for letter in plainText:
    index = chars.index(letter)
    cipherText = cipherText + key[index]

print("---------- ENCRYPTING MESSAGE ----------")
print("----------------------------------------")
time.sleep(2)
print(f"Encrypted Message: {cipherText}")


# Decryption
print()
print("---------- DECRYPTING MESSAGE ----------")
print("----------------------------------------")
time.sleep(2)

OG_Text = ""
for x in cipherText:
    index = key.index(x)
    OG_Text = OG_Text + chars[index]

print(f"Decrypted Message: {OG_Text}")
