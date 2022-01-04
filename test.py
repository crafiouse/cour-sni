def nb_occurences(listes, num):
    occu = 0
    let = listes[num]
    for i in range (len(listes)):
        if listes[i]==let:
            occu = occu + 1
    return occu

def supprime_occurence(listes, num):
    let = listes[num]
    let1=[]
    for i in range (len(listes)):
        if listes[i]!=let:
            let1.append(listes[i])
    return let1


def retourne_impair(listes):
    br = []
    for i in range(len(listes)):
        if listes[i]%2!=0:
            br.append(listes[i])
    return br