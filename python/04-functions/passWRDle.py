from operator import xor
import random
import hashlib
from traceback import print_tb
import os
# easy implementation of the game wordle but random passwords

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    print("Welcome to PassWRDle!")
    print()
    print("Meanings of the outputs:")
    print("\t*:\tright character, right place")
    print("\t+:\tright character, wrong place")
    print("\t-:\twrong character")
    print()
    print()
def clearConsoleExit():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def printMenu(menutype):
    if menutype == 'p': #password
        print("Please select your desired generation option::")
        print("\tc:\tcustom password")
        print("\tr:\trandom password")
    elif menutype == 'h': #hardness    
        print("Please select your desired level:")
        print("\tz:\tzen,\t\tno life limit")
        print("\te:\teasy,\t\t20 lives")
        print("\tm:\tmedium,\t\t15 lives")
        print("\th:\thard,\t\t10 lives")
        print("\ti:\timpossible,\t6 lives")
        print("\tc:\tcustom")
    elif menutype == "r":
        print("Meanings of the outputs:")
        print("\t*:\tright character, right place")
        print("\t+:\tright character, wrong place")
        print("\t-:\twrong character")
        input("press any key to continue...")
        clearConsole()
    elif menutype == 'l':
        print("Please select your desired character longitude:")
        print("\ts:\tshort:\t5 digits")
        print("\tm:\tmedium:\t10 digits")
        print("\tl:\tlong:\t20 digits")
        print("\tf:\tfull:\t40 digits")
    elif menutype == "w":
        print("Please select the desired game generator:")
        print("\tp:\tpreset:\n\t\t>randomly generated password \n\t\t>with hard (10 lives) hardness \n\t\t>and classical 5 character SHA1 texture")
        print("\tc:\tcustom:\n\t\t>you will be choosing the settings")
        
