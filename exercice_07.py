nombres = [5, 19, 456, 20, 12, 8, 33, 0]

for i in nombres: print(i, end=" ")
print()
# for i in range(len(nombres)): print(nombres[i], end=" ")
# print()

for i in nombres:
    if i % 2 == 0 :
        print(f"{i} -> pair")
    else:
        print(f"{i} -> impair")
