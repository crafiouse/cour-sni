#Ex1
from typing import List


def calculVitesse(temps:float,distance:float):
    vitesse = distance/temps
    print(round(vitesse,2))
    return(round(vitesse,2))
#Ex2    
def entier():
    for i in range(1,11):
        print(i)
        i = i+1
#Ex3
def entierbor():
    i = 1
    while i != 11:
        print(i)
        i = i+1
#Ex4
def liste(char:str):
    length=((char).join(char)).count(char)
    for i in range (length):
        print(char[i])
        i = i + 1
#Ex5
def entiernincl():
    for i in range(2,10):
        print(i)
        i = i+1

def rechercheMinimale():
    inputrate = int(input("Combien de fois voulez-vous entré une donné ?"))
    for i in range(inputrate):
     listeav = int(input("Donner votre valeur."))
     listeav3 = [].append(listeav)
    listeav3.sort(reverse=True)
    return listeav3

#Partie 2

def table():
    tables = []
    for i in range(1,12):
        print(tables)
        tables = []
        for n in range(1,11):
            y = n*i
            tables.append(y)

#Ex3

def noespachar():
    charlist = []
    chars = int(input("combien de caractère voulez-vous?"))
    says = ""
    
    for i in range (chars):
        
        bruh = input("donner votre caractère")
        charlist.append(bruh)
    print(charlist)
    
    for i in range(len(charlist)):
        if charlist[i] != " ":
            says = says + charlist[i]
    print(says)
noespachar()


def retirespace(s):
    s2=""
    for i in range(len(s)):
        if s[i]!=" ":
            s2+=s[i]
            
    print(s2)
    return s2
    
def retireEspaceListe(lis):
    t=[]
    for i in range(len(lis)):
        t.append(retirespace(lis[i]))
    return t
    