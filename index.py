# La fonction deciToBin prends un seul param, un int N positif
# Elle renvoie l'équivalent en binaire sans aucun préfixe sous la forme d'un str

def deciToBin(n):
    reply = ""
    while n > 0:
        reply = str(n%2) + reply
        n = n//2
    return "0" + reply


# La fonction binToDeci prends un seul param, un str N sous forme d'un binaire sans préfixe (0b)
# Elle en renvoie l'équivalent en décimal sous forme d'un int

def binToDeci(n):
    n = list(str(n)) #Découpe le str donné en param en list pour traiter chaque bit induviduellement
    l = len(n)       #Permet de connaitre le nombre de bits total
    r = int(0)       #Variable stockant le résultat, incrémenté à chaque bit positif dans la boucle suivante
    for n in range(l):
        r += int(i[n]) * (2**(l-n-1))
        # La formule de calcul suivante est un peu complexe et je vais me mettre un commentaire pour ne pas oublier comment elle fonctionne
        # En premier on chercher sur quel bit on travaille (i[n])
        # Étant donné que i[n] est sous la forme d'un STR au début, je le transforme en INT en assumant que l'utilisateur final n'est pas casse couile et ne va pasmettre une lettre
        # Puis je le multiplie i[n] par 2 puissance X
        # X est très important car pour le premier bit il doit être de 0
        # Car 1*(2^0) = 1*1 = 1 tandis que dans le 2eme bit ca doit être 1*2 puis dans le 3eme 2*4...
        # Pour trouver X je fais donc longueur totale (disons 6) - valeur actuelle (disons qu'on traite le 2eme bit donc c'est la 5ème répétition de la boucle) ce qui fait 2
        # Sauf que 2^2 = 4 alors que le 2eme bit doit être égal à 2^1 donc on fait au calcul valeur totale - valeur actuelle ce qui fait 2^1
        # Cette partie peut être optimisé mais F*** j'ai pas envie, peut-être plus tard :D
    return r

# La fonction deciToHexa prends un seul param, un int N positif (prck f*** les négatifs et les floats)
# Elle renvoie l'équivalent en hexadécimal sans aucun préfixe sous la forme d'un str

def deciToHexa(n):
    lettres = ["A", "B", "C", "D", "E", "F"]
    reply = ""
    while n > 0:
        m = n % 16
        if m < 10: reply = str(m) + reply
        else: reply = str(lettres[m-10]) + reply
        n = n // 16
    return reply