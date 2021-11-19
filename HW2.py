# -*- coding: utf-8 -*-
'''
Anche nella poesia, così come nella musica, esiste la nozione di ritmo.
In musica, il ritmo è quella proprietà della canzone che stai ascoltando che ti fa
battere il piede o le mani a tempo, o ti guida mentre stai ballando.
Analogamente, anche le poesie o i poemi non scritti in versi liberi hanno un ritmo, determinato
dalle sillabe che compongono le parole dei loro versi.
Alcune poesie o poemi poi hanno un ritmo sempre uguale in ogni riga, mentre altri hanno un ritmo
che cambia leggermente tra una riga e la successiva.
Vorremmo quindi provare a stimare quanto una poeasia o poema è regolare o irregolare in termini di ritmo
contenuto nei versi. Un ritmo regolare significa che le varie righe della poesia o poema
hanno tutte esattamente lo stesso ritmo, diremo quindi che sono in sync.
Al contrario, un ritmo irregolare varie ad ogni riga, diremo quindi in quel caso che le
righe della poesia o poema sono out of sync.

Ogni parola in qualunque lingua è composta di sillabe che vengono pronunciate usando l'intonazione della
voce per dare loro un accento più o meno forte. Ad esempio, in italiano la parola "casa" ha un accento
sulla prima sillaba. Esiste un modo per specificare questo, si chiama trascrizione fonetica
di una parola: nell'esempio, la trascrizione fonetica di casa è kˈaza, dove l'apostrofo
indica che sulla prima sillaba (ka) c'è un accento primario.

Vogliamo scrivere un programma che, dato un file di testo con encoding 'utf-8'
contenente i versi di una poesia o poema divisi in un certo numero di righe 
(possono esserci anche righe vuote, che ignoreremo),
trovi gli accenti di ogni parola e quindi di tutta la poesia, mantenendo però la suddivisione
del testo per righe, com'era nel testo originale.
Per farlo, sfrutteremo due funzioni, "phones_for_word" e "stresses", del modulo "pronouncing"
(https://pronouncing.readthedocs.io/en/latest/).
Data quindi una riga (non vuota) della poesia, chiameremo la funzione phones_for_word su ogni parola,
ottenendo da essa la traduzione fonetica della parola (casa -> k'asa).
La funzione potrebbe restituire più di una traduzione fonetica per la stessa parola nel
caso di parole che possono essere pronunciate in diversi modi, in quel caso considereremo
solo la prima traduzione fonetica restituita.
A quel punto, chiameremo la funzione stresses che, data in input la traduzione phonetica
della parola, ci restituirà una stringa di accenti, in cui: 0=nessun accento, 1=accento primario,
2=accento secondario. Per il nostro scopo, considereremo solo gli accenti primari, quindi
tralasceremo i secondari considerandoli come assenza di accento (come se fossero degli zeri).
Inoltre, nel tradurre frasi intere in accenti, aggiungeremo uno zero tra ogni coppia di parole
(vedi anche Nota 2 sotto).

Nota 1: nel tradurre parole in fonemi, la funzione phones_for_word potrebbe restituire
una lista vuota (perché la parola è sconosciuta); in quel caso considereremo come accenti
corrispondenti alla parola una sequenza di zeri pari alla lunghezza della parola divisa
per due (parte intera del risultato); ad esempio, siccome "pierc" non ha traduzione
fonetica, considereremo come stringa di accenti "00"

Nota 2: per semplificare, ci sarà sempre uno zero extra dopo l'ultima parola di ogni riga

Ad esempio, dalla seguente riga di testo: "IN the midway of this our mortal life,"
otterremo la lista di accenti: [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
Perché:
IN -> ['IH0 N', 'IH1 N'] -> 0
spazio -> 0
the -> ['DH AH0', 'DH AH1', 'DH IY0'] -> 0
spazio -> 0
midaway - > ['M IH1 D W EY2'] -> 1,0
spazio -> 0
of -> ['AH1 V'] -> 1
spazio -> 0
this -> ['DH IH1 S', 'DH IH0 S'] -> 1
spazio -> 0
our -> ['AW1 ER0', 'AW1 R', 'AA1 R'] -> 1,0
spazio -> 0
mortal -> ['M AO1 R T AH0 L'] -> 1,0
spazio -> 0
life -> ['L AY1 F'] -> 1
spazio -> 0

Una volta tradotta tutta la poesia in sequenze di zeri e uni, avremo una lista di liste
di varie lunghezze, ad esempio:

IN the midway of this our mortal life,
I found me in a gloomy wood, astray
Gone from the path direct: and e'en to tell
It were no easy task, how savage wild
That forest, how robust and rough its growth,
Which to remember only, my dismay
Renews, in bitterness not far from death.

[
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
]

Vogliamo trasformare questa lista di liste in una matrice di accenti,
aggiungendo un opportuno numero di zeri alla fine delle righe
eventualmente più corte della riga più lunga:

[
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
]

A questo punto calcoliamo la sincronizzazione tra le tutte le coppie di righe
della matrice. Date due liste A e B, ciascuna di N valori 0 o 1, e un valore tau
compreso tra zero e N, definiamo l'indice di sincronizzazione tra A e B come:

       0.5 * (c(B|A) + c(A|B))
Sync = -----------------------
          sqrt(m(A)*m(B))

Dove:
    - c(B|A) è il numero di volte in cui un accento di B è preceduto da un accento di A 
      a una distanza <= tau
    - c(A|B) è il numero di volte in cui un accento di A è preceduto da un accento di A 
      a una distanza <= tau
    - m(A) è il numero di accenti in A
    - m(B) è il numero di accenti in B

e dove, ricordiamo, un valore di 1 in A o B rappresenta un accento.

NOTA: se m(A) == 0 o m(B) == 0 assumiamo come valore di Sync zero

Ad esempio, date le due sequenze:
    - A = [0, 0, 0, 0, 1, 0, 0, 1]
    - B = [1, 0, 1, 0, 1, 0, 0, 0]
    - tau = 3

avremo:
    - c(B|A) = 1, perché solo il terzo accento in B (posizione 4) è preceduto in A da un
      accento a una distanza inferiore o uguale a 3 (in questo caso l'1 in A coincide come
      posizione con l'1 in B)
    - c(A|B) = 2, perché entrambi gli accenti di A sono preceduti in B da due accenti entro
      3 posizioni
    - m(A) = 2
    - m(B) = 3
    - Sync = 0.5 * (1 + 2) / sqrt(2 * 3) = 0.6123724356957946

Data una poesia o poema in input, definiamo l'indice di sincronizzazione del testo come
la media tra i valori di Sync tra tutte le coppie di righe  di accenti (A1, A2)
dove A1 e A2 non sono la stessa lista
NOTA: due liste diverse possono comunque contenere gli stessi valori

Scrivere la funzione PoemSync che, dati in input:
- il path di un file di testo contenente una poesia
- il path del file di output in cui salvare la matrice di accenti
- il valore (intero) di tau

svolga le seguenti operazioni:
- apra il file della poesia e calcoli la matrice degli accenti
- salvi la matrice degli accenti nel file il cui path è specificato in input, nel formato specificato
- calcoli e ritorni l'indice di sincronizzazione del testo, arrotondato
  alla sesta cifra decimale (es: 0.6123724356957946 -> 0.612372)

nota: tornando alla matrice degli accenti riportata sopra, il file generato
da PoemSync conterrà:

000010010101001001000
101010000010010010000
101000100100010101010
101010100101010010000
101001001000101010000
101001001001001000000
010001000101010100000


ESEMPIO DI ESECUZIONE:

PoemSync("example.txt", "example.out.txt", 2)

contenuto di example.txt:
No one can tell me
Where the wind comes from
Where the wind comes from

no one can tell me
['no', 'one', 'can', 'tell', 'me']
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
where the wind comes from
['where', 'the', 'wind', 'comes', 'from']
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
where the wind comes from
['where', 'the', 'wind', 'comes', 'from']
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]

matrix:
1010101010
1000101010
1000101010

sync tra a=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (5, 5)
sync = 1.0062305898749053

sync tra a=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (5, 5)
sync = 1.0062305898749053

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (5, 5) (c(a|b), m(a)) = (4, 4)
sync = 1.0062305898749053

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (4, 4)
sync = 1.0

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (5, 5) (c(a|b), m(a)) = (4, 4)
sync = 1.0062305898749053

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (4, 4)
sync = 1.0

PoemSync = 1.004154

TIMEOUT: 0.5s

'''

