import random

c=0
while True:
    a=input("Roll the dice? y/n: ").lower()
    if a=='y':
        c+=1
        b=int(input('How many dice you want?: '))
        for i in range(b):
            die=random.randint(1,6)
            print(die,end=" ")
        print()
        
    elif a=='n':
        print('Thanks for playing')
        print(f' You rolled the dice {c} times.')
        break
    else:
        print('Invalid choice')
