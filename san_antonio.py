# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

def show_random_quote(my_list):
      # get a random number
  item = my_list[0]
  return item

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

# Tant que la réponse de l'utilisateur n'ai pas B
while user_answer != "B":
    print(show_random_quote(quotes)) #Affiche une citation
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

for character in characters:
  name_character = character.capitalize()
  print(name_character)
    
print(show_random_quote(quotes))