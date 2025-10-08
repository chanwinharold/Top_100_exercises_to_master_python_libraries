import time
nombres = list(range(1000000))

# for loop

x1 = time.time()
cubes_1 = list()
for i in nombres: cubes_1.append(i**3)
x2 = time.time()
# Comprehension list

y1 = time.time()
cubes_2 = [i**3 for i in nombres]
y2 = time.time()

print(f"La méthode 'For loop' prend {x2 - x1} temps")
print(f"La méthode 'Comprehension list' prend {y2 - y1} temps")