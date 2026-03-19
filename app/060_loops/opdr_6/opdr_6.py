# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
#n deze opdracht ga je list-methoden gebruiken om een lijst pizza's aan te passen en te printen.
#Gebruik deze lijst met pizza's:
#> ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

#Sorteer de lijst op alfabet
#> ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi']


#Voeg naar eigen smaak nog een pizza toe
#> ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi', 'yo-favorito']

#Verwijder de pizza die je het minst lekker vindt
#> ['calzone', 'margharita', 'quattro stagioni', 'verdi', 'yo-favorito']

#Print de eerste 3 pizza's uit de lijst
#> ['calzone', 'margharita', 'quattro stagioni']  

#Print alleen de middelste pizza uit de lijst  
#> ['quattro stagioni']

#Print de laatste 3 pizza's uit de lijst
#> ['quattro stagioni', 'verdi', 'yo-favorito']

# Hier start de for-loop

my_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
my_list.sort()
print(my_list)
my_list.append('yo-favorito')
print(my_list)  
my_list.remove('olivio')
print(my_list)
print(my_list[0:3])
print(my_list[2:3])
print(my_list[-3:])


