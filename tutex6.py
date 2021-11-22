# # snake water gun
# import random
#
# list=["snake","water","gun"]
# chance=10 # n=10
# i=0 #i=0
# comp_chance=0
# user_chance=0
#
# while i<chance: # (i<n)
#     comp = random.choices(list)
#     user = input("snake,gun,water")
#
#     if comp==user:
#         print("tie")
#
#     elif comp=="snake" and  user=="water":
#         comp_chance=comp_chance+1
#         print(f"your guess is {user} and comp guess is {input} ")
#         print("comp wins 1 point")
#         print(f"comp point is {comp} and your point is {user}")
#
#     elif comp == "water" and user == "snake":
#         user_chance = user_chance + 1
#         print(f"your guess is {user} and comp guess is {input} ")
#         print("user wins 1 point")
#         print(f"comp point is {comp} and your point is {user}")
#
#     elif comp == "snake" and user == "gun":
#         user_chance = user_chance + 1
#         print(f"your guess is {user} and comp guess is {input} ")
#         print("user wins 1 point")
#         print(f"comp point is {comp} and your point is {user}")
#
#     elif comp == "gun" and user == "snake":
#         comp_chance = comp_chance + 1
#         print(f"your guess is {user} and comp guess is {input} ")
#         print("comp wins 1 point")
#         print(f"comp point is {comp} and your point is {user}")
#
#     elif comp == "gun" and user == "water":
#         user_chance = user_chance + 1
#         print(f"your guess is {user} and comp guess is {input} ")
#         print("user wins 1 point")
#         print(f"comp point is {comp} and your point is {user}")
#
#     elif comp == "water" and user == "gun":
#         comp_chance = comp_chance + 1
#         print(f"your guess is {user} and comp guess is {input} ")
#         print("comp wins 1 point")
#         print(f"comp point is {comp} and your point is {user}")
#
#     else:
#         print("you have input wrong")
#
#     i=i+1
#     print(f"{chance-i} is left out of chance{chance}")
#
# print("game over")

# Snake water gun

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#










