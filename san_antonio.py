# -*- coding: utf8 -*-
import random
import json

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

# characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

# Read values from a JSON file -> lire les donnée dans le fichier json
# Create a new empty list -> crée une liste vide 
# Open a json file with my objects -> ouvre le fichier json
# Load all the data contained in my file.data = entries -> charger toute les donnée contenu dans ce fichier
# add each item in my list -> chaque éléments va être stocker dans la new list
# return my completed list -> renvoye la liste fini
def read_value_from_json(file, key):
      values = []
      with open(file) as f:
          data = json.load(f)
          for entry in data:
              values.append(entry[key])
      return values

def get_random_item(my_list):
      rand_numb = random.randint(0, len(my_list) - 1) #le nom du module et randit le nom de la méthode
      item = my_list[rand_numb]
      return item

def random_character():
      all_values = read_value_from_json('characters.json', 'character')
      return get_random_item(all_values)

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
      print(message(random_character(), get_random_item(quotes))) # Affiche une citation
      user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

