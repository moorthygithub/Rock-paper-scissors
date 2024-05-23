#Rock paper scissor

import random
def inputfn():
    moves=["rock","paper","scissors"]
    return random.choice(moves)
    
def winner(player,computer):
    if player==computer:
        return "Tie"
    elif (player=='rock' and computer=='scissors' or player=='paper'and computer=="rock" or player=='scissors'and computer=='paper'):
        return "player wins"
    else:
        return "computer wins"
def main():
    print("Welcome to Rock-paper-scissors  Type quit if you need to quit the play" )

    while True:
        player=input("Welcome to Rock-paper-scissors Enter a input").lower()
        if player=='quit':
            print("Thanks for playing")
            break
        if player not in ['rock','paper','scissors']:
            print("enter a valid move like Rock Paper scissors")
            continue
        computermove=inputfn()
        print(f"compter move is :{computermove}")
        Result=winner(player,computermove)
        print(f"final winnner is :{Result}")

main()