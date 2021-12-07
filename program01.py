#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 
Il sindaco si una cittÃ  deve pianificare un nuovo quartiere.  Voi fate
parte dello studio di architetti che deve progettare il quartiere.  Vi
viene fornito un file che contiene divisi in righe, le informazioni
che descrivono in pianta le fasce East-West (E-W) di palazzi, ciascuno
descritto da larghezza, altezza, colore da usare in pianta.

I palazzi devono essere disposti in pianta rettangolare
in modo che:
  - tutto intorno al quartiere ci sia una strada di larghezza minima
    indicata.
  - in direzione E-W (orizzontale) ci siano le strade principali,
    dritte e della stessa larghezza minima, a separare una fascia di
    palazzi E-W dalla successiva.  Ciascuna fascia E-W di palazzi puÃ²
    contenere un numero variabile di palazzi.  Se una fascia contiene
    un solo palazzo verrÃ  disposto al centro della fascia.
  - in direzione North-South (N-S), tra ciascuna coppia di palazzi
    consecutivi, ci dev'essere almeno lo spazio per una strada
    secondaria, della stessa larghezza minima delle altre.

Vi viene chiesto di calcolare la dimensione minima dell'appezzamento
che conterrÃ  i palazzi.  Ed inoltre di costruire la mappa che li
mostra in pianta.

Il vostro studio di architetti ha deciso di disporre i palazzi in modo
che siano **equispaziati** in direzione E-W, e di fare in modo che
ciascuna fascia E-W di palazzi sia distante dalla seguente dello
spazio minimo necessario alle strade principali.

Per rendere il quartiere piÃ¹ vario, il vostro studio ha deciso che i
palazzi, invece di essere allineati con il bordo delle strade
principali, devono avere se possibile un giardino davanti (a S) ed uno
dietro (a N) di uguale profonditÃ .  Allo stesso modo, dove possibile,
lo spazio tra le strade secondarie ed i palazzi deve essere
distribuito uniformemente in modo che tutti possano avere un giardino
ad E ed uno a W di uguali dimensioni.  Solo i palazzi che si
affacciano sulle strade sul lato sinistro e destro della mappa non
hanno giardino su quel lato.

Vi viene fornito un file txt che contiene i dati che indicano quali
palazzi mettere in mappa.  Il file contiene su ciascuna riga, seguiti
da 1 virgola e/o 0 o piÃ¹ spazi o tab, gruppi di 5 valori interi che
rappresentano per ciascun palazzo:
  - larghezza
  - altezza
  - canale R del colore
  - canale G del colore
  - canale B del colore

Ciascuna riga contiene almeno un gruppo di 5 interi positivi relativi
ad un palazzo da disegnare. Per ciascun palazzo dovete disegnare un
rettangolo del colore indicato e di dimensioni indicate

Realizzate la funzione ex(file_dati, file_png, spaziatura) che:
  - legge i dati dal file file_dati
  - costruisce una immagine in formato PNG della mappa e la salva nel
    file file_png
  - ritorna le dimensioni larghezza,altezza dell'immagine della mappa

La mappa deve avere sfondo nero e visualizzare tutti i palazzi come segue:
  - l'argomento spaziatura indica il numero di pixel da usare per lo
    spazio necessario alle strade esterne, principali e secondarie,
    ovvero la spaziatura minima in orizzontale tra i rettangoli ed in
    verticale tra le righe di palazzi
  - ciascun palazzo Ã¨ rappresentato da un rettangolo descritto da una
    quintupla del file
  - i palazzi descritti su ciascuna riga del file devono essere
    disegnati, centrati verticalmente, su una fascia in direzione
    E-W della mappa
  - i palazzi della stessa fascia devono essere equidistanti
    orizzontalmente l'uno dall'altro con una **distanza minima di
    'spaziatura' pixel tra un palazzo ed il seguente** in modo che tutti
    i primi palazzi si trovino sul bordo della strada verticale di
    sinistra e tutti gli ultimi palazzi di trovino sul bordo della
    strada di destra
    NOTA se la fascia contiene un solo palazzo dovrÃ  essere disegnato
    centrato in orizzontale
  - ciascuna fascia di palazzi si trova ad una distanza minima in
    verticale dalla seguente per far spazio alla strada principale
    NOTE la distanza in verticale va calcolata tra i due palazzi piÃ¹
    alti delle due fasce consecutive. 
    Il palazzo piÃ¹ grosso della prima riga si trova appoggiato al
    bordo della strada principale E-W superiore. 
    Il palazzo piÃ¹ grosso dell'ultima riga si trova appoggiato al
    bordo della strada principale E-W inferiore 
  - l'immagine ha le dimensioni minime possibili, quindi:
     - esiste almeno un palazzo della prima/ultima fascia a
       'spaziatura' pixel dal bordo superiore/inferiore
     - esiste almeno una fascia che ha il primo ed ultimo palazzo a
       'spaziatura' pixel dal bordo sinistro/destro
     - esiste almeno una fascia che non ha giardini ad E ed O

    NOTA: nel disegnare i palazzi potete assumere che le coordinate
        saranno sempre intere (se non lo sono avete fatto un errore).
    NOTA: Larghezza e altezza dei rettangoli sono tutti multipli di due.
