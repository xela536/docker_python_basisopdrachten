# Opdracht 3 input functie
# Naam student:
# Groep:
#Gebruik de input functie om een lijst met minimaal 5 objecten te maken. Dat mag van alles zijn: games, voertuigen, motoren, snoep, whatever.  
#Print de lijst gesorteerd in omgekeerde volgorde, dus woorden die met een z beginnen staan vooraan.

#Stel je vraagt de gebruiker om steden in te vullen:
#> Amsterdam, Zwolle, Dronten, Haarlem, Zaanstad
# Hier komt je code...

steden = input("vul een paar steden in").split(", ")

steden.sort(reverse=True)

print(steden)