"""
La fonction deciToHexa prends un seul param, un int N positif
Elle en renvéra l'équivalent en bi,aire sous forme d'un str
"""

def deciToBin(n):
    reply = ""
    while n>0:
        reply = str(n%2) + reply
        n = n//2
    return "0" + reply


"""La fonction binToDeci prends un seul param, un str N sous forme d'un binaire sans préfixe (0b)
Elle en renvéra l'équivalent en décimal sous forme d'un int"""

def binToDeci(n):
    reply = int()
    nbr = str(n)
    nbr_len = len(nbr) - 1
    while(nbr.find("1") != -1):
        yolo = nbr.find("1")
        print(nbr_len - yolo)
        reply = 2 ** (nbr_len - yolo) + reply
        old = "0" * yolo
        nbr = nbr.replace(old+'1', '0')
    return(reply)
