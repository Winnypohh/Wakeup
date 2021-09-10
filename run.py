

def start():
    print("I pull the corner. (left or right)")

    answer = input("")

    if "left" in answer:
        print("You got out to coridor")
        coridor()
    elif "right" in answer:
        game_over("Freddy got you already.")
    else:
        game_over("Invalid choice.")
    start()


def coridor():
    print("Got out of my room, I think I'm safe now. ")
    print("I see light under my parent's room.")
    print(" Is mom home and way she didn't she hear me when I was calling.")
    print("Do I go in and check or I will still try to get out. (yes or no)")

    answer = input("")

    if answer == "yes":
        game_over("Freddy got you!! ")
    elif answer == "no":
        guest_room()
    else:
        print("Invalid choice.")


def guest_room():
    print("You got to the stairs.")
    print(" But you heard your mom in the guest bedroom!")
    print("Thank God I didn't go to mom's room.")
    print("Maybe Freddy got here cornered?")
    print("I need to help here.")
    print("Are you taking? (bedroom or stairs)")

    answer = input("")

    if answer == "bedroom":
        lobby()
    print("You got mom and she can run out to be safe. Good job.")
    elif answer == "stairs":
        game_over("Freddy got you!!")
    else:
        print("Invalid choice.")


def lobby():
    print("We creep down the stairs very slowly and quietly.")
    print("Mom told she needs here purse, because the car keys are in it.")
    print("The purse is in the kitchen next to the microwave. ")
    print("Mom was going to the car, and I turned to the kitchen.")

    answer = input("")

    if answer == "left":
        game_over("Freddy never let's you out!!")
    elif answer == "right":
        stop_living_room("You heading to the kitchen..")
    else:
        print("Invalid choice.")


def stop_living_room():
    print("I’m scared and moving closer to the kitchen.")
    print("But I need to pass the living room.")
    print("Someone turned tv on.")
    print("I'm looking through the gap between the door frame and the door.")
    print("Someone is sitting on my dad’s chair, did dad came home early.")
    print("Come in my son told the man on chair, and it sounded like my dad.")
    print("I went in slowly, but Freddy pushed me in, straight to the chair.")
    print("The whole room changed and I was sitting infront of the fireplace,")
    print("and it was hot.")
    print("Freddy's fingers looked like sharp knives,")
    print("when he was sliding his fingers over my face,")
    print("and asked me to sing a song with him.")
    print("I knew what he wanted, but I wanted to wake up so badly. ")
    print("Are you singing for Freddy (yes or no)")

    answer = input("")

    if answer == "yes":
        print("The heat from fire, fire I was thinking, and I told him yes.")
        print("I want to sing for him, but can he stand in front of me,")
        print("when I start singing.")
        print("One, Two, Three Freddy.. and I pushed him into the fire.")
        lobby("You ran out of the room and got back to Lobby.")
    elif answer == "no":
        game_over("Freddy got you again!!")
    else:
        game_over("Invalid choice.")


def kitchen():
    print("")
    print("")
    print("")
    print("")


# game_over function accepts an argument called "reason"
def game_over(reason):
    print("No" + reason)
    print("Game Over!")
    play_again()


# function to ask play again or not
def play_again():
    print("Do you want to play again? (yes or no)")
    answer = input("")

    if "yes" in answer:
        start()
    else:
        exit()
