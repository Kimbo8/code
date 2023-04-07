import sys
import math
import string

#start with reading in the number of lines 
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):#run a for loop with this many cases
    line = sys.stdin.readline()#read each line
    
    chineseZodiac = line.split(" ") # put the line into a list, split up by spaces
    
    for j in range(len(chineseZodiac)):#convert each slor in the list from a string into a number
        chineseZodiac[j] = int(chineseZodiac[j])

if chineseZodiac[j] >= 1984:
    
    #animals = ["Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat","Monkey","Rooster","Dog","Pig"]    
        
    aspect = (chineseZodiac[j] %2)
    
    element = (((chineseZodiac[j] - 4) % 10)/2)

    animal = ((chineseZodiac[j] - 4) % 12)
    
    if element == 0:
       if aspect == 0:
           if animal == 0:
               print(chineseZodiac[j], "Yang", "Wood", "Rat")
           else:
               print(chineseZodiac[j], "Yin", "Wood","Rat")
    elif element == 1:
        if aspect == 0:
            print(chineseZodiac[j], "Yang", "Fire")
        else:
            print(chineseZodiac[j], "Yin", "Fire")
    elif element == 2:
       if aspect == 0:
            print(chineseZodiac[j], "Yang", "Earth")
       else:
            print(chineseZodiac[j], "Yin", "Earth")
    elif element == 3:
        if aspect == 0:
            print(chineseZodiac[j], "Yang","Metal")
        else:
            print(chineseZodiac[j], "Yin", "Metal")
    else:
        if aspect == 0:
            print(chineseZodiac[j], "Yang", "Water")
        else:
            print(chineseZodiac[j], "Yin", "Water")

