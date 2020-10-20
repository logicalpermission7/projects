import random



cp = ["1-rock", "2-paper", '3-scissors']
players_answer = ""
players_points = 0
cp_points = 0
turns = 0


def getPlayersChoice():
    print('\n')
    players_points = 0
    cp_points = 0
    turns = 0
    game = open("/Users/ironman/Desktop/elvisgame.txt", "r")
    print(game.read())
    game.close()
    print('\n')
    while True:
        try:
            print("Players Score: " + str(players_points))
            print("Computers Score: " + str(cp_points) + "\n")
            cp_choice = random.choice(cp)
            if players_points == 5 or cp_points == 5:
                print("------------------------------------------------END OF GAME \n")
                players_points = 0  # resets the point after match ends.
                cp_points = 0
            players_answer = int(input("Enter 1 for ROCK, 2 for PAPER or 3 for SCISSORS: "))
        except ValueError:
            print("invalid entry, only 1-3 accepted")
            continue
        else:
            if players_answer != 1 and players_answer != 2 and players_answer != 3:
                getPlayersChoice()
            elif players_answer == 1 and cp_choice == "2-paper":
                print("The CP choice " + cp_choice)
                print("CP Wins!, PAPER beats ROCK\n")
                cp_points += 1
                turns += 1
            elif players_answer == 1 and cp_choice == "3-scissors":
                print("The CP choice " + cp_choice)
                print("Player Wins, ROCK beats SCISSORS\n")
                players_points += 1
                turns += 1
            elif players_answer == 2 and cp_choice == "1-rock":
                print("The CP choice " + cp_choice)
                print("Player Wins, PAPER beats ROCK\n")
                players_points += 1
                turns += 1
            elif players_answer == 2 and cp_choice == "3-scissors":
                print("The CP choice " + cp_choice)
                print("CP Wins, SCISSORS beats PAPER\n")
                turns += 1
                cp_points += 1
            elif players_answer == 3 and cp_choice == "1-rock":
                print("The CP choice " + cp_choice)
                print("CP Wins, ROCK beats SCISSORS\n")
                turns += 1
                cp_points += 1
            elif players_answer == 3 and cp_choice == "2-paper":
                print("The CP choice " + cp_choice)
                print("Player Wins, SCISSORS beats PAPER\n")
                players_points += 1
                turns += 1
            else:
                print("The CP choice " + cp_choice)
                print("ITS A DRAW\n")


getPlayersChoice()




