import random
def gameWin(Computer,You):
    if Computer==You:
        return None
    elif Computer=='s':
        if You=='w':
            return False
        elif You=='g':
            return True
    elif Computer=='w':
        if You=='g':
            return False
        elif You=='s':
            return True
    elif Computer=='g':
        if You=='s':
            return False
        if You=='w':
            return True
print("Computer Turn: Snake(s) Water(w) or Gun(g)\n?")
random_No=random.randint(1,3)
if random_No==1:
    Computer='s'
elif random_No==2:
    Computer='w'
elif random_No==3:
    Computer='g'
You=input("Your Turn: Snake(s) Water(w) Gun(g)?\n")
a=gameWin(Computer,You)
print(f"Computer chose: {Computer}")
print(f"You chose: {You}")
if a==None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")