import pronouncing
import math

def Estrai(F):
    with open(F, encoding='utf8', mode='rt') as F:
        lines = F.readlines()
    matrice=[]
    for line in lines:
            caratteri = set(line)
            for c in caratteri:
                if not c.isalpha():
                    line = line.replace(c, ' ')
            line=line.split()
            l=[]
            for i in range(len(line)):
                acc=pronouncing.phones_for_word(line[i])
                if acc!=[]:
                    n=pronouncing.stresses(acc[0])
                    for c in n:
                        
                        if c!='2':
                            l.append(int(c))
                        else:
                            
                            l.append(0)
                else:
                    for y in range(len(line[i])//2):
                          l.append(0)      
                
                l.append(0)
                
            if l!=[]:
                matrice.append(l)
    F.close()
    return matrice


def Matrice(F,F1): 
    
    matrice=Estrai(F)
    lunghezzamax=len(max(matrice, key=len))
    
    for i in range(len(matrice)):
        lun=len(matrice[i])
        if lun!=0:
            d=lunghezzamax-lun
            matx=matrice[i]
            matx[lun:lun+d]=[0]*d
    matricestr=str(matrice)
    with open(F1, 'w', encoding='utf-8') as F1:
        i=matricestr.replace(",", "")
        i=i.replace("[", "")
        i=i.replace("]", "\n")
        i=i.replace(" ","")
        i=i[:-1]
        F1.write(i)
        F1.close()

    return matrice


def Presync(a,b,tau):
    cab=0
    cba=0
    for j in range(len(a)):
        if b[j]==1:
            if j<=tau:
                x=a[0:j+1]
                if 1 in x:
                    cba+=1 
            else:
                x=a[j-tau:j+1]
                if 1 in x:
                    cba+=1 
        if a[j]==1:
            if j<=tau:
                x=b[0:j+1]
                if 1 in x:
                    cab+=1 
            else:
                x=b[j-tau:j+1]
                if 1 in x:
                    cab+=1  
    return cba,cab

def Sync(matrice,tau):
    sync=0.0
    s=0

    for i in range(len(matrice)-1):
        for e in range(i+1,len(matrice)):
            a=matrice[i]
            b=matrice[e]
            ma=0
            mb=0
            ma=a.count(1)
            mb=b.count(1)
            if ma!=0 and mb!=0 and i!=e:
                    cba,cab=Presync(a,b,tau)
                    sync+=(0.5*(cab+cba)/(math.sqrt(ma*mb)))
            s+=1
            
    sync=sync/s
    return sync

def PoemSync(inputfilename, outputfilename, tau):
    matrice=Matrice(inputfilename,outputfilename)
    sync=Sync(matrice,tau)
    roundup=round(sync,6)
    return roundup

    pass

if __name__ == "__main__":
    
    pass
