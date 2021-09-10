
username = input("Enter username:")
print("Let's go " + username)


def start():
    print("I pull the corner. (left or right)")

    answer = input("")

    if answer == "left":
        print("You got out to coridor")
    coridor()
    elif answer == "right":
        game_over("Freddy got you already.")
    else:
        print("Invalid choice.")
    start()


def coridor():
    print("Got out of my room, I think I'm safe now. ")
    print("I see light under my parent's room.")
    print(" Is mom home and way she didn't hear me when I was calling here.")
    print("Do I go in and check or I will still try to get out (yes or no)")

    answer = input("")

    if answer == "yes":
        game_over("Freddy got you!! ")
    elif answer == "no":
        guest_room()
    else:
        print("Invalid choice.")


def guest_room():
    print("You got to the stairs, way mom is in the guest bedroom?")
    print("Thank God I didn't go to mom's, Freddy got here to corner.")
    print("I need to help here.")
    print("Are you taking? (bedroom or stairs)")

    answer = input("")

    if answer == "bedroom":
        lobby()
    print("You got mom and she can run out to be safe. Good job.")
    elif answer == "stairs"
    game_over("Freddy got you!! ")
    else:
        print("Invalid choice.")


def lobby():
    print("We sneak down the stairs very slowly and quietly.")
    print("Mom told she needs here purse, because there are car keys in it.")
    print("The purse is in the kitchen next to the microwave. ")
    print("Mom was going to the car, and I turned to the kitchen.")

    answer = input("")

    if answer == "left":
        game_over("Freddy never let's you out!!")
    elif answer == "right":
        kitchen("You heading to the kitchen..")
    else:
        print("Invalid choice.")


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
