approved_players = "Elizabeth Jeffrey Henning Thomas Tommy Jacob"
play = "y"

print("Welcome to the cup game. Please enter your name.")
name = input()
if name.lower() in approved_players.lower():
#win game
    print("Glad to see you, " + name + ".")
    while play == "y":
        print("Please choose a cup from 1-3. Under one of these cups is the winning ball.")
        while input().lower() not in "123cup 1cup 2cup 3":
            print("Simply enter a single number 1-3.")
        print("You won! Play again? y/n")
        play = input()
    print("Thanks for playing.")
#lose game
else:
    print("You lose.")

#I know I commit way too often.
