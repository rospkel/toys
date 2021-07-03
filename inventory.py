import random
import time

# This is a game loop for an arbitrary inventory.
# This interface is highly adaptable to a variety of narrative devices.
# More commands and higher levels of interactivity may come in a later version.


inventory = []
ground = []
command_list = ("CHECK INVENTORY", "CHECK GROUND", "SORT INVENTORY", "STOP", "PICK UP (X)", "DROP (X)", "SPAWN (X)", "DESTROY (X)", "EAT (X)")
while True:
    s = input().lower()
    if s == "check inventory":
        print(inventory)
    elif s == "check ground":
        print(ground)
        if ground.count('poop') > 2:
            print("THE GROUND IS COVERED IN POOP")
    elif s == "sort inventory":
        inventory.sort()
        print(inventory)
    elif s == "stop":
        break
    elif s.startswith("pick up "):
        if s == "pick up something":
            if ground != []:
                something = random.choice(ground)
                ground.remove(something)
                inventory.append(something)
                print("PICKED UP "+something.upper())
            else:
                print("GROUND IS BARE")
        elif s == "pick up everything":
            inventory += ground
            ground = []
            print("PICKED UP EVERYTHING")
        elif s[8:] in ground:
            inventory.append(s[8:])
            ground.remove(s[8:])
            print("PICKED UP "+s[8:].upper())
        else:
            print(s[8:].upper()+" NOT ON GROUND")
    elif s.startswith("drop "):
        if s == "drop something":
            if inventory != []:
                something = random.choice(inventory)
                inventory.remove(something)
                ground.append(something)
                print("DROPPED "+something.upper())
            else:
                print("INVENTORY IS EMPTY")
        elif s == "drop everything":
            ground += inventory
            inventory = []
            print("DROPPED EVERYTHING")
        elif s[5:] in inventory:
            inventory.remove(s[5:])
            ground.append(s[5:])
            print("DROPPED "+s[5:].upper())
        else:
            print(s[5:].upper()+" NOT IN INVENTORY")
    elif s.startswith("spawn "):
        if s == "spawn something" or s == "spawn everything":
            print(f"YOU CAN'T JUST {s.upper()}")
        else:
            ground.append(s[6:])
            print("SPAWNED "+s[6:].upper())
    elif s.startswith("destroy "):
        if s == "destroy something":
            if ground != []:
                something = random.choice(ground)
                ground.remove(something)
                print("DESTROYED "+something.upper())
            else:
                print("GROUND IS BARE")
        elif s == "destroy everything":
            ground = []
            print("DESTROYED EVERYTHING")
        elif s[8:] in ground:
            ground.remove(s[8:])
            print("DESTROYED "+s[8:].upper())
        else:
            print(s[8:].upper()+" NOT ON GROUND")
    elif s.startswith("eat "):
        if s == "eat something":
            if inventory != []:
                something = random.choice(inventory)
                inventory.remove(something)
                print("ATE "+something.upper())
                ground.append("poop")
                print("POOPED")
            else:
                print("INVENTORY IS EMPTY")
        elif s == "eat everything":
            n = len(inventory)
            inventory = []
            print("ATE EVERYTHING")
            ground += ['poop']*n
            if n != 0:
                print("POOPED")
            if n >= 2:
                print("A LOT")
        elif s[4:] in inventory:
            inventory.remove(s[4:])
            print("ATE "+s[4:].upper())
            ground.append("poop")
            print("POOPED")
        else:
            print(s[4:].upper()+" NOT IN INVENTORY")
    else:
        print(f"COMMAND NOT UNDERSTOOD. YOU CAN: {command_list}")
