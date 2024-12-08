print('Did you know "e" is the most common letter?')
print(""),
print("1 = How Many Letters?")
print("2 = Immpossible Sentence...")
print("3 = History of E")
print("4 = Guess the word")
Word1 = "Elephant"
Word2 = "Election"
Word3 = "Entrance"
Word4 = "Episode"
Word5 = "Earth"
Word6 = "Eastern"
Word7 = "Ecthyma"
Work8 = "Economy"
Work9 = "Effective"
Word10 = "Elaborate"
import random
random_number = random.randint(1, 10) 
# Generates a random integer between 1 and 10
word = "what"
if random_number == 1:
    word = Word1
    lettercount = 8
if random_number == 2:
    word = Word2
    lettercount = 8
if random_number == 3:
    word = Word3
    lettercount = 8
if random_number == 4:
    word = Word4
    lettercount = 7
if random_number == 5:
    word = Word5
    lettercount = 5
if random_number == 6:
    word = Word6
    lettercount = 7
if random_number == 7:
    word = Word7
    lettercount = 7
if random_number == 8:
    word = Work8
    lettercount = 7
if random_number == 9:
    word = Work9
    lettercount = 9
if random_number == 10:
    word = Word10
    lettercount = 9
WhichMinigame = input("Which Gamemode do you want to play?")
i = 0
print(lettercount)
if WhichMinigame == "1":
    OneInput = input("Type a Sentence...")
    if "e" in OneInput:
        print("Your word has the letter e in it!")
    else:
        print("Your word doesnt have the letter e in it.")
else:
    if WhichMinigame == "2":
        OneInput = input("Try to write a full sentence without the letter e!")
        if "e" in OneInput:
            print("Start Over; Try again")
        else:
            print("You did it!")
    else:
        if WhichMinigame == "3":
            print("History")
            print("The letter 'E' has a rich linguistic history, with its roots dating back to ancient civilizations. It is derived from a Semitic consonant that represented a sound similar to the English. The original Semitic character may have represented a lattice window or a fence1. In ancient Greek, it was associated with mystery and secret rites2. The letter 'E' has evolved over time, and its origins can be traced back to Egyptian hieroglyphic writing and early Semitic writing")
        else:
            if WhichMinigame == "4":
                print('You just choose "find the word"')
                while i < 10:
                    Letter1 = input("What do you think the next letter is?")
                    if Letter1 in word:
                        print("the letter", Letter1, "is in the word")
                        lettercount -= 1
                    else:
                        print("your letter isnt in  the word")
                        i += 1
                    if lettercount == 0:
                        print("you did it!")
                if lettercount != 0:
                    print("You lost...")
                    print("To restart restart the code...")
                

                    
                