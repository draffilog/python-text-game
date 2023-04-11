import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import random

# Define the Room class
class Room:
    # Constructor for the Room class
    def __init__(self, filename):
        # Initialize attributes
        self.treasure = None
        self.keys = None
        self.times_won = 0

        # Read the room file
        with open(filename, 'r') as f:
            lines = f.readlines()

        # Remove empty lines from the list of lines
        lines = [line.rstrip() for line in lines if line.rstrip()]

        # Set the room name
        self.name = filename.split('.')[0]
        self.visited = False

        # Initialize the room description
        self.description = ""
        # Read the room description from the file
        for line in lines:
            if line.startswith("# description #"):
                idx = lines.index(line)
                while not lines[idx + 1].startswith("#"):
                    self.description += lines[idx + 1]
                    idx += 1
                break  # Exit the loop after reading the description

        # Read the enemy information from the file
        for line in lines:
            if line.startswith("enemy"):
                enemy_data = line.split(':')[1].split(',')
                self.enemy = {
                    'name': enemy_data[0].strip(),
                    'damage': int(enemy_data[1].strip()),
                    'health': int(enemy_data[2].strip())
                }
                break

        # Read the points information from the file
        for line in lines:
            if line.startswith("points"):
                self.points = int(line.split(':')[1].strip())
                break

        # Read the weapon information from the file
        for line in lines:
            if line.startswith("weapon"):
                weapon_data = line.split(':')[1].split(',')
                self.weapon = {
                    'name': weapon_data[0].strip(),
                    'damage': int(weapon_data[1].strip()),
                    'price': int(weapon_data[2].strip())
                }
                break

        # Read the money information from the file
        for line in lines:
            if line.startswith("money"):
                self.money = int(line.split(':')[1].strip())
                break

        # Read the treasure information from the file
        for line in lines:
            if line.startswith("treasure"):
                treasure_data = line.split(':')[1].split(',')
                self.treasure = {
                    'code': int(treasure_data[0]),
                    'points': int(treasure_data[1].rstrip())
                }
                break

        # Read the key information from the file
        for line in lines:
            if line.startswith("key"):
                key_data = line.split(':')[1].split(',')
                self.keys = {
                    'code': int(key_data[0]),
                    'price': int(key_data[1].rstrip())
                }
                break

        # Read the healing pad information from the file
        for line in lines:
            if line.startswith("healingpad"):
                self.healing_pad = int(line.split(':')[1].strip())
                break
        else:  # If there's no healing pad, set it to 0
            self.healing_pad = 0

# Define the Shop class
class Shop:
    # Constructor for the Shop class
    def __init__(self, filename):
        # Read the shop file
        with open(filename, 'r') as f:
            lines = f.readlines()

        # Set the shop name
        self.name = "shop"

        # Initialize the shop description
        self.description = ""
        # Read the shop description from the file
        for line in lines:
            if line.startswith("# description"):
                idx = lines.index(line)
                while not lines[idx + 1].startswith("#"):
                    self.description += lines[idx + 1]
                    idx += 1

        # Initialize the list of weapons
        self.weapons = []
        # Read the weapon information from the file
        for line in lines:
            if line.startswith("weapon"):
                weapon_data = line.split(':')[1].split(',')
                self.weapons.append({
                    'name': weapon_data[0].strip(),
                    'damage': int(weapon_data[1]),
                    'price': int(weapon_data[2].rstrip())
                })

        # Initialize the list of keys
        self.keys = []
        # Read the key information from the file
        for line in lines:
            if line.startswith("key"):
                key_data = line.split(':')[1].split(',')
                self.keys.append({
                    'code': int(key_data[0]),
                    'price': int(key_data[1].rstrip())
                })

        # Set the healing pad information
        self.healing_pad = {
            'health': 50,
            'price': int(lines[14])
        }

        # Initialize the list of armours
        self.armours = []
        # Read the armour information from the file
        for line in lines:
            if line.startswith("armour"):
                armour_data = line.split(':')[1].split(',')
                self.armours.append({
                    'durability': int(armour_data[0]),
                    'price': int(armour_data[1].rstrip())
                })

# Define the Player class
class Player:
    # Constructor for the Player class
    def __init__(self, name):
        # Set the player's name
        self.name = name
        
        # Initialize the player's money with a random value between 50 and 350
        self.money = random.randint(50, 350)
        
        # Set the player's initial health to 100
        self.health = 100
        
        # Initialize the player's points to 0
        self.points = 0
        
        # Initialize the player's inventory with empty lists for weapons, keys, armours, and unopened treasures
        self.inventory = {
            'weapons': [],
            'keys': [],
            'armours': [],
            'unopened_treasures': []
        }
        
        # Initialize the number of healing pads bought by the player to 0
        self.healing_pads_bought = 0

        
# Main function of the game
def main(): 
    # Get the player's name as input
    player_name = input("Enter your name: ")
    
    # Create a player object with the given name
    player = Player(player_name)
    
    # Create room objects using the corresponding text files
    room1 = Room("Room1.txt")
    room2 = Room("Room2.txt")
    room3 = Room("Room3.txt")
    room4 = Room("Room4.txt")
    
    # Create a shop object using the Shop.txt file
    shop = Shop("Shop.txt")
    