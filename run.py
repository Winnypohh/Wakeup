# Find player name
playername = input(" Enter playername: ")
# Print Call player to play
print(" Let's play: " + playername)
# player age and underage confermation
while True:
    try:
        age = int(input(" Enter your age:  "))
    except ValueError:
        print(" Sorry, didn't get that.")
        continue
    if age < 0:
        print(" Sorry, your response must not be negative.")
        continue
    else:
        # age was successfully parsed, and we're happy with its value.
        break
if age >= 18:
    print(" You are able to play!")
# if age is under 18 you are out of game and from program
else:
    print(" You are not able to play.")
    exit()


# function to ask play again or not
def play_again():
    print("\n Do you want to play again? (yes or no)")
# take input()
    answer = input("# ")
# if player choice is yes, start the game from beginning
    if "yes" in answer:
        start()
# if player choice is no or something else, exit() form game
    else:
        exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()


# second floor coridor
def second_floor_coridor():
    # some text
    print("\n Got out of my room, I think I'm safe now. ")
    print(" I see a light under my parent's room.")
    print(" Is my mom home and why she didn't she hear me when I was calling.")
    print("\n Do I go in or I will still try to get out? (yes or no)")
# take input for player answer
    answer = input("# ")
# player choices
    if answer == "yes":
        # wrong choice start new game
        print(" Freddy got you!! ")
        play_again()
    elif answer == "no":
        # player is pass to next room, guest_room
        guest_room()
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# guest room
def guest_room():
    # some text
    print("\n You got to the stairs.")
    print(" But you heard your mom in the guest bedroom!")
    print(" Thank God I didn't go to mom's room.")
    print(" Maybe Freddy got here cornered?")
    print(" I need to help her.")
    print("\n Are you taking? (guest bedroom or stairs)")
# take input for player answer
    answer = input("# ")
# player choices
    if answer == "guest bedroom":
        print("\n You got mom and she can run out to be safe. Good job.")
# Takes player to lobby
        lobby()
    elif answer == "stairs":
        # wrong choice start new game
        play_again(" Freddy got you!!")
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# lobby
def lobby():
    # some text
    print("\n We creep down the stairs very slowly and quietly.")
    print(" Mom told me she needs here purse, because the car keys are in it.")
    print(" The purse is in the kitchen next to the microwave.")
    print(" Mom was going to the car, and I turned to the kitchen.")
    print("\n Are you going? (left or right)")
# take input for player answer
    answer = input("# ")
    # player choices
    if answer == "left":
        # wrong choice start new game
        play_again(" Freddy never let's you out!!")
    elif answer == "right":
        # right choice pass to stop_living_room
        print(" You heading to the kitchen.. ")
        stop_living_room()
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# stop in the living room
def stop_living_room():
    # some text
    print("\n I’m scared and moving closer to the kitchen.")
    print(" But I need to pass the living room.")
    print(" Someone turned tv on.")
    print(" I'm looking through the gap between the door frame and the door.")
    print(" Someone is sitting on my dad’s chair, did dad came home early.")
    print(" Come in my son told the man on chair, and it sounded like my dad.")
    print(" I went in slowly, but Freddy pushed me in, straight to the chair.")
    print(" The whole room changed and I front of the fireplace, ")
    print(" and it was hot.")
    print(" Freddy's fingers looked like sharp knives, ")
    print(" when he was sliding his fingers over my face, ")
    print(" and asked me to sing a song with him.")
    print(" I knew what he wanted, but I wanted to wake up so badly.")
    print("\n Are you singing for Freddy? (yes or no)")
# take input for player answer
    answer = input("# ")
    # player choices
    if answer == "yes":
        # some text
        print("\n The heat from fire, fire I was thinking, and I told yes.")
        print(" I want to sing for him, but can he stand in front of me, ")
        print(" when I start singing.")
        print(" One, Two, Three Freddy.. and I pushed him into the fire.")
        print(" You ran out of the room and got back to Lobby.")
# right choice pass to next room called lobby1
        lobby1()
    elif answer == "no":
        # wrong choice start new game with some text
        play_again(" Freddy got you again!!")
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# lobby 1
def lobby1():
    # some text
    print("\n Back in lobby.")
    print(" I'm so scared and relieved at the same time ")
    print(" and forgot what I need to do now.")
    print("\n Do I go? (left or right).")
# take input for player answer
    answer = input("# ")
    # player choices
    if answer == "left":
        # right choice pass to next room called kitchen
        kitchen()
    elif answer == "right":
        # wrong choice start new game with some text
        play_again(" Freddy got you.")
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# kitchen
def kitchen():
    # some text
    print("\n I’m at the kitchen door, I need to get the car keys.")
    print(" The kitchen is a bad place for me, ")
    print(" all the knives and forks and who knows what more is in there ")
    print(" waiting for me. But I need the car key!!!")
    print("\n Do I open the door? (yes or no)")
# take input for player answer
    answer = input("# ")
    # player choices
    if answer == "yes":
        print(" you are in the kitchen and got the keys.")
# right choice pass to next room called lobby2
        lobby2()
    elif answer == "no":
        # wrong choice start new game with some text
        play_again(" Car key is important and Freddy got you in end.")
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# lobby 2
def lobby2():
    # some text
    print("\n Running out from kitchen and getting back to lobby, ")
    print(" do I go through the living room to the front door, ")
    print(" or I go straight to the front,  or basement.")
    print("\n What i do? (straight, right or left)")
# take input for player answer
    answer = input("# ")
    # player choices
    if answer == "left":
        print(" I will go to the basement, and get closer to getting out.")
