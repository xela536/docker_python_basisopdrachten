# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

#Schrijf een programma dat twee input variabelen accepteert. De variabelen stellen twee zijden van een rechthoekig driehoek voor. Bereken de lengte van de 3e zijde door gebruik te maken van de stelling van pythagoras. (effe googlen dus!)

#Output van het programma is...

#> Geef de lengte van de eerste zijde  
#4  
#> Geef de lengte van de tweede zijde  
#> 3  
#> 
#> De lengte van de schuine zijde is: 5


#> Geef de lengte van de eerste zijde  
#> 12  
#> Geef de lengte van de tweede zijde  
#> 9  
#> 
#> De lengte van de schuine zijde is: 15

#> Geef de lengte van de eerste zijde  
#> 11  
#> Geef de lengte van de tweede zijde  
#> 9  
#> 
#> De lengte van de schuine zijde is: 14.21267040355189


print("Geef de lengte van de eerste zijde")
zijde_1 = int(input())  
print("Geef de lengte van de tweede zijde")
zijde_2 = int(input())      
zijde_3 = (zijde_1**2 + zijde_2**2)**0.5
print("De lengte van de schuine zijde is:", zijde_3)   
