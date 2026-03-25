# Opdracht 3 condities
# Naam student:
# Groep:
#Bekijk de volgende dictionaries:
#```python
#normale_toegangsprijs = 12.50
#kortings_percentages = { "baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30 }
#leeftijd = { "baby": (0,2), "kinderen": (3,18), "volwassenen": (19,64), "ouderen": (65,150) }

#```
#Voor een attractiepark moet de toegangsprijs voor bezoekers worden berekend.  
#Schrijf een programma dat gebruik maakt van de gegeven variabelen en een input functie waarmee de leeftijd van een bezoeker wordt gevraagd.  
#Het programma geeft de volgende output:

#> Geef uw leeftijd in aantal jaar  
#3  
#U behoort tot de groep kinderen  
#U krijgt 50% korting  
#U betaalt daarom 6.25  

#> Geef uw leeftijd in aantal jaar   
#23  
#U behoort tot de groep volwassenen  
#U krijgt 0% korting  
#3U betaalt daarom 12.5  

#> Geef uw leeftijd in aantal jaar   
#89  
#U behoort tot de groep ouderen  
#U krijgt 30% korting  
#U betaalt daarom 8.75  




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
print("Geef uw leeftijd in aantal jaar")
leeftijd_bezoeker = int(input())        
if leeftijd["baby"][0] <= leeftijd_bezoeker <= leeftijd["baby"][1]:
    print("U behoort tot de groep baby")
    print(f"U krijgt {kortings_percentages['baby']}% korting")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - kortings_percentages['baby'] / 100)}")       
elif leeftijd["kinderen"][0] <= leeftijd_bezoeker <= leeftijd["kinderen"][1]:
    print("U behoort tot de groep kinderen")
    print(f"U krijgt {kortings_percentages['kinderen']}% korting")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - kortings_percentages['kinderen'] / 100)}")
elif leeftijd["volwassenen"][0] <= leeftijd_bezoeker <= leeftijd["volwassenen"][1]:
    print("U behoort tot de groep volwassenen")
    print(f"U krijgt {kortings_percentages['volwassenen']}% korting")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - kortings_percentages['volwassenen'] / 100)}")

elif leeftijd["ouderen"][0] <= leeftijd_bezoeker <= leeftijd["ouderen"][1]:
    print("U behoort tot de groep ouderen")
    print(f"U krijgt {kortings_percentages['ouderen']}% korting")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - kortings_percentages['ouderen'] / 100)}")
    
