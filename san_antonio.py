# -*- coding: utf8 -*-
import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre.",
    "Ti pas, ti pas na arriver !",
    "Ti lampe ti lampe!",
    "Tien bo largue pa dalon!"
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "Simba",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou",
    "mulan"
]

def message(character, quote):
    name_character = character.capitalize()
    name_quote = quote.capitalize()
    return "{} a dit : {}".format(name_character, name_quote)

def get_random_quote():
    # get a random number
    # get a quote from an array
    # show the quote in the interpreter
    pass

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return item # return the item

# Programm
user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(get_random_item_in(characters), get_random_item_in(quotes)))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')