# right choice pass to next room called basement
        basement()
    elif answer == "right":
        # wrong choice start new game with some text
        play_again(" Living room hell and Freddy got you.")
    elif answer == "straight":
        # wrong choice start new game with some text
        play_again(" You should to know, Freddy waits you there..!!")
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# basement
def basement():
    # some text
    print("\n Basement is scary but living room was hell alredy")
    print(" I think i will be ok..")
    print(" and Freddy knows I'm not giving up.")
    print(" I will fight till I'm out and safe. ")
    print(" There is a door at the back of the wall.")
    print(" I need to get there.")
    print(" I hope the door is not locked.... ")
    print("\n Do I go? (right or straight)")
# take input for player answer
    answer = input("# ")
    # player choices
    if answer == "straight":
        # wrong choice start new game with some text
        print(" I will be stuck in ropes and other tools.")
        play_again(" Freddy got you!!")
    elif answer == "right":
        print(" I'm closer than ever to get out. Run quickly!!")
# right choice pass to next room called backdoor
        backdoor()
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# backdoor
def backdoor():
    # some text
    print("\n Finally, I got to the back door, ")
    print(" and someone left the key on the door lock.")
    print(" I turned the key, ")
    print(" and I felt the wind from outside.")
    print("\n Suddenly I felt something sharp on my back, ")
    print(" it hurts, the pain is real.")
    print(" But I can't stop now up the steps and then (Left or Right) ")
    print(" Do i go? (left or right)")
# take input for player answer
    answer = input("# ")
# player choices
    if answer == "left":
        # wrong choice with play_again and with some text
        print("\nThe fence is too high and you are stuck.")
        print(" Evil dog and Freddy are here.")
        play_again(" Freddy got you!!")
    elif answer == "right":
        # some text
        print(" I see the car. Run, run quickly!!")
# right choice pass to next room called car
        car()
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# cars
def car():
    # some text
    print("\n Running fastest how I can.")
    print(" It's my legs they are moving, ")
    print(" but it feels I'm standing in the same place. ")
    print(" I see the car!!")
    print(" I have car keys in my hand.")
    print(" Need to unlock car doors.")
    print(" She Locked  them to be safe.")
    print(" I'm so panicked, but i need to get in to hte car!!")
    print(" Wich button to press? (left or right)")
# take input for player answer
    answer = input("# ")
# player choices
    if answer == "left":
        # you finished the game takes you back play_again() choice
        print("\n You got to the car and locked the doors.")
        print(" Freddy is gone forever.")
        print("\n You woke up in your ROOM!!")
        play_again()
    elif answer == "right":
        # wrong choice start new game with some text
        print(" You will sleep forever, in Freddys land")
        game_over()
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# beginning of the game
def start():
    # some text
    print("\n WAKE UP OR FREDDY WILL HUNT YOU!!!")
    print("\n One day coming from school we called out Freddy, ")
    print(" with my friends.")
    print(" I think he heard us calling.")
    print(" When I walked home, I was thinking a lot about what I felt.")
    print(" I wished my mom was driving me home from school, ")
    print(" the car is the safest place for me, ")
    print("it’s a relaxing and calm place, ")
    print(" if you are driving in the back seat.")
    print("\n I saw my house from a distance, and I felt safer than ever.")
    print(" We have lovely two floor house.")
    print(" A fence going all around the house.")
    print(" On the left, if I’m in front of the house is a higher fence, ")
    print(" we have a dog, and he jumps over all the time.")
    print(" On the right of the house, we have the drive for car two cars, ")
    print(" but today there is one. Mom is home, I hope.")
    print(" Do we continue? (yes or no)")
# take input for player answer
    answer = input("# ")
# player choices
    if answer == "yes":
        # takes player to next() text.
        next()
    elif answer == "no":
        # takes player play_again().
        paly_again()
    else:
        # takes player to game_over()
        game_over(" Invalid choice.")


# some text
def next():
    print("\n On the first floor we have a kitchen, ")
    print(" lobby, living room, office and a door to the basement.")
    print(" On the second floor we have three bedrooms ")
    print(" and two bathrooms with walk-in wardrobes.")
    print(" I stepped into the lobby, and I called: ")
    print(" is there anybody home!! No answer!!")
    print(" I went to up to my room and felt tired, ")
    print(" jumped on my bed and was looking at the ceiling, ")
    print(" wind blowing into my room, ")
    print(" because my mom had opened the window like she always does.")
    print(" Wind blowing and birds are singing ... ")
    print("\n Do we continue? (yes or no)")
# take input for player answer
    answer = input("# ")
# player choices
    if answer == "yes":
        # takes player to next1() text.
        next1()
    elif answer == "no":
        # takes player play_again().
        paly_again()
    else:
        # takes player to game_over()
        game_over(" Invalid choice.")


# some text.
def next1():
    print("\n I think I closed my eyes for a second.")
    print(" I opened my eyes and somehow, I was under the blanket.")
    print(" How I got under the blanket, maybe I was doing that at my sleep, ")
    print(" but I just closed my eyes for a second.")
    print(" I didn't feel any wind, someone closed my window.")
    print(" I noticed, it was dark outside but still windy.")
    print(" I try to get out, I move myself left and right and I get arms out")
    print(" I try to pull the left corner and right corner,")
    print(" but someone is holding blanket very tight.")
    print(" I can hear metal sounds coming from under my bed!")
    print("\n I pull the corner. (left or right)")
# take input for player answer
    answer = input("# ")
    # player choices
    if "left" in answer:
        # takes you to second_floor_coridor and some text
        print(" You got out to coridor.")
        second_floor_coridor()
    elif "right" in answer:
        # wrong choice start new game with some text
        game_over(" Freddy got you already.")
    else:
        # else is game_over() with a reason
        game_over(" Invalid choice.")


# start the game
start()
