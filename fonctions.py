import matplotlib.pyplot as plt
from math import *
from random import randint
import os

#définition de la fonction suiteM
def suiteM(c):
    """
    fonction qui renvoie qui renvoie un booléen caractérisant
    l'appartenance d'un nombre complexe à l'ensemble de Mandelbrot

    Entrée : c, complexe
    Sortie : True si c appartient
             False si c n'appartient pas
    """
    z=0
    n=0
    appartenance=True
    while abs(z)<2 and n<200: #tant que le module est inf à 2
        n=n+1
        z=z**2+c
        
    if n!=200: #si boucle s'est terminée à cause du module
        appartenance=False
        
    return appartenance

#définition de la fonction rectangle
def rectangle(xmin, xmax, ymin, ymax, n):
    """
    fonction qui renvoie une liste de tuples représentants les coordonnées des
    points d'un plan
    Entrées : -xmin, flottant,borne du bas du plan
              -xmax, flottant,borne du haut du plan
              -ymin, flottant,borne de gauche du plan
              -ymax, flottant,borne de droite du plan
              -n, entier positif, subdiviseur des intervalles
    Sortie : liste de tuples représentants n² points
    """
    pasX=(xmax-xmin)/(n-1)
    pasY=(ymax-ymin)/(n-1)
    liste=[]
    for i in range(n):
        for k in range(n):
            liste.append((xmin+pasX*k, ymin+pasY*i))
    return liste

#définition de la fonction creerListManNB
def creerListManNB(coords):
    """
    fonction qui renvoie 2 listes contenant les abscisses et les ordonnées
    des points dont l'affixe appartient à l'ensemble de Mandelbrot
    Entrée : liste de tuples contenant les coordonnées des points
    Sortie : tuple de deux listes
    """
    listeX=[]
    listeY=[]
    for point in coords:
        affixe=complex(point[0],point[1]) #on détermine l'affixe du point
        if suiteM(affixe)==True: #si il appartient à l'ensemble de Mandelbrot
            listeX.append(point[0])
            listeY.append(point[1])
    return (listeX, listeY)

#définition de la fonction suiteFract1
def suiteFract1(c, nmax):
    """
    fonction qui renvoie le nombre d'itérations nécessaires
    pour avoir le module de Zn supérieur à 2 ou une borne si il
    y a plus d'itérations que celle-ci
    Entrées : -c, complexe
              -nmax, entier positif, borne de l'itérateur
    Sortie : entier
    """
    z=0
    n=0
    appartenance=True
    while abs(z)<2 and n<nmax: #tant que le module est inf à 2
        n=n+1
        z=z**2+c
        
    return n

#définition de la fonction creerListManCoul
def creerListManCoul(coords, n):
    """
    fonction qui renvoie une liste de listes de tuples représentants
    les points dont le module de l'affixe est inférieur à 2 en fonction du nombre d'itérations
    La dernière liste de points est celle dont le nombre d'itérations est égal à la borne donnée
    Entrées : -coords, liste de tuples représentants les points
              -n, entier positif, borne de l'itérateur
    Sortie : liste de n+1 listes de tuples
    """
    #liste de n+1 listes
    listeDeListes=[]
    for i in range(n+1):
        listeDeListes.append([])

    #remplissage des listes
    for point in coords:
        affixe=complex(point[0], point[1])#on prend l'affixe du point
        nNecessaire=suiteFract1(affixe, n)#puis le rang à partir duquel abs(Zn)>2
        listeDeListes[nNecessaire].append(point)#on ajoute le tuple dans la liste correspondante
    return listeDeListes

#définition de la fonction suiteJ
def suiteJ(c, z):
    """
    fonction qui renvoie un booléen selon l'appartenance d'un nombre complexe
    à l'ensemble de Julia d'un paramètre donné
    Entrée : -z, nombre complexe
             -c, nombre complexe, paramètre de l'ensemble de Julia
    Sortie : booléen
    """
    n=0
    appartenance=True
    while abs(z)<2 and n<200: #tant que le module est inf à 2
        n=n+1
        z=z**2+c
        
    if n!=200: #si boucle s'est terminée à cause du module
        appartenance=False
        
    return appartenance


#fonction artistique
def coeffsRVB(n):
    """
    fonction qui renvoie une liste de n+1 tuples contenants des coeffs RVB
    selon une alternance vert-bleu nuancée, et dont le dernier est du bleu
    """
    liste=[]
    for k in range(n):
        coeffV=exp(-14*(k/n))
        if k%2==0:
            coeffB=1-coeffV
        else:
            coeffB=coeffV
        liste.append((0, coeffV, coeffB))
    liste.append((0, 0, 1))
    return liste

