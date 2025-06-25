import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for computer."""
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_user_choice():
    """Ask user for their choice and validate it."""
    while True:
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("❗ Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user, computer):
    """Compare user and computer choices to determine the winner."""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print("\n🎉 Welcome to Rock-Paper-Scissors Game!")
    print("--------------------------------------")

    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n🌀 Round {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        print(f"📊 Current Score → You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n🏁 Game Over!")
            print(f"🏆 Final Score → You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🎉 Congratulations! You won the game.")
            elif user_score < computer_score:
                print("😔 Better luck next time. Computer won the game.")
            else:
                print("🤝 It's a draw!")
            break

        round_number += 1

play_game()
