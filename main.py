import random

points = 0
life = 10


def Afghanistan():
    print("Clue: The grave yard of empire!")


def India():
    print("Clue:Once know as the golden Bird!")


def Bhutan():
    print("Clue: The land of thunders!")


def SouthKorea():
    print("Clue: Kpop orginate from this country!")


def Egypt():
    print("Clue: This country is famous for its pyramids!")


def Japan():
    print("Clue: This land of Anime!")


def China():
    print("Clue: This country has the Biggest man made wall in the world!")


def Russia():
    print("Clue: This country sent the first human into space")


def Israel():
    print("Clue: This country is home to some of the world's most holy sites")


def Greece():
    print("Clue: This country invented the Olympic Games")


countries = [
    Afghanistan,
    India,
    Bhutan,
    SouthKorea,
    Egypt,
    Japan,
    China,
    Russia,
    Israel,
    Greece,
]


while life > 0 and len(countries) > 0:
    flag = random.choice(countries)
    flag()
    answer = input("Guess the flag!")

    if answer == flag.__name__:
        print("Correct answer!")
        points += 1
        print("Points:", points)
        print("Life:", life)
        countries.remove(flag)

    else:
        print("Try again")
        if points > 0:
            points -= 1
        else:
            points = 0
        life -= 1
        print("Points:", points)

if (points) >= 5:
    print(" Your Geography knowledge is good")
elif (points) >= 8:
    print(" Your Geography Knowledge is Very good")
elif (points) >= 9:
    print("Congragulation!!! You are the king of Geography")
else:
    print("Try Again after learning more about countries ")

print("GAME OVER")
