import matplotlib.pyplot as plt
from math import *

#définition de la fonction suiteM
def suiteM(c):
    """
    fonction qui renvoie qui renvoie un booléen caractérisant
    l'appartenance d'un nombre complexe à l'ensemble de Mandelbrot

    Entrée : c, complexe
    Sortie : booléen
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
    #par colonnes
    for i in range(n):
        #par lignes
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
        if suiteM(affixe)==True: #si il appartient à l'ensemble de Mandelbrot, on l'ajoute
            listeX.append(point[0])
            listeY.append(point[1])
    return (listeX, listeY)



#SCRIPT TRACE NOIR ET BLANC DU GRAPHIQUE

#création du plan
plan=rectangle(-1.5, 0.5, -1, 1, 100)

#création des listes des coordonnées
tupleCoord=creerListManNB(plan)

#tracé
plt.figure(figsize=(10, 10), dpi=96)
plt.plot(tupleCoord[0], tupleCoord[1], ",k")
plt.axis("equal")
plt.show()


#SCRIPT TRACE MOTIFS SIMILAIRES

#Motif 1

#création du plan
plan=rectangle(-1.4, -0.6, -0.4, 0.4, 100)

#création des listes des coordonnées
tupleCoord=creerListManNB(plan)

#tracé
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(tupleCoord[0], tupleCoord[1], ",k")
plt.axis("equal")


#Motif 2

#création du plan
plan=rectangle(-1.4, -1.2, -0.1, 0.1, 100)

#création des listes des coordonnées
tupleCoord=creerListManNB(plan)

#tracé
plt.subplot(1, 2, 2)
plt.plot(tupleCoord[0], tupleCoord[1], ",k")
plt.axis("equal")

#affichage
plt.show()

#Motif 3

#création du plan
plan=rectangle(-1.4, -1.36, -0.022, 0.022, 300)

#création des listes des coordonnées
tupleCoord=creerListManNB(plan)

#tracé
plt.figure(figsize=(10, 10), dpi=96)
plt.plot(tupleCoord[0], tupleCoord[1], ",k")
plt.axis("equal")
plt.show()

#------------------------------------------------"

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

#SCRIPT TRACE EN COULEUR
n=200
plan=rectangle(-1.5, 0.5, -1, 1, 800)
listePoints=creerListManCoul(plan, n)

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


plt.figure(figsize=(10, 10), dpi=96)
coeffs=coeffsRVB(n)
for i in range(n+1):
    longueur=len(listePoints[i])
    listeX=[listePoints[i][k][0] for k in range(longueur)]
    listeY=[listePoints[i][k][1] for k in range(longueur)]
    plt.plot(listeX, listeY, ",", color=coeffs[i])

plt.show()

#------------------------------------------------#

#Ensemble de Julia

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

#définition de la fonction creerListeJuliaNB
def creerListeJuliaNB(L, c):
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
        if suiteJ(c, affixe)==True: #si il appartient à l'ensemble de Julia, on l'ajoute
            listeX.append(point[0])
            listeY.append(point[1])
    return (listeX, listeY)

#création des listes des coordonnées
plan=rectangle(-1.5, 1.5, -1.5, 1.5, 600)
tupleCoord=creerListeJuliaNB(plan, 0.3+0.5j)#on peut essayer avec -0.8+0.2j

#tracé
plt.figure(figsize=(10, 10), dpi=96)
plt.plot(tupleCoord[0], tupleCoord[1], ",k")
plt.axis("equal")
plt.show()

#Fin DM


#PERSO JULIA COULEUR (TOUS DROITS RESERVES)
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

#TRACE COULEUR JULIA
n=200
c=0.3+0.5j
plan=rectangle(-1.5, 1.5, -1.5, 1.5, 800)
listePoints=creerListeJuliaCoul(plan, c, n)
plt.figure(figsize=(10, 10), dpi=96)
coeffs=coeffs2RVB(n)
for i in range(n):
    longueur=len(listePoints[i])
    listeX=[listePoints[i][k][0] for k in range(longueur)]
    listeY=[listePoints[i][k][1] for k in range(longueur)]
    plt.plot(listeX, listeY, ",", color=coeffs[i])
plt.show()
