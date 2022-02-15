# Auteur : Sémiat Oyénikè Olaitan
# Date : 15 Février 2022
#
# Ce programme calcul la masse molaire 
# d'une molécule (la formule du molécule) entrée par un utilisateur.





# Charger les atomes en dictionnaire
def charger_atomes():
    with open('atomes.txt', 'r') as atomes:
        lignes = atomes.read().split('\n')

    dictionnaire = {}

    for i in lignes:
        i = i.split('*')
        dictionnaire[i[0]] = i[1]

    return dictionnaire

def decomposition(mol: str):
    mol.strip()
    mol += '*'
    i = 0
    l = {}
    while i < len(mol) - 1:
        nb = 1
        if mol[i].isupper():
            ch = mol[i]
            if mol[i+1].islower():
                ch += mol[i+1]
                i += 1
            if mol[i+1].isdigit():
                a = mol[i+1]
                i += 1
                if mol[i + 1].isdigit():
                    a += mol[i + 1]
                    i += 1

                nb = int(a)

            l[ch] = nb

        i += 1
    return l

def masse_molaire_moleculaire(mol: {}, atomes: {}):
    masse = 0

    for i in mol.items():
        tmp = masse
        for j in atomes.items():
            if i[0] == j[0]:
                masse += int(i[1]) * float(j[1])
                break

        if tmp == masse:
            return "Erreur: l'atome " + i[0] + " n'existe pas."

    return masse



if __name__ == '__main__':
    atomes = charger_atomes()

    titre = 'Programme de calcul de masse molaire'

    print(3*'****** '.center(len(titre)))
    print(titre.upper().center(len(titre)*3))
    print(3*'****** '.center(len(titre)))


    molecule = str(input('>>> Entrez la formule de la molécule: '))

    # Vérifier si la formule de la molécule est un alphanumérique
    if molecule.isalnum():
        print(masse_molaire_moleculaire(decomposition(molecule), atomes))

    else:
        print("La formule d'une molécule est un alphanumérique et "\
         "commence avec une lettre majuscule.")


# def verification(mol: str):
#     if mol[0].islower():
#         return False
#
#     for i in mol:
#         if not ('A' <= i <= 'Z' or 'a' <= i <= 'z' or i not in range(2,10)):
#             return False
#
#     return True


# Auteur : Sémiat Oyénikè Olaitan
# Date : 15 Février 2022
#
# Ce programme calcul la masse molaire 
# d'une molécule (la formule du molécule) entrée par un utilisateur.
