"""
    << Ce module intègre les fonctions communes a tous les autres fichiers i.e.
    03 problemes qui vont etre resolue en cette Journée Sahel Digital 2023 >>
"""


# Changement de couleur et de mise en forme
def color(num=0, text=""):
    return "\033[" + str(num) + "m" + text + "\033[0m"


# Titre Journée Sahel digital 2023
def welcome():
    print("\n\033[94m===========\033[0m\033[93m\033[1mJOURNEE SAHEL DIGITAL 2023 -- JSD'23\033[0m\033["
          "94m===========\033[0m")


# Affichage d'une ligne
def line():
    print("----------------------------------------------------------")


# Probleme et enoncé du probleme
def problem(num, enonce):
    print("\n-----------------------" + color(1, "PROBLEME N°" + str(num)) + "-----------------------")
    print(color(3, enonce))
    line()


# Affichage d'un titre
def title(text):
    print("\n=====" + color(1, text) + "=====")


# Affichage de ma signature (ABDOUL-BAGUI)
def me():
    print("\n" + color(90, "             \033[3mABDOUL-BAGUI, Master Informatique\033[0m"))
