import pkgutil
import subprocess
from torrentool.api import Torrent


def verifier_dependance():
    check = 0
    if pkgutil.find_loader("torrentool") is not None:
        check = 1
    else:
        check = 0
    if check == 1:
        print("Les dépendances sont bien installées")
        create_torrent()
    else:
        inst = input("Les dépences ne sont pas installées, voulez vous les installées (oui/non)?\n")
        if inst == "oui":
            subprocess.check_call(["pip", "install", "torrentool"])
            create_torrent()
        else:
            print("Installer torrentool avec pip manuellement")
            exit()


def create_torrent():
    global file
    global nbr_tracker
    global tracker
    global tracker2
    global torrent_file
    global nom
    file = input("Entrez le chemin vers le fichier à partager sans les guillemets \n")
    tracker = input("Entrez le tracker \n")
    ts = input("Avez vous un autre tracker ? (oui/non) \n")
    if ts == "oui":
        tracker2 = input("Entrez l'url du second tracker\n")
    else:
        tracker2 = " "
    nom = input("Choisissez le nom du torrent\n")
    torrent_file = nom + ".torrent"
    recap()


def recap():
    print("Les informations sont elles corrects ?\n")
    print(file, "\n", tracker, "\n", tracker2, "\n", "Nom du torrent : ", nom)
    verif = input("Tout est correct ? (oui ou non)\n")
    if verif == "oui":
        new_torrent = Torrent.create_from(file)
        new_torrent.announce_urls = tracker, tracker2
        new_torrent.to_file(torrent_file)
        print("Torrent crée dans le répertoire courrant")
        exit()
    else:
        print("Revérifier vos informations et recommencer")
        create_torrent()


verifier_dependance()