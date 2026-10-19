# rock paper scissor game
import random

# get input from the user and a random input from comp
item = ["Rock","Paper","Scissor"]
user_Choice = input("enter user choice = Rock, Paper, Scissor= ")
comp_choice = random.choice(item)

# show the computer choice in output
print(f"user choice = {user_Choice}, computer choice = {comp_choice}")

# lets write our game logic
if user_Choice == "Rock":
    if comp_choice == "Rock":
        print("Tie, Rock cancel each other")
    elif comp_choice == "Paper":
        print("Loose, paper covers rock")
    else:
        print("Win, rock crush the scissor")   

elif user_Choice == "Paper":
    if comp_choice == "Rock":
        print("Win, paper covers rock")
    elif comp_choice == "Paper":
        print("Tie, paper cancel each other")
    else:
        print("Loose, scissor cuts the paper")
        
elif user_Choice == "Scissor":
    if comp_choice == "Rock":
        print("Loose, rock crush the scissor")
    elif comp_choice == "Paper":
        print("Win, scissor cuts the paper")
    else:
        print("Tie, scissor cancel each other")

        
        
       
