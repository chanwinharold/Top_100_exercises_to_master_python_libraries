class Rectangle:
    def __init__(self, largeur :int|float, hauteur :int|float):
        """
        Création d'un rectangle
        :param largeur: Sa largeur
        :param hauteur: Sa hauteur
        """
        self.largeur_ = largeur
        self.hauteur_ = hauteur

    def aire(self) -> float | int:
        """
        Calcul de l'aire du rectangle
        :return: retourne l'aire
        """
        return self.hauteur_ * self.largeur_

    def perimetre(self) -> float | int:
        """
        Calcul du périmètre du rectangle
        :return: retourne le périmètre
        """
        return (self.hauteur_ + self.largeur_) * 2

rect = Rectangle(5, 12.589)
print(f"L'aire d'un rectangle de hauteur {12} et de largeur {5} est {rect.aire()}")
print(f"Le périmètre d'un rectangle de hauteur {12} et de largeur {5} est {rect.perimetre()}")

