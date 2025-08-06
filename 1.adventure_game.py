name = input("Hey type your name: ")
print("Hello", name, "Welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

#play = should_we_play == "yes"
#print(play)

#input is either "y" or "yes"
if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!")

# if yes, choose direction
    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("Okay we went left and fell off a cliff, game over")
    elif direction == "right": 
        print("We went right")
        choice = input("Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross)")
        if choice == "swim":
            print("You got eaten by a crocodile, you die, the end!")
        else:
            print("You found the gold and won!")
    else:
        print("Sorry not a valid reply, you die!")
else:
    print("We are NOT playing.........")