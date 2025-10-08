def carre(x: int | float) -> int | float:
    """
    Retoune le carré du nombre entré (fonctionnel à partir de python 3.10)
    :param x: Valeur en entrée
    :return: Le carré de la valeur en entrée
    """
    return x**2


print(f"{10.4}² ->", carre(10.4))
print(f"{3}² ->", carre(3))
print(f"{5}² ->", carre(5))
print(f"{48.6394}² ->", carre(48.6394))
