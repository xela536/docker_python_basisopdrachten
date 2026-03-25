# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

#In deze opdracht maak je het spel "Raad een nummertje"
#* Je programma verzint een random getal tussen de 1 en 100.
#* De gebruiker voert een getal in
#* Het programma antwoord met 'hoger' of 'lager' totdat de gebruiker het juiste getal heeft geraden!
#* De uitvoer van het programma geeft weer wat het te raden getal is
#* Het programma geeft het aantal keer dat de gebruiker moest raden weer.

#Output:
#> Raad mijn geheime getal   
#50  
#hoger  
#Raad mijn geheime getal   
#75  
#Je hebt het getal geraden het is 75!  
#Je hebt het in 2 keer gedaan


import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

aantal_keer_geraden = 0
geraden = False

while not geraden:
    antwoord = int(input(prompt))
    aantal_keer_geraden += 1

    if antwoord < geheim_getal:
        print("hoger")
    elif antwoord > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_keer_geraden} keer gedaan")
        geraden = True
