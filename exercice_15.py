etudiants = [
    {'nom': 'Gladyss', 'notes': [18, 12, 20]},
    {'nom': 'Paul', 'notes': [15, 8, 12]},
    {'nom': 'Mathias', 'notes': [20, 19, 5]},
]

for i in range(len(etudiants)):
    etudiants[i]['moyenne'] = round(
        number=sum(etudiants[i]['notes']) / len(etudiants[i]['notes']),
        ndigits=2 )
    print(f"Moyenne de {etudiants[i]['nom']} : {etudiants[i]['moyenne']}")

print(max(etudiants, key=lambda etu: etu['moyenne'])['nom'], "a la plus haute moyenne")