#définition de la fonction creerListeJuliaNB
def creerListeJuliaNB(L, c, n):
    """
    fonction qui renvoie 2 listes contenant les abscisses et les ordonnées
    des points dont l'affixe appartient à l'ensemble de Julia d'un paramètre donné
    Entrée : - L, liste de tuples contenant les coordonnées des points
             - c, paramètre de l'ensemble de Julia
    Sortie : tuple de deux listes
    """
    listeX=[]
    listeY=[]
    for point in L:
        affixe=complex(point[0],point[1]) #on détermine l'affixe du point
        if suiteJ2(c, affixe, n)==True: #si il appartient à l'ensemble de Julia
            listeX.append(point[0])
            listeY.append(point[1])
    return (listeX, listeY)

#définition de la fonction suiteFract2
def suiteFract2(z, c, nmax):
    """
    fonction qui renvoie le nombre d'itérations nécessaires
    pour avoir le module de Zn supérieur à 2 ou une borne si il
    y a plus d'itérations que celle-ci
    Entrées : -z, premier terme de la suite
              -c, complexe
              -nmax, entier positif, borne de l'itérateur
    Sortie : entier
    """
    n=0
    appartenance=True
    while abs(z)<2 and n<nmax: #tant que le module est inf à 2
        n=n+1
        z=z**2+c
        
    return n

#définition de la fonction creerListeJuliaCoul
def creerListeJuliaCoul(coords, c, n):
    """
    fonction qui renvoie une liste de listes de tuples représentants
    les points dont le module de l'affixe est inférieur à 2 en fonction du nombre d'itérations
    La dernière liste de points est celle dont le module de l'affixe des points est inférieur ou égal à 2
    Entrées : -coords, liste de tuples représentants les points
              -c, paramètre de l'ensemble de Julia
              -n, entier
    Sortie : liste de n+1 listes de tuples
    """
    #liste de n+1 listes
    listeDeListes=[]
    for i in range(n+1):
        listeDeListes.append([])

    #remplissage des listes
    for point in coords:
        affixe=complex(point[0], point[1])#on prend l'affixe du point
        nNecessaire=suiteFract2(affixe, c, n)#puis le rang à partir duquel abs(Zn)>2
        listeDeListes[nNecessaire].append(point)#on ajoute le tuple dans la liste correspondante
    return listeDeListes

def coeffs2RVB(n):
    """
    fonction qui renvoie une liste de n+1 tuples contenants des coeffs RVB
    """
    liste=[]
    for k in range(n):
        x=k/n
        coeffR=-2*x*(x-1)
        coeffV=(-exp(-5*x)+1)/1.1
        coeffB=-exp(-10*x)+1
        liste.append((coeffR, coeffV, coeffB))
    return liste

def suiteJ2(c, z, n):
    """
    fonction qui renvoie un booléen selon l'appartenance d'un nombre complexe
    à l'ensemble de Julia d'un paramètre donné
    Entrée : -z, nombre complexe
             -c, nombre complexe, paramètre de l'ensemble de Julia
             -n, entier positif, borne de l'itérateur de la suite
    Sortie : booléen
    """
    i=0
    appartenance=True
    while abs(z)<2 and i<n: #tant que le module est inf à 2
        i=i+1
        z=z**2+c
        
    if i!=200: #si boucle s'est terminée à cause du module
        appartenance=False
        
    return appartenance

def ensembleJulia(c=0.3+0.5j, r=100, n=200, color=False, frmt="png"):
    """
    fonction qui affiche l'ensemble de Julia selon les paramètres donnés
    
    Entrées : -c, nombre complexe, paramètre de l'ensemble de Julia
              -r, entier positif, résolution du plan
                  ex : r=100, plan à 1000 points
              -n, entier positif, borne de l'itérateur de la suite
              -color, booléen, couleur si True, NB si False
    """
    plan=rectangle(-1.5, 1.5, -1.5, 1.5, r)
    if color==True:
        listePoints=creerListeJuliaCoul(plan, c, n)
        coeffs=coeffs2RVB(n)
        plt.figure(figsize=(10, 10), dpi=96)
        for i in range(n):
            longueur=len(listePoints[i])
            listeX=[listePoints[i][k][0] for k in range(longueur)]
            listeY=[listePoints[i][k][1] for k in range(longueur)]
            plt.plot(listeX, listeY, ",", color=coeffs[i])
        plt.axis("equal")
        plt.title("Graphe avec c = "+str(c))
        os.chdir("E:/PTSI/Informatique/DM/DM_2/essais")
        try:
            os.mkdir(str(c))
        except OSError:
            pass
        plt.savefig(str(c)+"/"+str(r)+"_color."+frmt)
    else:
        listePoints=creerListeJuliaNB(plan, c, n)
        plt.figure(figsize=(10, 10), dpi=96)
        plt.plot(listePoints[0], listePoints[1], ",k")
        plt.axis("equal")
        plt.title("Graphe avec c = "+str(c))
        os.chdir("E:/PTSI/Informatique/DM/DM_2/essais")
        try:
            os.mkdir(str(c))
        except OSError:
            pass
        plt.savefig(str(c)+"/"+str(r)+"_nb."+frmt)

ensembleJulia(color=True)