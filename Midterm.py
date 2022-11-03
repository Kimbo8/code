#1
#cookies = int(input("how many cookies do you have?"))

#if cookies< 3:
   # print("you dont have enough cookies sorry bud")
#elif cookies <= 10:
  #  print("you have a good amount i guess.")
#else:
    #print("you have too many cookies! but really can anyone ever have tooo much cookies? Either way you should give me one")
#--------------------------------------------------------------------------------------
#2
#character = input("are you a jedi or a sith: ")
#if character == 'jedi':
    #print("you get a green light saber")
#elif character == 'sith':
#    print("you get a red lighsaber")
#else:
  #  print("you get a soggy breadstick")
#---------------------------------------------------------------
#3
#print("pollo loop")
#for pollo in range(4,42,2):
  #  print(pollo, end = " ")
#--------------------------------------
#4
print("da while loop")
num = 100
while num >= 50:
    print(num)
    num-=10
#-----------------------------------------
#5
quit = False
while quit == False:
   word =input("enter something")
   while word != 'orange':
       word = input("knock knock, whos there.....banana!")
   else:
       print("orange you glad i didnt say banana?!")
   quit=True
#---------------------------------------------------
#6
def mult(a, f, s):
    return a*f*s

print(mult(2, 3, 4))

#--------------------------------------------------------
#7
def rootBeer(x):
    while x > 0:
        print(x, "bottles of rootbeer on the wall")
        x-=1
num = int(input("give me a number"))
rootBeer(num)
    

    
