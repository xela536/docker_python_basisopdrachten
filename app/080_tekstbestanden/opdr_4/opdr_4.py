# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]


persoon = {}


sleutels = ["voornaam", "achternaam", "drank", "eten"]


for i in range(len(vragen)):
    antwoord = input(f"{i+1}. {vragen[i]} \n")
    persoon[sleutels[i]] = antwoord


print("\nBedankt voor het invullen!")
print("See you at the party.")


with open("feestgangers.txt", "a") as bestand:
    bestand.write("----\n")
    for sleutel, waarde in persoon.items():
        bestand.write(f"{sleutel}: {waarde}\n")
    bestand.write("\n")