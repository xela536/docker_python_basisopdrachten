# Opdracht 1 lists
# Naam student:
# Groep:
#Schrijf een programma waarin je een list aanmaakt.
#aarnaast maak je 4 dictionaries om gegevens van personen in op te slaan. Je mag zelf namen bedenken.
#```python
#{ "id": 0, "voornaam": "", "achternaam": "" }
#```
#Voeg de 4 dictionaries toe aan de list. Maak hierbij gebruik van een list-methode
#Print de volledige naam van de 2e persoon op het scherm door de juiste gegevens op de plek van de vraagtekens te zetten.



mylist = []
dict_1 = { "id": 1, "voornaam": "Jan", "achternaam": "Jansen" }
dict_2 = { "id": 2, "voornaam": "Piet", "achternaam": "Pieters" }
dict_3 = { "id": 3, "voornaam": "Klaas", "achternaam": "Klaassen" }
dict_4 = { "id": 4, "voornaam": "Maria", "achternaam": "de Vries" }


mylist.append(dict_1)
mylist.append(dict_2)
mylist.append(dict_3)
mylist.append(dict_4)

print(mylist[1]["voornaam"], mylist[1]["achternaam"])

