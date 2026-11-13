import random

game = ["Rock", "Paper", "Scissor"]
game = random.choice(game)

while True:
    user_choice = input("Rock or Paper or Scissor (r/p/s) ?")
    if user_choice.lower() == "r" and game == "Rock":
        print("Equal , one more time")
    elif user_choice.lower() == "r" and game == "Paper":
        print("Computer won")
        break
    elif user_choice.lower() == "r" and game == "Scissor":
        print("You won")
        break
    elif user_choice.lower() == "p" and game == "Paper":
        print("Equal , one more time")
    elif user_choice.lower() == "p" and game == "Rock":
        print("You won")
        break
    elif user_choice.lower() == "p" and game == "Scissor":
        print("Computer won")
        break
    elif user_choice.lower() == "s" and game == "Scissor":
        print("Equal , one more time")
    elif user_choice.lower() == "s" and game == "Rock":
        print("Computer won")
        break
    elif user_choice.lower() == "s" and game == "Paper":
        print("You won")
        break
    else:
        print("enter r or p or s")
