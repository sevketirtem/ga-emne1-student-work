import random
def roll_die (sides=50):
     return random.randint(1,sides)
#sides = 50 is a values we assumed when defining the function.
for i in range(1,11):
    alfa = roll_die()
    print(alfa)
# left parameter empty. Python checked there is no value then it went to assumption value. And run 50 as assumed value !
for i in range(1,11):
    beta=roll_die()
    print(beta)