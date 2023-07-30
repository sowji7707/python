#BUILDING A GUESSING GAME

secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('guess: '))
    guess_count+=1
    if guess==secret_number:
        print("you win")
        break
else:
    print('sorry you failed')

#building car game:

command=""
while command!="quit":
    command=input(">")
    if command=="start":
        print("car started")
    elif command=="stop":
        print("car stopped")
    elif command=="help":
        print("""
              start-to start the car
              stop-to stop the car
              quit-to quit
              """)
    else:
        print('i can not umderstand')        