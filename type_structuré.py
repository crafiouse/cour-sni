#uplet de differentes tailles
#ex1 ver = ("barnabé","jacques")
#les tuples ne peuvent être modiffiers

#exemple 2:
jour = 6 
mois = 12
annee = 2021
date = (jour, mois, annee)

'''
listes:
    -type muable
    -peut etre manipulé par des fonctions built-in
'''
def multiplierPar2(liste):
    longueur_liste = len(liste)
    for i in range(longueur_liste):
        liste[i]= liste[i]*2
    return liste

def splitingandjoin(chaine):
    print(chaine.split("c"),"= split")
    print(" ".join(chaine))
splitingandjoin("abcabcabcabc")