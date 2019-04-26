# -*- coding: utf8 -*-
import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

def get_random_item(my_list):
  rand_numb = random.randint(0, len(my_list) - 1) #le nom du module et randit le nom de la méthode
  item = my_list[rand_numb]
  return item

def capitalize(words):
     for word in words:
         word.capitalize()

def message(character, quote):
    name_character = character.capitalize()
    name_quote= quote.capitalize()
    return "{} a dit : {}".format(name_character, name_quote)     

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

# Tant que la réponse de l'utilisateur n'ai pas B
while user_answer != "B":
    print(message(get_random_item(characters), get_random_item(quotes))) #Affiche une citation
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

