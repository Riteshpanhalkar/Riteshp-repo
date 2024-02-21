import random

def get_user_choice():
    user_choice = input("Choose: paper, rock, or scissors:").lower()
    while user_choice not in ["paper","rock","scissors"]:
        print("Invalid choice. Plese choose: paper, rock, or scissors.")
        user_choice = input("Choose: paper, rock, or scissors:").lower()
    return user_choice
    
def get_computer_choice():
    return random.choice(["paper", "rock", "scissors"])
    
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!!!"
    elif(
        (user_choice == "paper" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "rock") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "you are winning!!"
    else:
        return "Computer winning!!"
        
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You choose {user_choice}")
        print(f"Computer choose {computer_choice}")
        
        result = determine_winner(user_choice,computer_choice)
        print(result)
        
        if result == "You win!!":
            user_score += 1
        elif result == "Computer_choice":
            computer_choice += 1
            
        play_again = input("Do you want to play game again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"Final scores - you: {user_score}, Computer: {computer_score}")
    
    if name == "main":
        print("Welcome to rock-paper-scissors!!!!!")
play_game()
