# Temps conseillé : 20 minutes
# Sujet : Il était une fois...
# Créer les classes nécessaires à l'exécution du programme sans erreur.
# Le travail devra se faire dans la zone désignée.
# Il est possible d'exécuter le code à tout moment afin de voir le résultat.

from utils import test, results
# -------------------------------Ajouter le code en dessous------------------------------------------------------------
# Le diagramme des classes est disponible dans le fichier Diagramme.png
# Il est possible d'ajouter des attributs et méthodes au besoin sur les classes.


class Page:

    contenu: str

    def __init__ (self, contenu: str):
        self.contenu = contenu

    def getContenu(self):
        return self.contenu


class Livre:

    titre: str
    auteur: str
    annee_publication: int
    pages: []

    def __init__(self, titre: str, auteur: str, annee_publication: int):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.pages = []

    def ajouterPage(self, page: Page):
        self.pages.append(page)

    def supprimerPage(self, numPage: int):
        self.pages.pop(numPage-1)

    def hasWord(self, word: str):
        for page in self.pages:
            if word in page.getContenu():
                return True
        return False

    def lecture(self):
        tableau = []
        for index, page in enumerate(self.pages):
            tableau.append(f"{index+1} - {page.getContenu()}")
        return "\n".join(tableau)

    def __str__(self):
        return f"{self.titre}, {self.auteur} ({self.annee_publication}) : {len(self.pages)} pages"


# -------------------------------Ajouter le code au dessus-------------------------------------------------------------
# Ne pas modifier le code en dessous permettant l'exécution des tests
# La fonction test(given, expected, message) peut indiquer le résultat attendu en second paramètre
livre1 = Livre(titre="Le seigneur du Python", auteur="B2", annee_publication=2025)
livre2 = Livre(titre="1984", auteur="Orwell", annee_publication=1949)

test(livre2.titre, "1984", "1 - Le titre est bien indiqué")
test(livre1.auteur, "B2", "2 - L'auteur est bien indiqué")
test(livre1.annee_publication, 2025, "3 - L'année est bien indiquée")

livre1.ajouterPage(Page("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sed."))
livre1.ajouterPage(Page("Nulla justo nunc, tristique sit amet dui eu, rhoncus finibus dolor. Quisque vel convallis nisi. Integer id pulvinar felis. Maecenas risus lectus, aliquam ullamcorper arcu et, posuere rhoncus quam. Mauris non commodo metus, sed dapibus ex. Curabitur imperdiet, sapien vitae tristique accumsan, nisi risus varius mi, eu posuere turpis velit quis lacus. Aliquam urna ligula, sollicitudin nec eleifend in, commodo a lorem. Cras eu augue lacinia, mattis ex quis, imperdiet ligula."))
test(str(livre1), "Le seigneur du Python, B2 (2025) : 2 pages", "4 - La représentation textuelle est conforme au format '{titre}, {auteur} ({date}) : {nombrePage} pages'")

test(str(livre2), "1984, Orwell (1949) : 0 pages", "5 - Les livres ne partagent pas leurs pages entre eux")

livre1.supprimerPage(1)
test(str(livre1), "Le seigneur du Python, B2 (2025) : 1 pages", "6 - La supression de page retire une page au livre")
test(livre1.pages[0].getContenu().find("Nulla justo nunc"), 0, "7 - La supression de page retire la page avec le bon numéro au livre")

livre2.ajouterPage(Page("Mais si c'est possible avec la carte Kiwi !"))
livre2.ajouterPage(Page("l’enfant de moins de seize ans ... et ceux qui l’accompagnent jusqu’à quatre personnes ... payent tous moitié prix"))
livre2.ajouterPage(Page("https://tinyurl.com/les-classes-en-python"))
test(livre2.hasWord('Python'), False, "8 - Si le mot n'existe pas, le résultat de hasWord est False")
test(livre2.hasWord('quatre'), True, "9 - Si le mot existe, le résultat de hasWord est True")

expected_lecture = "1 - Mais si c'est possible avec la carte Kiwi !\n2 - l’enfant de moins de seize ans ... et ceux qui l’accompagnent jusqu’à quatre personnes ... payent tous moitié prix\n3 - https://tinyurl.com/les-classes-en-python"
test(livre2.lecture(), expected_lecture, "10 - La lecture du livre renvoie une chaine de caractère avec 1 page par ligne, commençant pas le numéro de page (première page = 1)")

results()
