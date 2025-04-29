# Temps conseillé : 15 minutes
# Sujet : Des Comptes à rendre !
# Barème : Chaque test réussi rapporte 1 point.
# Créer la classe nécessaire à l'exécution des tests sans erreur.
# Le travail devra se faire dans la zone désignée.
# Il est possible d'exécuter le code à tout moment afin de voir le résultat.

from utils import test, results
# -------------------------------Ajouter le code en dessous------------------------------------------------------------
# Le diagramme de la classe est disponible dans le fichier Diagramme.png
# Il est possible d'ajouter des attributs et méthodes au besoin.
class CompteBancaire:

    titulaire: str
    solde: float = 0
    canRetirer: bool = False

    def __init__(self, titulaire: str):
        self.titulaire = titulaire

    def __str__(self):
        return f"{self.titulaire} : {self.solde}€"

    def deposer(self, montant: float):
        if montant > 0:
            self.solde += montant
            if self.solde >= 50:
                self.canRetirer = True

    def retirer(self, montant: float):
        if self.canRetirer and self.solde - montant >= 0:
            self.solde -= montant

# -------------------------------Ajouter le code au dessus-------------------------------------------------------------
# Ne pas modifier le code en dessous permettant l'exécution des tests
# La fonction test(given, expected, message) peut indiquer le résultat attendu en second paramètre

c1 = CompteBancaire("Jean")
c2 = CompteBancaire("Charlotte")
c3 = CompteBancaire("Gérard")
test(c1.titulaire, "Jean", "1 - Le nom du titulaire est correctement renseigné")

c2.deposer(50)
test(c2.solde, 50, "2 - Le dépot d'un solde positif est possible")

c2.deposer(-50)
test(c2.solde, 50, "3 - Le dépot d'un solde négatif ne fonctionne pas")

c2.retirer(25)
test(c2.solde, 25, "4 - Le retrait est possible")

c1.deposer(25)
c1.retirer(25)
test(c1.solde, 25, "5 - Le retrait n'est pas possible si au moins 50€ n'ont pas été déposés")

c1.deposer(25)
test(c1.solde != c2.solde, True, "6 - Les comptes bancaires ne sont pas liés entre eux")

c1.retirer(50)
test(c1.solde, 0, "7 - Le retrait est possible après 50€ déposé sur le compte")

c3.deposer(50)
c3.retirer(50)
test(c3.solde, 0, "8 - Il est possible de retirer et atteindre 0€ sur son compte bancaire")

c3.deposer(150)
c3.retirer(151)
test(c3.solde, 150, "9 - On ne peut pas retirer plus que son solde")

test(str(c3), "Gérard : 150€", "10 - La représentation en chaine de caractère correspond au format : 'titulaire : solde€'")
results()