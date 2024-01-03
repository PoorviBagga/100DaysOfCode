treasure_image = '''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''
print(treasure_image)
first_choice = input('''Welcome to Treasure Island.\nYou're at a cross road. Where do you want to go? Type "left" or "right' ''')
if first_choice != 'left':
    print("You fell into a hole. Game Over.")
else:
    second_choice = input('''You're in front of a river. What do you want to do? Type "swim" or "wait' ''')
    if second_choice != 'wait':
        print("You were attacked by trout.\nGame Over.")
    else:
        third_choice = input('''You're in front of a door. Where do you want to go? Type "red" , "blue" or "yellow' ''')
        if third_choice == 'red':
            print("You were burned by fire\nGame Over.")
        elif third_choice == 'blue':
            print("You were eaten by beasts.\n Game Over.")
        elif third_choice == 'yellow':
            print("Yaaay\nYou win!")
        else:
            print("Game Over.")

            
    
        
