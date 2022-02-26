import random

def createNumber (noofnumbers):
    r = [-1,-1,-1]
    for i in range(noofnumbers):
        a = -1
        while r.count(a) > 0 or (a == 0 and i == 0): #prevent recurring and zero as a 0th element
            a = str(random.randint(0,9))
        r[i] = a
    return r
    
def check (l, g): #number, guess
    r = [0,0] #r(eturn) = right, wrong
    for i in range(len(g)):
        if l.count(g[i]) > 0: 
            if g[i] == l[i]:
                r[0] += 1
            else:
                r[1] +=1
    return r
        

def isHit(guesscondition, numofelement):
    if guesscondition[0] == numofelement:
        return True
    return False

def toString(guesscondition, numofelement):
    r = ""
    if guesscondition[0] == 0 and guesscondition[1] == 0:
        r += '0'*numofelement
    else:
        r += '+'*guesscondition[0] + '-'*guesscondition[1]
    return r

while True:
    #generating the three gidits for our number
    numofelement = 3
    gennum = createNumber(numofelement)
    
    lives = 5

    for r in range(lives):  #[0,8) = 0,1,2,3,4,5,6,7 // range(2,5) --> [2,5) = 2,3,4
        guess = input("Enter your guess for a 3 digit number: ")
        guesscondition = check(gennum, guess)
        achieve = isHit(guesscondition)
        if achieve:
            print("You did it you magnificent mf!!!")
            break
        if r == lives-1:
            print("You failed, co cry in a dark room corner :P")
            break
        print("Your guess is wrong:", toString(guesscondition, numofelement))
        print("You have ", lives-1-r, "lives left.")

    cont = input("if you would like to play again press c, if you would like to quit press q: ")
    if cont == 'q':
        print("byeeeee")
        break
    elif cont == 'c':
        print("allright then...")
