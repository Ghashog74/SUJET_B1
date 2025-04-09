# Temps conseillé : 10 minutes
# Sujet : Des lettres et des lettres
# Barème : Chaque test réussi rapporte 1 point.
# Créer la fonction nécessaire à l'exécution des tests sans erreurs
# Le travail devra se faire dans la zone désignée.
# Il est possible d'exécuter le code à tout moment afin de voir le résultat.

from utils import test, results
# -------------------------------Ajouter le code en dessous------------------------------------------------------------

# La fonction 'compterVoyelles' prendra en paramètre une chaine de caractères et devra compter le nombre de
# voyelles dans cette chaine.
# Elle devra retourner un dictionnaire ayant comme clés les voyelles (a, e, i, o, u, y) en minuscules et en valeur le
# compte de chaque voyelle. La fonction ne doit pas être sensible à la casse.
voyelles = ["a", "e", "i", "o", "u", "y"]
def compterVoyelles(chaine: str):
    chaine = chaine.lower()
    result = {"a":0, "e":0, "i":0, "o":0, "u":0, "y":0}
    for lettre in chaine:
        if lettre in voyelles:
            result[lettre] += 1
    return result


# -------------------------------Ajouter le code au dessus-------------------------------------------------------------
# Ne pas modifier le code en dessous permettant l'exécution des tests
# La fonction test(given, expected, message) peut indiquer le résultat attendu en second paramètre

test(compterVoyelles("aeiouy"), {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'y': 1}, "1 - Les voyelles sont bien comptées en minuscules")
test(compterVoyelles("AEIOUY"), {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'y': 1}, "2 - Les voyelles sont bien comptées en majuscules")
test(compterVoyelles("hfjdks"), {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}, "3 - L'absence de voyelle est bien pris en compte")
test(compterVoyelles("AaA"), {'a': 3, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}, "4 - Il est possible de mixer la casse")

results()