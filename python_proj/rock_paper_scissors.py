import random

user_wins = 0
pc_wins = 0
draws = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type: Rock/Paper/Scissors or Q to quit: \n").lower()
    #print(end="\n")
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    #0 - Rock, 1 - Paper, 2 - Scissors
    pc_pick = options[random_number]
    print("Computer chose: ", pc_pick + ".")
    
    if user_input == "rock" and pc_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "paper" and pc_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and pc_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == pc_pick:
        print("Draw!")
        draws += 0
        continue
    else:
        print("You lost!")
        pc_wins += 1
        

print("You won ", user_wins, " times.")
print("The computer won ", pc_wins, " times.")
print("Draws: ", draws)
print("Goodbye")