import time


# Choix de cuisson
def choix_cuisson(teme):
    choix = input(f"Votre choix entre (1 et {len(teme)}) : ")
    try:
        choix_int = int(choix)
        if choix_int < 1 or choix_int > len(teme):
            print("Erreur!")
            return choix_cuisson(teme)
    except:
        print("Erreur! Vous devez entré des chiffres")
        return choix_cuisson(teme)
    cle = teme[choix_int-1][0]
    valeur = teme[choix_int-1][1]
    return cle, valeur


cuisson = [
    ("Oeufs à la coque", 3*60),
    ("Oeufs mollets", 6*60),
    ("Oeufs durs", 9*60)
]

# Affichage du menu
print("Cuisson de œufs")
index = 1
for c in (cuisson):
    print(index, "-", c[0])
    index += 1


cle, valeur = choix_cuisson(cuisson)

duree = valeur

# Ce programme de type "minuteur" vous permettra d'afficher en temps réel le temps restant de cuisson.
print("\n_", cle, ":", str(duree//60) +":"+ str(duree-(duree//60)*60).zfill(2))
print("\ncuisson en cours", end="", flush=True)

temps = 10
while True:
    for i in range(temps):
        time.sleep(1)
        print(".", end="", flush=True)
        duree -= 1
        
        if duree < temps:
            temps = duree

    min = duree//60 
    if duree == 0:
        print()
        print("Cuisson terminée !")
        break
    
    print()
    print(f"temps restant {min:02}:{duree-min*60:02}", end="", flush=True)


# ____________________________________________________

# def table_mult(min, max,n):
#     if min > max:
#         print("Erreur! min est suppérieur à max")
#         return
#     for i in range(min, max+1):
#         print(n,"x", i, "=", n*i)


# min = 1
# max = 10
# n = 4
# table_mult(min, max,n)


# __________________________________________________

# age = [30, 36, 53, 46, 92, 57, 30]
# f = False
# for i in age:
#     if i == 36:
#         f = True

# if f:
#     print(i, "est present")
# else:
#     print(i, "est absent")

# ________________________________________________

# def extention(u, doc):
#     for i in doc:
#         if u == i[0].lower():
#             return i[1]  
#     return "Extension inconnue"

  
# fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

# definition_extensions = (("doc", "Document Word"),
#                         ("exe", "Executable"),
#                         ("txt", "Document Texte"),
#                         ("jpeg", "Image JPEG"))


# for fichier in fichiers:
#     ext = fichier.split(".")
#     if len(ext) > 1:
#         definition = extention(ext[-1].lower(), definition_extensions)
#         print(fichier, ":", definition)
#     else:
#         print(fichier, ": Pas d'extension")
        
# ________________________________________________________________


