# Opdracht 1 while-loops
# Naam student:
# Groep:

#In deze opdracht ga je een korte enquete maken.  
#Je hebt 3 vragen waar je graag antwoord op wil hebben.  
#Dit zijn ze: 
#* Wat vind je van de huidige regering?
#* Wat vind je van de Python-lessen tot nu toe?
#* Wat vind jij de mooiste stad van Nederland?

#Als de 3 vragen zijn beantwoord worden de resultaten opgeslagen in een tekstbestand.
# Jouw code komt hier

antwoord1 = input("Wat vind je van de huidige regering? ")
antwoord2 = input("Wat vind je van de Python-lessen tot nu toe? ")
antwoord3 = input("Wat vind jij de mooiste stad van Nederland? ")

with open("enquete_resultaten.txt", "w") as file:
    file.write("Vraag 1: " + antwoord1 + "\n")
    file.write("Vraag 2: " + antwoord2 + "\n")
    file.write("Vraag 3: " + antwoord3 + "\n")

print("De resultaten zijn opgeslagen!")

import os
print(os.getcwd())