from enum import Enum
import json
import os

# The type atr for the food class. Also created the enum for use. 
class Food_Types(Enum):
    Metal = 1
    Veggies = 2 
    Fruit = 3
    Armor = 4
    Insect = 5
    Water = 6
    Beef = 7
    Poultry = 8
    Miscilaneous = 9

# Class food, is built to take the attributes of an object representing food for
# a pet class, to either grow levels, give bonuses, and evolve. 
class Food():
    fd_list:dict
    def __init__(self) -> None:
        self.create_list()
    
    def create_list(self):
        cur_dir = os.getcwd()
        path = cur_dir + '/' + 'tamagatchi/assets/food/food_list.json'
        f_list = open(path)
        self.fd_list = json.load(f_list)

    def get_food(self, name):
        for fd in self.fd_list['Food']:
            if fd['name'] == name:
                return fd
        return None
    