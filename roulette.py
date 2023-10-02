import random

spin = random.randint(0,14)

print("RESULT:")

if spin < 5:
    print("black," , spin)
elif spin < 10:
    print("red," , spin)
else:
    print("green," , spin)