def shorter(passwd):
    r = ""
    for i in range(len(passwd)//2):
        j = random.randint(0,1)
        if j == 0:
            r+=passwd[i]
        else:
            r+=passwd[len(passwd)-1-i]
    return r

def createGame():
    randomP = 'r'
    zen = 'z'
    easy = 'e'
    medium = 'm'
    hard = 'h'
    impossible = 'i'
    password = 'p'
    preset = 'p'
    hardness = 'h'
    custom = 'c'
    welcome = 'w'
    long = 'l'
    short = 's'
    full = 'f'

    printMenu(welcome)
    while True:
        command = input("\t>")
        if command == preset:
            password = ""
            for i in range(8):
                j = random.randint(0,9)
                password+= str(j)
            lives = 10
            charlen = 5
            clearConsole()
            break
        elif command == custom:
            clearConsole()
            printMenu(password)
            command = input("\t>")
            while True:
                if command == custom:
                    password = input("Enter a keyword to play PassWRDle with.\n\t>")
                    break
                elif command == randomP:
                    password = ""
                    for i in range(8):
                        j = random.randint(0,9)
                        password+= str(j)
                    break
                command = input("The input is wrong, please try again.\n\t>")
            clearConsole()
            printMenu(hardness)
            while True:
                command = input("\t>")
                if command == zen:
                    lives = -1
                    break
                elif command == easy:
                    lives = 20
                    break
                elif command == medium:
                    lives = 15
                    break
                elif command == hard:
                    lives = 10
                    break
                elif command == impossible:
                    lives = 6
                    break
                elif command == custom:
                    while True:
                        lives = int(input("How many lives would you like to have?\n\t>"))
                        if lives < 1:
                            lives = int(input("The numbers lower than 1 are not permitted. Please enter a valid number.\n\t>"))
                        else:
                            clearConsole()
                            break
                    break
                command = input("The input is wrong, please try again.\n\t>")
            clearConsole()
            printMenu(long)    
            while True:
                command = input("\t>")
                if command == short:
                    charlen = 5
                    break
                elif command == medium:
                    charlen = 10
                    break
                elif command == long:
                    charlen = 20
                    break
                elif command == full:
                    charlen = 40
                    break
                else:
                    command = input("The input is wrong, please try again.\n\t>")
            break

        else:
            command = input("The input is wrong, please try again.\n\t>")
            

    hashPasswd = str(hashlib.sha1(password.encode()).hexdigest())
    if charlen < 40:
        hashPasswd = shorter(hashPasswd)
        if charlen < 20:
            hashPasswd = shorter(hashPasswd)
            if charlen <10:
                hashPasswd = shorter(hashPasswd)
                if charlen < 5:
                    hashPasswd = shorter(hashPasswd)
    else:
        for i in range(random.randint(1,5)):
            hashPasswd = str(hashlib.sha1(password.encode()).hexdigest())

    clearConsole()
    print("Here is the final settings:")
    print("\t>Keyword:\t"+password)
    if lives < 0:
        print("\t>Hardness:\tZen (Limitless)")
    elif lives < 10:
        print("\t>Hardness:\tImpossible (6 Guesses)")
    elif lives < 15:
        print("\t>Hardness:\tHard (10 Guesses)")
    elif lives < 20:
        print("\t>Hardness:\tMedium (15 Guesses)")
    else:
        print("\t>Hardness:\tEasy (20 Guesses)")

    if charlen < 10:
        print("\t>Longitude:\tShort")
    elif charlen < 20:
        print("\t>Longitude:\tMedium")
    elif charlen < 40:
        print("\t>Longitude:\tLong")
    else:
        print("\t>Longitude:\tFull")
    input("Press any key to continue...")
    clearConsole()

    return (hashPasswd, lives,charlen,password)

def check(hashPasswd, guess):
    r = ""
    for i in range(len(guess)):
        if hashPasswd.count(guess[i]) > 0:
            if hashPasswd[i] == guess[i]:
                r += "*"
            else :
                r += "+"
        else:
            r+= "-"
    return r

def printallguesses(guesslist):
    for i in guesslist:
        print()
        print("\t"+i[0])
        print("\t"+i[1])
        print("\t"+i[2])
        
        print()

def approx(guess, result):
    r=""
    for i in range(len(result)):
        if result[i] == '*':
            r+=guess[i]
        else:
            r+="?"
    return r

clearConsole()

gameno = 0
points = 0

while True:
    gameno += 1
    clearConsole()
    game = createGame()
    clearConsole()
    
    gamecount = 1
    pointRound = 0
    ach = False
    lives = game[1]
    guesslist = list()
    while lives != 0:
        
        clearConsole()
        
        print("Game Settings:")
        print("\t>Keyword:\t"+game[3])
        if game[1] < 0:
            print("\t>Hardness:\tZen (Limitless)")
        elif game[1] < 10:
            print("\t>Hardness:\tImpossible (6 Guesses)")
        elif game[1] < 15:
            print("\t>Hardness:\tHard (10 Guesses)")
        elif game[1] < 20:
            print("\t>Hardness:\tMedium (15 Guesses)")
        else:
            print("\t>Hardness:\tEasy (20 Guesses)")

        if game[2] < 10:
            print("\t>Longitude:\tShort")
        elif game[2] < 20:
            print("\t>Longitude:\tMedium")
        elif game[2] < 40:
            print("\t>Longitude:\tLong")
        else:
            print("\t>Longitude:\tFull")
        print()
        print("Game is staring now.\nTip 1:\tThe inputs are",len(game[0])," characters long\nTip 2:\tIf you would like to resign press 'q' instead of a guess.\n\tTip 3:\tThe resulting hash is scrambled so that you cannot look it up:)")
        print()
        
        if gamecount > 1:
            print()
        if gamecount > 1:
            printallguesses(guesslist)
        print("Guess no:", gamecount)
        guess = input("\t>")
        if guess == 'q':
            print()
            print("You are quitting? Wow!")
            
            break
        if len(guess) != len(game[0]):
            continue
        result = check(game[0],guess)
        guesslist.append([guess,result,approx(guess,result)])
        print("\t>"+result)

        if result.count("-") == 0 and result.count("+") == 0:
            ach = True
            if game[1] > 0:
                pointRound = 10000*game[2]/game[1]
            else:
                pointRound = 0
                points+=pointRound
            break
        else:
            gamecount += 1
            lives -= 1
            if lives > 0:
                print("\tYou have", lives,"lives left.")
            continue
    
    clearConsole()
    printallguesses(guesslist)

    if ach == False:
        print()
        print("The answer was:\n\t>"+game[0])
    else:
        print("You did it you beautiful mf!")
    
    print()
    print("The points gained for this round is:\t",pointRound)
    print("Your total points in this session is:\t",points)
    print("The number of games you have played is:\t",gameno)
    
    input("Press any key to continue...")
    clearConsole()
    print("Do you want to play again?(y/n)")
    cont = input("\t>")
    while True:
        if cont == 'y' or cont == 'Y':
            c = True
            break
        elif cont == 'n' or cont == 'N':
            c = False
            break
        else:
            print()
            howto = input("The input is wrong, please try again.\n\t>")
    if c == False:
        break
    elif c == True:
        clearConsole()
        continue
input("Hope to see ya again!\n Press any key to quit...")
clearConsoleExit()



    