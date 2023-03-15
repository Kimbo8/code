import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    line = sys.stdin.readline().rstrip()
    
    if line == "blue":
        print("No colors need to be mixed to make blue")
    if line == "yellow":
        print("No colors need to be mixed to make yellow")
    if line == "red":
        print("No colors need to be mixed to make red")
        
    if line == "violet" or line == "blue-violet" or line == "red-violet":
        print("In order to make "+ line+ ", blue and red must be mixed")
    if line == "blue-green" or line == "green" or line == "yellow-green":
        print("In order to make "+ line+ ", blue and yellow must be mixed")
    if line == "orange" or line == "red-orange" or line == "yellow-orange":
        print("In order to make "+ line+ ", red and yellow must be mixed")
