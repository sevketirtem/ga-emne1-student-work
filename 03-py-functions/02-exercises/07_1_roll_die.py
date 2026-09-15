import random
def roll_die (sides=50):
     return random.randint(1,sides)

for i in range(1,11):
    alfa = roll_die()
    print(alfa)

for i in range(1,11):
    beta=roll_die()
    print(beta)