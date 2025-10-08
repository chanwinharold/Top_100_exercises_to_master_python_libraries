def divise(a :int, b :int) -> float | None:
    """
    Division entre deux entiers
    :param a: Divdende
    :param b: Diviseur
    :return: Quotient
    """
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erreur : division par zéro")

def enterDivisionInputs():
    """
    Permet à l'utilisateur d'entrer ses arguments
    :return: retoune les valeurs
    """

    while True:
        try:
            a = int(input("Entrez un entier a: "))
            b = int(input("Entrez un entier b: "))
            divise(a, b)
            break
        except ValueError:
            print("Veuillez entrer un entier !")

enterDivisionInputs()