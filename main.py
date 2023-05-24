from torrentool.api import Torrent

def create_torrent():
    global file
    global nbr_tracker
    global tracker
    global tracker2
    global torrent_file
    global nom
    file = input("Entrez le chemin vers le fichier à partager \n")
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
    print(file,"\n",tracker,"\n",tracker2,"\n","Nom du torrent : ",nom)
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


create_torrent()