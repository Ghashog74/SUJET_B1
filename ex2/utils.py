# NE PAS MODIFIER CE FICHIER !
# Il s'agit de fonctions permettant d'exécuter les tests de votre programme.
TOTAL_TEST = 0
OK_TEST = 0
WARN_TEST = 0
ERROR_TEST = 0

def test(given, expected, name):
    global TOTAL_TEST, OK_TEST, WARN_TEST, ERROR_TEST
    TOTAL_TEST += 1

    if type(given) is not type(expected):
        warning(f"{name} : Les types de l'attendu et du reçu ne correspondent pas.\n\t- Type attendu : {type(expected)}\n\t- Type reçu : {type(given)}")
        WARN_TEST += 1

    if given != expected :
        error(f"{name} : \n\t- Attendu : {expected}\n\t- Reçu : {given}")
        ERROR_TEST += 1
        return

    OK_TEST += 1
    success(name)

def results():
    global TOTAL_TEST, OK_TEST, WARN_TEST, ERROR_TEST
    print("\033[94m[RÉSULTATS DES TESTS]\033[0m")
    print(f"Nombre de tests exécutés : {TOTAL_TEST}")
    print(f"Nombre de warning : { '\033[93m' if WARN_TEST != 0 else ''} {WARN_TEST}\033[0m")
    print(f"Nombre d'erreurs : { '\033[91m' if ERROR_TEST != 0 else ''} {ERROR_TEST}\033[0m")
    print(f"Nombre de réussites : \033[92m{OK_TEST}\033[0m")

    score = (100 * OK_TEST / TOTAL_TEST) if TOTAL_TEST != 0 else 0
    print(f"\n\tScore global = \033[1m{OK_TEST}/{TOTAL_TEST} ({score:.2f} %)")

def warning(m):
    print(f"\033[93m[WARN] {m}\033[0m")

def error(m):
    print(f"\033[91m[ERROR] {m}\033[0m")

def success(m):
    print(f"\033[92m[OK] {m}\033[0m")