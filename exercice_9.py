nombres = list(range(1, 21))

def isOdd(x :int) -> bool:
    return x % 2 == 0

def isOdd_(x :int) -> int | None:
    if x % 2 == 0: return x
    return None

# Filter
pairs = filter(isOdd, nombres)
for i in pairs: print(i, end=" ")
print()

# Map
pairs = map(isOdd_, nombres)
for i in pairs:
    if i:
        print(i, end=" ")
print()

# Comprehension
print([i for i in nombres if i % 2 == 0])
print()
