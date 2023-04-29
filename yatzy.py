from random import randint
from time import sleep


def ones():
    score = []
    userInput = input("Roll the dice by pressing \"r\" and \"ENTER\", end turn by pressing \"e\" or quit by pressing \"q\" and \"ENTER\": ")

    if userInput == "r":

        # Initial roll
        spinner(rounds=1)
        rolled = [(randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6))]
        print(rolled)
        collectables = [num1 for num1 in str(rolled) if "1" in num1]
        print(collectables)
        if len(collectables) != 0:
            score.extend(collectables)
        print("Score: ", score)

        if len(score) != 5:
            userInput = input("Second try! Roll the dice with \"r\" or press \"e\" to end turn: ")

            if userInput == "r":
                # Second roll
                if len(score) == 0:
                    spinner(rounds=1)
                    rolled = [(randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6))]
                    print("Rolled: ", rolled)
                    collectables = [num1 for num1 in str(rolled) if "1" in num1]
                    print(collectables)
                    if len(collectables) != 0:
                        score.extend(collectables)
                    print("Score: ", score)
            
                elif len(score) == 1:
                    spinner(rounds=1)
                    rolled = [(randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6))]
                    print("Rolled: ", rolled)
                    collectables = [num1 for num1 in str(rolled) if "1" in num1]
                    print(collectables)
                    if len(collectables) != 0:
                        score.extend(collectables)
                    print("Score: ", score)

                elif len(score) == 2:
                    spinner(rounds=1)
                    rolled = [(randint(1,6)), (randint(1,6)), (randint(1,6))]
                    print("Rolled: ", rolled)
                    collectables = [num1 for num1 in str(rolled) if "1" in num1]
                    print(collectables)
                    if len(collectables) != 0:
                        score.extend(collectables)
                    print("Score: ", score)

                elif len(score) == 3:
                    spinner(rounds=1)
                    rolled = [(randint(1,6)), (randint(1,6))]
                    print("Rolled: ", rolled)
                    collectables = [num1 for num1 in str(rolled) if "1" in num1]
                    print(collectables)
                    if len(collectables) != 0:
                        score.extend(collectables)
                    print("Score: ", score)

                elif len(score) == 4:
                    spinner(rounds=1)
                    rolled = [(randint(1,6))]
                    print("Rolled: ", rolled)
                    collectables = [num1 for num1 in str(rolled) if "1" in num1]
                    print(collectables)
                    if len(collectables) != 0:
                        score.extend(collectables)
                    print("Score: ", score)

            elif userInput == "e":
                # TODO: add ending turn
                print("TURN ENDED")

            if len(score) != 5:
                userInput = input("Third try, put everything to it! Roll the dice with \"r\" or press \"e\" to end turn: ")

                if userInput == "r":
                # Third roll
                    if len(score) == 0:
                        spinner(rounds=1)
                        rolled = [(randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6))]
                        print("Rolled: ", rolled)
                        collectables = [num1 for num1 in str(rolled) if "1" in num1]
                        print(collectables)
                        if len(collectables) != 0:
                            score.extend(collectables)
                        print("Score: ", score)
            
                    elif len(score) == 1:
                        spinner(rounds=1)
                        rolled = [(randint(1,6)), (randint(1,6)), (randint(1,6)), (randint(1,6))]
                        print("Rolled: ", rolled)
                        collectables = [num1 for num1 in str(rolled) if "1" in num1]
                        print(collectables)
                        if len(collectables) != 0:
                            score.extend(collectables)
                        print("Score: ", score)

                    elif len(score) == 2:
                        spinner(rounds=1)
                        rolled = [(randint(1,6)), (randint(1,6)), (randint(1,6))]
                        print("Rolled: ", rolled)
                        collectables = [num1 for num1 in str(rolled) if "1" in num1]
                        print(collectables)
                        if len(collectables) != 0:
                            score.extend(collectables)
                        print("Score: ", score)

                    elif len(score) == 3:
                        spinner(rounds=1)
                        rolled = [(randint(1,6)), (randint(1,6))]
                        print("Rolled: ", rolled)
                        collectables = [num1 for num1 in str(rolled) if "1" in num1]
                        print(collectables)
                        if len(collectables) != 0:
                            score.extend(collectables)
                        print("Score: ", score)

                    elif len(score) == 4:
                        spinner(rounds=1)
                        rolled = [(randint(1,6))]
                        print("Rolled: ", rolled)
                        collectables = [num1 for num1 in str(rolled) if "1" in num1]
                        print(collectables)
                        if len(collectables) != 0:
                            score.extend(collectables)
                        print("Score: ", score)

                elif userInput == "e":
                    # TODO: add ending turn
                    print("TURN ENDED")

    elif userInput == "e":
        # TODO: add functionality
        print("Turn ended!")
    
    elif userInput == "q":
        # TODO: go back to selection
        print("END")

    else:
        print("Please press \"r\" \"e\" or \"q\"")
        ones()


# TODO: change this to use it from dice
def spinner(rounds):
    if rounds == 1:
        for x in range(1):
                for frame in r"-\|/-\|/":
                    print("\b", frame, sep="", end="\r", flush=True)
                    sleep(0.2)

    elif rounds == 3:
        for x in range(3):
                for frame in r"-\|/-\|/":
                    print("\b", frame, sep="", end="\r", flush=True)
                    sleep(0.2)


ones()

