import random
def main():
    print('''
1 - Play
2 - Show score
''')
    choice = int(input('Enter number of choice: '))
    if choice == 1:
        play()

    elif choice == 2:
        show_score()

    else: 
        print()

def win_ii():
    score['ii'] += 1
    print("Win ii")

def win_human():
    score['human'] += 1
    print("Win human")

def rules(choice):
    vars = [1,2,3]
    ii = random.choice(vars)
    if ii == choice:
        print("Draw")
    if ii == 1 and choice == 2:
        win_ii()

    if ii == 1 and choice == 3:
        win_human()

    if ii == 2 and choice == 1:
        win_human()

    if ii == 2 and choice == 3:
        win_ii()

    if ii == 3 and choice == 1:
        win_ii()
        
    if ii == 3 and choice == 2:
        win_human()
    

def play():
    print('''
1 - Rock
2 - Paper
3 - Scissors
''')
    choice = int(input('Enter number of choice: '))
    rules(choice)
    main()

def show_score():
    text = 'You : Bot ' + '\n' + str(score['human']) + ' : ' + str(score['ii'])
    print(text)
    main()

if __name__ == "__main__":
    score = {'human' : 0, 'ii' : 0}
    main()