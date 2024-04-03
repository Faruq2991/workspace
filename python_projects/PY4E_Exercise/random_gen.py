import random

for i in range(2):
    x = random.random()
    print(x)

x = random.randint(5, 20)
print(x)

names = ["Aisha", "Moonah", "Ruqayya"]

random.choice(names)
print(names)