'''

import images

def verificanumero(i):
    n=''
    k=[]
    for j in i:
        if j.isalnum():
            n=n+str(j)
        else:
            if n!="":
                k.append(int(n))
                n=''
    return k
    
def Estrai_file(file):
    dati=[]
    with open(file, encoding='utf8', mode='rt') as F:
        for i in F.readlines():
           k=verificanumero(i)
           x=0
           l=[]
           for j in range(len(k)//5):
               l.append(k[x:x+5])
               x=x+5
           dati.append(l)
    F.close()
    return dati

def dimensionisfondo(dati):
    maxriga=0
    apamx=0
    for i in range(len(dati)):
        if len(dati[i])>maxriga:
            maxriga=len(dati[i])
            indice=i
        saltezza=0
        for j in range(len(dati[i])):
            if  saltezza<dati[i][j][1]:
                saltezza = dati[i][j][1]
        apamx+=saltezza
    return indice,maxriga,apamx
  
def Sfondo(dati,spazio,png):
    slarghezza=0
    indice,maxriga,apamx=dimensionisfondo(dati)
    for j in range(len(dati[indice])):
        slarghezza+=dati[indice][j][0]
    altezza=(spazio*(len(dati)+1))+apamx
    larghezza=(spazio*(maxriga+1))+slarghezza
    return [[ (0,0,0) ]*larghezza for i in range(altezza)]


def drawrectangle(s, x1,y1, x2,y2, dati):
    colore=dati[2],dati[3],dati[4]
    for x in range(x1, x2):
        for y in range(y1, y2):
           if  0 <= x < len(s[0]) and 0 <= y < len(s):
                s[y][x] = colore
    return s
                

def disegnoilpalazzo(dati,s,apm,x,y,spaziomezzo=0):
    for i in range(len(dati)):
        altezza=dati[i][1]
        larghezza=dati[i][0]
        if len(dati)==1:
            l=(len(s[0])//2)-(larghezza//2)
            drawrectangle(s, l,y, larghezza+l, altezza+y, dati[i])
        elif altezza==apm:
                drawrectangle(s, x,y, larghezza+x, altezza+y, dati[i])
        else:
                drawrectangle(s, x,y+(apm//2-altezza//2), larghezza+x, (altezza+(apm//2-altezza//2))+y, dati[i])
        x+=larghezza+spaziomezzo
    return s

def DrawPalace(dati,s,spazio,x,y,apm):
    lp=0
    if len(dati)>1:
        for i in range(len(dati)):
            lp+=dati[i][0]   
        spaziomezzo=(len(s[0])-(spazio*2+lp))//(len(dati)-1)
        disegnoilpalazzo(dati,s,apm,x,y,spaziomezzo)
    else:
        disegnoilpalazzo(dati,s,apm,x,y)
    return s
           
              
def Draw(dati,png,spazio):

    sfondo=Sfondo(dati,spazio,png)
    y=spazio
    for g in range(len(dati)):
        apm=0
        for i in range(len(dati[g])):
            if apm<dati[g][i][1]:
                apm=dati[g][i][1]
        img=DrawPalace(dati[g],sfondo,spazio,spazio,y,apm)
        y+=apm+spazio
        
    images.save(img,png)
    return img  
 
def ex(file_dati, file_png, spaziatura):
    dati=Estrai_file(file_dati)
    disegno=Draw(dati,file_png,spaziatura)
    return(len(disegno[0]),len(disegno))
    pass

if __name__ == '__main__':
    pass
