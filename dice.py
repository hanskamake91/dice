from random import randint
from time import sleep
import logging

d1 =    ["---------",
         "|       |",
         "|   o   |",
         "|       |",
         "---------"]

d2 =    ["---------",
         "|       |",
         "|  o o  |",
         "|       |",
         "---------"]

d3 =    ["---------",
         "| o     |",
         "|   o   |",
         "|     o |",
         "---------"]

d4 =    ["---------",
         "| o   o |",
         "|       |",
         "| o   o |",
         "---------"]

d5 =    ["---------",
         "| o   o |",
         "|   o   |",
         "| o   o |",
         "---------"]

d6 =    ["---------",
         "| o   o |",
         "| o   o |",
         "| o   o |",
         "---------"]

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename="dice.log", encoding="utf-8", level=logging.INFO)


def oneDice():
    userAction = input("\n" + "Roll the dice by pressing \"r\" and \"ENTER\", go back to selection by pressing \"b\" or quit by pressing \"q\" and \"ENTER\": ")
    
    if userAction == "r":
        logging.info("Rolling dice")
        num = (randint(1,6))
        if num == 1:
            dice = d1

        elif num == 2:
            dice = d2

        elif num == 3:
            dice = d3

        elif num == 4:
            dice = d4

        elif num == 5:
            dice = d5
            
        elif num == 6:
            dice = d6
            
        spinner(rounds=1)

        print("\n".join(list(map(str,dice))))
        logging.info("Dice rolled: ""%s" % (num))
        oneDice()

    elif userAction == "b":
        logging.info("Back to selection")
        selection()    

    elif userAction == "q":
        print("\n" + "Thanks for using DICE!")
        spinner(rounds=3)
        print("END")
        logging.info("DICE shut down")
    
    else:
        print("Please press \"r\", \"b\" or \"q\"!")
        logging.info("Invalid input")
        oneDice()


def twoDice():
    userInput = input("\n" + "Roll the dice by pressing \"r\" and \"ENTER\", go back to selection by pressing \"b\" or quit by pressing \"q\" and \"ENTER\": ")

    if userInput == "r":
        logging.info("Rolling dice")
        num1 = (randint(1,6))
        num2 = (randint(1,6))
        
        if num1 == 1:
            dice1 = d1

        elif num1 == 2:
            dice1 = d2

        elif num1 == 3:
            dice1 = d3

        elif num1 == 4:
            dice1 = d4

        elif num1 == 5:
            dice1 = d5
            
        elif num1 == 6:
            dice1 = d6
            
        spinner(rounds=1)

        if num2 == 1:
            dice2 = d1

        elif num2 == 2:
            dice2 = d2

        elif num2 == 3:
            dice2 = d3

        elif num2 == 4:
            dice2 = d4

        elif num2 == 5:
            dice2 = d5

        elif num2 == 6:
            dice2 = d6

        print("\n".join(list(map(str,dice1))) + "\n" + "\n".join(list(map(str,dice2))))
        logging.info("Dice rolled: ""%s - %s" % (num1, num2))
        twoDice()

    elif userInput == "b":
        logging.info("Back to selection")
        selection()    

    elif userInput == "q":
        print("\n" + "Thanks for using DICE!")
        spinner(rounds=3)
        print("END")
        logging.info("DICE shut down")
    
    else:
        print("Please press \"r\", \"b\" or \"q\"!")
        logging.info("Invalid input")
        twoDice()


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


def selection():
    userSelection = input("\n" + "1. Roll one die" + "\n" + "2. Roll two dice" + "\n" + "Q Quit" + "\n" + "Please select: ")

    if userSelection == "1":
        logging.info("One dice selected")
        oneDice()
    
    elif userSelection == "2":
        logging.info("Two dice selected")
        twoDice()

    elif userSelection == "q" or "Q":
        print("\n" + "Thanks for using DICE!")
        spinner(rounds=3)
        print("END")
        logging.info("DICE shut down")
        
    else:
        selection()


def main():
    logging.info("DICE started")
    print("Welcome to the dice!".upper())
    print("You can select to roll just one die or to roll two dice.")
    selection()


if __name__ == "__main__":
    main()

