# -*- coding: utf-8 -*-
'''Nel gioco "chi la spara più grossa" si sfidano due concorrenti A e
B che generano delle sequenze di valori di lunghezza variabile,
rappresentati da un singolo carattere. Le sequenze possono essere di
lunghezza diversa poiché i valori possono essere separati da uno (o
più) spazi bianchi e tab ('\t'). Il numero di caratteri non spazio è,
comunque, uguale per ogni sequenza.

Ogni elemento della sequenza di A viene confrontato con l'elemento
corrispondente della sequenza di B e viene assegnato un punto
- al concorrente che ha generato il valore più alto (per esempio A),
  se la differenza fra il valore di A e il valore di B è inferiore o
  uguale ad un parametro k deciso all'inizio della sfida
- al concorrente che ha generato il valore più basso (per esempio B),
  se la differenza fra il valore di A e il valore di B è superiore
  a k (cioè A ha sballato)
- a nessuno, in caso di pareggio.
Al termine dell'assegnazione, vince chi ha ottenuto più punti. In caso
di pareggio, vince il giocatore che ha generato la sequenza con somma
totale dei valori inferiore.  In caso di ulteriore pareggio, il punto
è assegnato al giocatore con la prima sequenza in ordine
lessicografico. Non può capitare che due giocatori generino
esattamente la stessa sequenza di valori.

Si deve realizzare una funzione che prende in input il parametro k e
una lista di stringhe corrispondenti a un torneo di "chi la spara più
grossa" e restituisce la classifica finale del torneo. La stringa in
posizione i corrisponde alla sequenza dei valori generati dal
giocatore i.

Nel torneo, ogni giocatore sfida tutti gli altri con la propria
sequenza: ovvero, se ci sono n giocatori, ogni giocatore farà n-1
sfide. Il numero di sfide vinte determina la posizione in
classifica. In caso di parità di sfide vinte, i giocatori sono
ordinati in modo crescente in base alla posizione.

Esempio di partite a chi la spara più grossa fra tre giocatori.
    Se k=2 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2.
        Alla fine 0 ha 1 sfida, 1 ha 2 sfide e 2 ha 0 sfide, per cui
            la classifica finale sarà [1, 0, 2].

    Se k=1 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 0 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 2 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        Alla fine 0 ha 2 sfide, 1 ha 0 sfide e 2 ha 1 sfida, per cui
            la classifica finale sarà [0, 2, 1].

    Se k=10 e la lista è  [ "abc",  "dba" , "eZo"]
        La sfida 0, 1 è un pareggio, ma vince 0 perché la sua sequenza
            ha somma inferiore.
        La sfida 0, 2 è vinta da 0 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'c'.
        La sfida 1, 2 è vinta da 1 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'a'
        Alla fine 0 ha 2 sfide, 1 ha 1 sfida e 2 ha 0 sfide, per cui
            la classifica finale sarà [0, 1, 2].

    Se k=50 e la lista è  [ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."]
        La sfida 0, 1 è vinta da 1 per 4 punti a 0.
        La sfida 0, 2 è vinta da 2 per 3 punti a 1.
        La sfida 1, 2 è vinta da 1 per 3 punti a 1.
        Alla fine 0 ha 0 sfide, 1 ha 1 sfida e 2 ha 2 sfide, per cui
        la classifica finale sarà [1, 2, 0].

Il timeout per l'esecuzione di ciascun test è di 6 secondi (*2 sualla VM)

'''
def punti(lista,k,classifica):
    l=len(lista)-1 
    i=0 
    while l>0: 
        j=i+1 
        while j<= len(lista)-1: 
            if lista[i]!=lista[j]: 
                pg1=0 
                pg2=0 
                for l1, l2 in zip (lista[i], lista[j]): 
                    l1=ord(l1) 
                    l2=ord(l2) 
                    d = l1-l2 
                    if d: 
                        if d<0:
                            d=d*(-1) 
                        if d<=k:
                            if l1>l2: 
                                pg1 +=1
                            else:
                                pg2 +=1
                        else:
                            if l1>l2: 
                                pg2 +=1
                            else:
                                pg1 +=1
                    
                classifica=punticlassifica(pg1,pg2,classifica,i,j,lista)
                
            j+=1
        i+=1
        l=len(lista)-i-1
    return classifica
def punticlassifica(pg1,pg2,classifica,i,j,lista):
    if pg1 < pg2:
        classifica[j] += 1 
                       
    elif pg1 == pg2:
        s1 = sum([ord(p) for p in lista[i]])
        s2 = sum([ord(p) for p in lista[j]])
                
        if s1 > s2:
            classifica[j] += 1
        elif s1 == s2:
            if lista[i] < lista[j]:
                classifica[i] += 1
            else:
                classifica[j] += 1
        else:
            classifica[i] += 1
    else:
        classifica[i] += 1
        
    return classifica
def ex(matches, k):

    lista = []
    for stringa in matches:
        string=""
        for i in stringa:
            if i != " " and i != "\t":
                string+=i
        lista.append(string)
        
#confronto le due sequenze
    
    classifica = dict() 
    for i in range(len(lista)):
        classifica[i]=0
    
    classifica=punti(lista,k,classifica)
    
    classificaordinata= dict(sorted(classifica.items(),key=lambda item:item[1],reverse=True))
    classificalista=[i for i in classificaordinata.keys()]
    return classificalista

            


if __name__ == "__main__":
    classific=ex([ "abc",  "dba" , "eZo"],10)
    print(classific)
