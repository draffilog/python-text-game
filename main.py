class Player:
    """
    This class represents the player character in the game including their name, money, health, points, and inventory.
    """
    def __init__(self, name, money, health, points):
        self.name = name
        self.money = money
        self.health = health
        self.points = points
        self.inventory = []

class Room:
    """
    This class represents a room in the game, containing a description, enemy, points, items, money, and treasure.
    """

class Item:
    """
    This class represents a generic item in the game that can be used by the player.
    """

class Weapon(Item):
    """
    This class represents a weapon in the game, a subclass of Item, with a name, damage, and price.
    """

class Key(Item):
    """
    This class represents a key in the game, a subclass of Item, with a code (0 or 1) and price.
    """

class Armour(Item):
    """
    This class represents an armour in the game, a subclass of Item, with durability and price.
    """

class HealingPad(Item):
    """
    This class represents a HealingPad in the game, a subclass of Item, which can be bought to increase the player's health by 50.
    """

class Enemy:
    """
    This class represents an enemy in the game including their name damage, and health.
    """

class Game:
    """
    This class represents the main game, which manages the game loop, user interface, and game logic.
    """

class FileManager:
    """
    This class handles reading and writing information from text files.
    """