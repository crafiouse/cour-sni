#1
print("hello world !")
#2
#variable
i = 12
#Grâce à cette ligne, nous avons défini une variable qui porte le nom i. Ce nom i est associé à la valeur 12.
point_de_vie = 15

#3
#Nous venons de voir qu'un nom pouvait être associé à nombre entier, mais il peut aussi être associé à un nombre à virgule :
i = 5.2
#Un nom peut donc être associé à plusieurs types d'entités (pour l'instant nous n'en avons vu que deux, mais nous en verrons d'autres plus loin) :
#les nombres entiers ("integer" en anglais, abrégé en "int") et les nombres à virgule ("float" en anglais).
# Il est possible de connaitre le type de l'entité à l'aide de l'instruction "type"

#4 Testez le programme suivant :
a = 5.2
b = 12
print(a)
print(b)
#Comme vous pouvez le constater,
#le type de la grandeur associée à a et le type de la grandeur associée à b s'affichent dans la console
#Un ordinateur est bien évidemment capable d'effectuer des opérations mathématiques (arithmétiques).
#Les signes utilisés sont classiques : +, - , * (multiplication), / (division), // (division euclidienne) 
# ou encore % (modulo : reste d'une division euclidienne).

#5
#Essayez d'écrire un programme qui additionnera le contenu de 2 variables
print(a + b)

#6 D'après vous, que fait ce programme ?
#le programme:
a = 11
a = a + 1
#ce programme associe la valeur 11 a la variable "a" puis ajoute 1 a la variable
#donnant 12
print(a)
#exposant, racine carrée, fonctions trigonométriques

import math

#Cette ligne permet d'importer (et donc d'utiliser)
#le module math (ce module contient toutes les fonctions mathématiques "classiques").
#quelques exemples:
#math.pow(x,a) permet de calculer x à la puissance a (il est aussi possible de directement écrire x**a)
#math.cos(x) permet de calculer le cosinus de l'angle x (l'angle x doit être en radian) (nous avons la même chose pour le sinus ou la tangente)
#math.sqrt(x) permet de calculer la racine carrée de x
#Si vous avez besoin d'autres fonctions mathématiques, je vous invite à consulter la documentation de Python : https://docs.python.org/3/library/math.html

#7 Quelles sont les valeurs associées aux noms suivants : d, e, f, g, h et i après l'exécution du programme suivant :

import math
a = 5
b = 16
c = 3.14 / 2
d = b / a
e = b // a
f = b % a
g = math.pow(a,2)
h = math.sqrt(b)
i = math.sin(c)
#a = 25
#b = 4
#c = 0.9999996829318346
#d = 16/5
#e = 3 avec un reste de 5
#f = 1
print(f)

#8
#Quel est le type du résultat d'une addition d'un integer et d'un float ?
int = 23949894
float = 49.3345
print(int + float)