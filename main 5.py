#Logical operaters

a= True and True or False
print(a)

'''if (a == 13 and a == 21):
    print("Statement is True")
else:
    print("Statement is False")'''

# Treasure Island!!!!!
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treause Island\nYour mission is to find the treasure.")
first = input("Would you like to go left or right")
if first == ("left"):
    print("You made it to the other area!")
    swim = input("There is a river ahead. Would you like to swim or wait")
    if swim == ("wait"):
        print("A boat has arrived to the island!")
        print("You have arrived to another island.")
        doors = input("You see 3 doors ahead. Pick the color. Red, Green, Yellow")
        if doors == ("green"):
            print("You have picked the right door!")
        elif doors == ("red"):
            print("You got caught in a bear trap! You fail.")
        elif doors == ("yellow"):
            print("You got caught and burned by fire! You fail.")
        else:
            print("invalid choice")

    else:
        print("You drowned in the water. You fail!")
else:
    print("You failed.")