#Run on python 3.4.1
#This is a python program to simulate two dies and to print
# a message either if sum of the numbers on the two dies is
# equal to 12 or if the numbers on the two dies are same.

#To generate random numbers
import random

#Get the number of tries from the user
range_input = int(input("How many times you wanna try ?"))
#To check for zero input
while not (range_input):
    range_input = int(input("How many times you wanna try ?"))

for die in range(1,range_input+1):
    print("Throw", die)
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print("die1 = ",die1)
    print("die2 = ",die2)
    if die1+die2 ==12 or die1==die2:
        print("You just won hundred million dollars!")
        break
    if die==range_input:
        print("Sorry, Try next time!")
