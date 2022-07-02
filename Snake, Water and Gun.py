import random
i = 0
comp = []
user = []
while i <= 10:
    l1 = ['Snake', 'Water', 'Gun']
    choice = random.choice(l1)
    a = input('Choose your character:''\n'
              '1.S for Snake''\n'
              '2. W for water''\n'
              '3. G for gun''\n')
    # choosing a component
    if a == 'S':
        if choice == 'Water':
            user.append('Win')
            print('User Wins')
            print('Computer\'s choice was', choice)
        elif choice == 'Snake':
            print('Tie')
            print('Computer\'s choice was', choice)
        elif choice == 'Gun':
            comp.append('Win')
            print('Computer Wins')
            print('Computer\'s choice was', choice)
    elif a == 'W':
        if choice == 'Water':
            print('Tie')
            print('Computer\'s choice was', choice)
        elif choice == 'Snake':
            comp.append('Win')
            print('Computer wins')
            print('Computer\'s choice was', choice)
        elif choice == 'Gun':
            user.append('Win')
            print('User wins')
            print('Computer\'s choice was', choice)
    elif a == 'G':
        if choice == 'Water':
            comp.append('Win')
            print('Computer wins')
            print('Computer\'s choice was', choice)
        elif choice == 'Snake':
            user.append('Win')
            print('User wins')
            print('Computer\'s choice was', choice)
        elif choice == 'Gun':
            print('Tie')
            print('Computer\'s choice was', choice)
    else:
        print('Wrong Input')
    i += 1
# printing user's and computer's choices
print('User\'s win', user)
print('Computer\'s win', comp)
# shows the final results
if len(user) > len(comp):
    print('CONGRATULATIONS!!! YOU WON THE GAME')
elif len(user) == len(comp):
    print('TIE!!!')
else:
    print('COMPUTER WON THE GAME. BETTER LUCK NEXT TIME')
