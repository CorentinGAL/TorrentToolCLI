import pkgutil
import subprocess


def verifier_dependance():
    check = 0
    if pkgutil.find_loader("torrentool") is not None:
        check = 1
    else:
        check = 0
    if check == 1:
        print("Les dépendances sont bien installées")

    else:
        inst = input("Les dépences ne sont pas installées, voulez vous les installées (oui/non)?\n")
        if inst == "oui":
            subprocess.check_call(["pip", "install", "torrentool"])
            subprocess.check_call(["py", "create_torrent.py"])
        else:
            print("Installer torrentool avec pip manuellement")
            exit()


verifier_dependance()