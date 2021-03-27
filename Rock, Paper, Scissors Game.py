computer_choice="rock"
user_choice = input("Do you want a rock,paper,scissor,spock or lizard?\n")
if computer_choice == user_choice:
    print("seri")
elif user_choice == "paper" and "spock" and computer_choice == "rock":
    print("user win")
elif user_choice == "rock" and "spock" and computer_choice == "scissor":
    print("user win")
elif user_choice == "scissor" and "lizard" and computer_choice == "paper":
    print("user win")
elif user_choice == "rock" and "lizard" and computer_choice == "spock":
    print("user win")
elif user_choice == "scissor" and "rock" and computer_choice == "lizard":
    print("user win")
else: 
    print("you lose:( computer win")
