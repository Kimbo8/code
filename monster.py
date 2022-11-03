import random
def monster(biome):
    num = random.randrange(0,100)
    if biome == "dungeon":
        if num < 20: #20 percent chance
            print("a xombie is atacking you!")
        elif num < 50: # 30 percent chance
            print("a skeleton appears!")
        elif num < 90: #40 percent chance
            print("a spider bites you!")
        else: #10 percent chance
            print("a witch threw a potion at you")
    elif biome == "desert":
        if num < 40: #40 percent chance
            print("a husk is atacking you!")
        elif num < 60: # 20 percent chance
            print("a skeleton appears!")
        elif num < 80: #20 percent chance
            print("a spider bites you!")
        else: #20 percent chance
            print("a witch threw a potion at you")
    elif biome == "forest":
        if num < 25: #25 percent chance
            print("a rabid dog is atacking you!")
        elif num < 75: #50 percent chance
            print("a jaguar appears!")
        elif num < 85: #10 percent chance
            print("a vampire bites you!")
        else: #15 percent chance
            print("a bigfoot threw you!")


inventory = ["wood sword"]
room = 1
doExit = False
while doExit == False:
    print("your inventory:", end = "")
    print(inventory)
    if room == 1:
        print("You are in room 1. You can go 'n'.")
        choice = input()
        print("you got a health potion")
        inventory.append("health potion")
        if choice == 'n':
            room = 2
        else:
            print("no an option dummy!")
    if room == 2:
        monster("forest")
        print ("You are in room 2 you can go 's' or 'e', There is a rug")
        if choice == "rug" or choice == "look under rug":
            print("you found a key")
            inventory.append("key")
        choice = input()
        if choice == 's':
            room = 1
        elif choice == 'e':
            room = 3
        else:
            print("not an option, dummy")
    if room == 3:
      monster("desert")
      print("you are in room 3 you can go 'w' or 's' ")
      choice = input()
      if choice == 's':
          key = False
          for i in range(len(inventory)):
            if inventory [i] == "key":
                key = True
          if key == True:
              print("you open the door with the key")
              room = 4
          else:
              print("the door is locked")
      elif choice == 'w':
        room = 2
      else:
        print("that door leads to the emptiness of the world.")
    if room == 4:
      print("you are in room 4 you can go 'n'")
      monster("dungeon")
      if inventory[0] == 'wood sword':
          print("the monster wasnt affected by your weak sword. you die.")
          doExit = True
      choice = input()
      if choice == 'n':
        room = 3
      else:
        print("this door dont work.")
