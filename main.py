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

        # Function to check if the player has won or lost the game
    def check_victory():
        # If player's points are equal to or greater than 10, they win
        if player.points >= 10:
            messagebox.showinfo("Victory", "Congratulations! You've won the game with 10 or more points!")
            root.destroy()  
            return True  
        # If player's points fall below 0, they lose
        elif player.points < 0:
            messagebox.showinfo("Defeat", "You've lost the game. Your points fell below 0.")
            root.destroy()  
            return True  
        return False  

    # Function to update the player's statistics displayed on the screen
    def update_stats():
        stats_label.config(text=f"Name: {player.name}\nMoney: {player.money}\nHealth: {player.health}\nPoints: {player.points}")
        
    # Function to choose a weapon from the player's inventory
    def choose_weapon(weapons):
        # Get a list of weapon names
        weapon_names = [weapon['name'] for weapon in weapons]
        weapon_choice = ""
        
        # Keep asking for input until a valid weapon name is provided
        while weapon_choice not in weapon_names:
            weapon_choice = tk.simpledialog.askstring("Choose a weapon", f"Your weapons: {', '.join(weapon_names)}")
        
        # Return the chosen weapon
        return next(weapon for weapon in weapons if weapon['name'] == weapon_choice)

    # Function to choose an armour from the player's inventory
    def choose_armour(armours):
        # Return None if no armours are available
        if not armours:
            return None

        # Get a list of armour names
        armour_names = [f"Armour {armour['durability']}" for armour in armours]
        armour_names.append("None")
        armour_choice = ""

        # Keep asking for input until a valid armour name is provided
        while armour_choice not in armour_names:
            armour_choice = tk.simpledialog.askstring("Choose armour", f"Your armours: {', '.join(armour_names)}")

        # Return None if the player chooses not to wear any armour
        if armour_choice == "None":
            return None
        else:
            # Return the chosen armour
            chosen_armour = next(armour for armour in armours if f"Armour {armour['durability']}" == armour_choice)
            return chosen_armour
    
    
    # Function to handle a fight between the player and an enemy in a room
    def fight(player, room, weapon, use_armour, armour_choice):
        # Calculate the enemy's damage
        enemy_damage = room.enemy['damage']
        
        # If the player is using armour, reduce enemy damage based on armour durability
        if use_armour:
            armor_durability = armour_choice['durability']
            enemy_damage //= armor_durability

        # Calculate player's damage using the chosen weapon
        player_damage = weapon['damage']
        
        # Initialize enemy and player health
        enemy_health = room.enemy['health']
        player_health = player.health

        # Continue the fight loop until either the player or the enemy has no health left
        while player_health > 0 and enemy_health > 0:
            # Reduce enemy health by the player's damage
            enemy_health -= player_damage

            # If the enemy is defeated
            if enemy_health <= 0:
                # Update player health and remove used weapon and armour from the inventory
                player.health = max(0, player_health)
                player.inventory['weapons'].remove(weapon) 
                if use_armour:
                    player.inventory['armours'].remove(armour_choice)
                return {"won": True, "player_health": player_health, "enemy_damage": player_damage}

            # Reduce player health by the enemy's damage
            player_health -= enemy_damage

            # If the player is defeated
            if player_health <= 0:
                # Update player health and remove used weapon and armour from the inventory
                player.health = max(0, player_health)
                player.inventory['weapons'].remove(weapon)
                if use_armour:
                    player.inventory['armours'].remove(armour_choice)
                return {"won": False, "player_health": player_health, "enemy_damage": player_damage}

        # Return a result dictionary with the fight outcome and updated player_health and enemy_damage values
        return {"won": None, "player_health": player_health, "enemy_damage": player_damage}

    # Function for handling the player's entry into a room
    def enter_room(room):
        # Check if the player has already won in this room
        if room.visited and room.times_won > 0:
            messagebox.showinfo("Already won", "You have already won in this room.")
            return

        # Mark the room as visited and display the room's description
        room.visited = True
        messagebox.showinfo(room.name, room.description)

        # Show enemy information
        enemy_info = f"{room.enemy['name']} (Damage: {room.enemy['damage']}, Health: {room.enemy['health']})"
        messagebox.showinfo("Enemy", f"Enemy in this room: {enemy_info}")

        # Let the player choose a weapon and armour for the fight
        weapon_choice = choose_weapon(player.inventory['weapons'])
        armour_choice = choose_armour(player.inventory['armours'])
        use_armour = armour_choice is not None

        # Perform the fight with the chosen weapon and armour
        fight_result = fight(player, room, weapon_choice, use_armour, armour_choice)

        # Update the player's health after the fight
        player.health = max(0, fight_result['player_health'])

        # If the player won the fight
        if fight_result['won']:
            # Display victory message and update points, money, and inventory
            messagebox.showinfo("Victory", "You have defeated the enemy!")
            player.points += room.points
            game_ended = check_victory()
            if game_ended:
                return

            player.money += room.money
            player.inventory['weapons'].append(room.weapon)
            if room.treasure is not None:
                player.inventory['unopened_treasures'].append(room.treasure)
            if room.keys is not None:
                player.inventory['keys'].append(room.keys)

            # Use the healing pad if available
            if room.healing_pad:
                healing_size = 50
                player.health += healing_size
                messagebox.showinfo("Healing Pad", f"You found a healing pad in the room! Your health has been increased by {healing_size}.")
            
            # Update the player's stats
            update_stats()

            # Increment the times_won attribute and set the enemy's health to 0
            room.times_won += 1
            room.enemy['health'] = 0

        # If the player lost the fight
        else:
            # Display defeat message and update points and health
            messagebox.showinfo("Defeat", "You have been defeated!")
            player.health = 0
            player.points -= 2
            game_ended = check_victory()
            if game_ended:
                return

            # Update the enemy's health after losing
            room.enemy['health'] = max(0, room.enemy['health'] - fight_result['enemy_damage'])

            # Update the player's stats
            update_stats()
                
    # Function to sell an item and update the player's money and stats
    def sell_item(item_type, item):
        # Remove the item from the player's inventory based on its type
        if item_type == "weapon":
            player.inventory["weapons"].remove(item)
        elif item_type == "key":
            player.inventory["keys"].remove(item)
        elif item_type == "armour":
            player.inventory["armours"].remove(item)

        # Increase player's money and update stats
        player.money += item["price"]
        update_stats()
        messagebox.showinfo("Sold", f"You sold {item['name']} for {item['price']} coins")

            # Function to handle the player's interaction with the shop
    def enter_shop():
        # Create a new window for the shop
        shop_window = tk.Toplevel(root)
        shop_window.title("Shop")

        # Display shop information
        tk.Label(shop_window, text="Shop", font=("Arial", 24)).pack(pady=10)
        tk.Label(shop_window, text=shop.description).pack(pady=10)

        # Function to buy a weapon
        def buy_weapon(weapon):
            # Check if player has enough money and update their inventory and stats
            if player.money >= weapon['price']:
                player.money -= weapon['price']
                player.inventory['weapons'].append(weapon)
                update_stats()
                messagebox.showinfo("Purchased", f"You bought {weapon['name']} for {weapon['price']} coins")
            else:
                messagebox.showinfo("Not enough money", "You don't have enough money to buy this weapon")

        # Create buttons for each weapon in the shop
        for weapon in shop.weapons:
            weapon_button = tk.Button(shop_window, text=f"{weapon['name']} ({weapon['damage']} dmg) - {weapon['price']} coins",
                                    command=lambda w=weapon: buy_weapon(w))
            weapon_button.pack(pady=2)
