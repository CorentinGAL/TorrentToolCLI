import pkgutil
import subprocess


def verifier_dependance(nom_dependance):
    if pkgutil.find_loader(nom_dependance) is not None:
        return 1
    else:
        return 0


if verifier_dependance("torrentool") == 1:
    print("Les dépendances sont bien installées")
    subprocess.check_call(["python", "main.py"])
else:
    inst = input("Les dépences ne sont pas installées, voulez vous les installées (oui/non)?\n")
    if inst == "oui":
        subprocess.check_call(["pip", "install", "torrentool"])
        subprocess.check_call(["python", "main.py"])
    else:
        print("Installer torrentool avec pip manuellement")
        exit()
