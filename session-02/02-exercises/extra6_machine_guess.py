low = 1
high = 30
guessed_correctly = False

while not guessed_correctly and low <= high:
    guess = (low+high)//2
    print(f"Is your number {guess}?")
    feedback = input("Type h for too high, l for too low, c for correct: ")

    if feedback == "c":
        guessed_correctly = True
        print("I guessed it!")
    elif feedback == "h":
        high = guess - 1
    else:
        low = guess + 1


