# Show all these information on GUI
name: ask from the user
money: initialise random 50-310
health: initialise 100
point: initialise 0

# Show the following buttons on GUI
show inventory
shop
room 1
room 2
room 3
room 4

# In shop, you can buy and sell stuff

# In rooms:
you face an enemy:
	if win ---> collect items in the room 
	if loose ---> loose -2 points and leave the room (update the enemy health)
Delete armour if you have one
Delete the weapon you have used

Check points at each stage:
	if points >= 10 ---> win the game
	if points < 0 ---> lost the game
