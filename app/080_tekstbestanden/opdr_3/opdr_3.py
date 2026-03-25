# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypt(tekst, verschuiving):
    encrypted_tekst = ""
    for char in tekst:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + verschuiving) % 26 + base)
            encrypted_tekst += encrypted_char
        else:
            encrypted_tekst += char
    return encrypted_tekst
input_tekst = input("Geef de tekst die wilt encrypten.. \n")
verschuiving = 5

print(encrypt(input_tekst, verschuiving))
