import random

#VARIABLES

multiple1 = 3
multiple2 = 5

statesOfUSA = ["California", "Florida", "Texas", "Michigan", "Washington", "Arizona", "New York", "Pennsylvania", "Hawaii", "North Carolina", "Georgia", "New Jersey", "Minnesota"]
jamesBondFilms = ["Dr. No", "From Russia from Love", "Goldfinger", "Thunderball", "Casino Royale", "You Only Live Twice", "On Her Majesty's Secret Service", "Diamonds are Forever", "Live and Let Die", "TMWTGG"]

# sayAtMultiple1 = "Fizz"
# sayAtMultiple2 = "Buzz"

iterable = 100


def main():
    try:
        for i in range(1, iterable - 1):
            if i % multiple1 == 0 and i % multiple2 == 0:
                rand = random.randint(1, len(statesOfUSA) - 1)
                rand2 = random.randint(1, len(jamesBondFilms) - 1)
                print(statesOfUSA.pop(rand) + " " + jamesBondFilms.pop(rand2))
            elif i % multiple1 == 0:
                rand = random.randint(1, len(statesOfUSA) - 1)
                print(statesOfUSA.pop(rand))
            elif i % multiple2 == 0:
                rand = random.randint(1, len(jamesBondFilms) - 1)
                print(jamesBondFilms.pop(rand))
            else:
                print(i)
    except IndexError as e:
        pass
    except ValueError as e2:
        pass


if __name__ == "__main__":
    main()
