import random

choices = ['rock', 'paper', 'scissors']
emojis = {'rock': '✊', 'paper': '✋', 'scissors': '✌️'}

while True:
    answer = input("Do you want to play Rock Paper Scissors? (y/n): ").strip().lower()

    if answer == 'n':
        print("Thanks for playing! Goodbye.")
        break
    elif answer != 'y':
        print("Invalid input. Please enter y or n.")
        continue

    user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose: {emojis[user_choice]} {user_choice}")
    print(f"Computer chose: {emojis[computer_choice]} {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or          (user_choice == 'paper' and computer_choice == 'rock') or          (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win! 🎉")
    else:
        print("Computer wins! 💻")
