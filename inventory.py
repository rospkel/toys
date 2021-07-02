import random

x = 1
inventory = []
ground = []
while x:
    s = input().lower()
    if s == "check inventory":
        print(inventory)
    elif s == "check ground":
        print(ground)
    elif s == "sort inventory":
        inventory.sort()
        print(inventory)
    elif s == "stop":
        break
    elif "pick up " in s:
        if s == "pick up something":
            if ground != []:
                something = random.choice(ground)
                ground.remove(something)
                inventory.append(something)
                print("PICKED UP "+something.upper())
            else:
                print("GROUND IS BARE")
        elif s[8:] in ground:
            inventory.append(s[8:])
            ground.remove(s[8:])
            print("PICKED UP "+s[8:].upper())
        else:
            print(s[8:].upper()+" NOT ON GROUND")
    elif "put down " in s:
        if s == "put down something":
            if inventory != []:
                something = random.choice(inventory)
                inventory.remove(something)
                ground.append(something)
                print("PUT DOWN "+something.upper())
            else:
                print("INVENTORY IS EMPTY")
        elif s[9:] in inventory:
            inventory.remove(s[9:])
            ground.append(s[9:])
            print("PUT DOWN "+s[9:].upper())
        else:
            print(s[9:].upper()+" IS NOT IN INVENTORY")
    elif "spawn " in s:
        ground.append(s[6:])
        print("SPAWNED "+s[6:].upper())
