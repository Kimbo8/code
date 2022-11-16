import random
people = ['rey','tam', 'axel', 'alex', 'ricardo', 'dulce', 'kim','vanessa', 'caine', 'lalo']
locations = ['cafeteria', 'hallway', 'room 110', "EMT classroom", 'room 212']

def Clue():
    num = random.randrange (0,100)
    slot1 = random.randrange(0,9)
    slot = random.randrange(0,9)
    room = random.randrange(0,4)
    if num < 10:
        print(people[slot1], "got hit eith a waterballoon by", people[slot], "in the", locations[room])
    if num < 30:
        print(people[slot1], "got pied in the face by", people[slot], "in the", locations[room])
    if num < 65:
        print(people[slot1], " ate disgised choclate chip cookies given to them by", people[slot], "in the", locations[room])
    if num < 80:
        print(people[slot1], "got their shoelaces tied together by", people[slot], "in the", locations[room])
    else:
        print(people[slot1], "got turned into a bunny with a raygun by", people[slot], "in the", locations[room])
        

Clue()


