import random

user_wins = 0
computer_wins = 0

def user_options():
    user_choices = input("Choose Rock, Paper or Scissors: ")
    if user_choices in ['Rock', 'rock', 'R', 'r']:
        user_choices = 'r'
    elif user_choices in ['Paper', 'paper', 'P', 'p']:
        user_choices = 'p'
    elif user_choices in ['Scissors', 'scissors', 'S', 's']:
        user_choices = 's'
    else:
        print("Sorry I can't understand, please try again")
        user_options()
    return user_choices

def computer_options():
    computer_choices = random.randint(1,3)
    if computer_choices == 1:
        computer_choices = 'r'
    elif computer_choices == 2:
        computer_choices = 'p'
    else:
        computer_choices = 's'
    return computer_choices

while True:
    user_choices = user_options()
    computer_choices = computer_options()
    if user_choices == 'r':
        if computer_choices == 'r':
            print('Both of You and Computer choose Rock. Match tied\n')
        elif computer_choices == 'p':
            print("You choose rock and Computer Choose Paper. Computer wins!\n")
            computer_wins += 1
        else:
            print("You choose Rock and Computer choose Scissors. You win!\n")
            user_wins += 1

    if user_choices == 'p':
        if computer_choices == 'r':
            print("You choose Paper and Computer Choose Rock. You win!\n")
            user_wins += 1
        elif computer_choices == 'p':
            print("Both of You and Computer choose Paper. Match tied\n")
        else:
            print("You choose Paper and Computer Choose Scissors. Computer wins!\n")
            computer_wins += 1

    if user_choices == 's':
        if computer_choices == 'r':
            print('You choose Scissors and Computer choose Rock. Computer wins')
            computer_wins += 1
        elif computer_choices == 'p':
            print("You choose Scissors and Computer choose Paper. User wins.")
            user_wins += 1
        else:
            print("Both of You and Computer choose Scissors. Match tied")
    
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print("")

    user_choices = input("Do you want to play again: y/n: ")
    if user_choices in ['Yes', 'yes', 'Y', 'y']:
        user_choices = 'y'
        pass
    elif user_choices in ['No', 'no', 'N', 'n']:
        user_choices = 'n'
        break
    else:
        break

        

