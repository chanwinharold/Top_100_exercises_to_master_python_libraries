liste1 = ['Alice', 'Bob', 'Clara', 'David', 'Eva']
liste2 = [23, 30, 25, 19, 22]

etudiants = {k:v for k, v in zip(liste1, liste2)}
print(etudiants)