# Opdracht 3 condities
# Naam student:
# Groep:



normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

leeftijd_bezoeker = int(input("Geef uw leeftijd in aantal jaar: "))
if leeftijd["baby"][0] <= leeftijd_bezoeker <= leeftijd["baby"][1]:
    groep = "baby"
elif leeftijd["kinderen"][0] <= leeftijd_bezoeker <= leeftijd["kinderen"][1]:
    groep = "kinderen"
elif leeftijd["volwassenen"][0] <= leeftijd_bezoeker <= leeftijd["volwassenen"][1]:
    groep = "volwassenen"
elif leeftijd["ouderen"][0] <= leeftijd_bezoeker <= leeftijd["ouderen"][1]:
    groep = "ouderen"

print(f"U behoort tot de groep {groep}")
print(f"U krijgt {kortings_percentages[groep]}% korting")
print(f"U betaalt daarom {normale_toegangsprijs * (1 - kortings_percentages[groep] / 100)}")

