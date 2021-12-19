
'''

Un pixel artist di fama mondiale di nome Fred Zuppa ha recentemente
prodotto diversi capolavori sottoforma di immagini quadrate raster
codificate su pixels in scala di grigi. Le immagini che ha disegnato
possono prendere valori da 0 a 255 compresi. Sfortunatamente le famose
opere sono andate perdute in quanto il suo disco rigido (ahilui!) ha
smesso di funzionare e ovviamente il buon Fred e' disperato. I
programmi per recuperarle dal filesystem non funzionano purtroppo e
cosi' Fred si affida al suo amico informatico di fiducia, il quale gli
dice:

   "Fratello, in verita' ti dico, se ti ricordi la dimensione delle
   immagini e i valori dei pixel di cui erano formate e delle
   proprieta' particolari delle tue opere, allora possiamo provare a
   scrivere un generatore ricorsivo che le produca tutte in base ai
   tuoi input, cosi' facendo possiamo provare a recuperarle!"

Il mattino seguente Fred riesce a dare le informazioni necessarie
sottoforma di:
   1. `D` parametro intero che descrive la dimensione dell'immagine
       quadrata.
   2. `colors` una lista di interi che descrive i colori delle
      immagini di Fred.  I colori di Fred sono compresi fra 0, 255.
      colors puo' essere quindi [128, 0, 255] mentre NON puo' essere
      [-100, 999]
   3. Un testo `img_properties` che descrive le proprieta' delle sue
      immagini: Il testo puo' descrivere nessuna proprita' (stringa
      vuota) oppure puo' descrivere una proprieta' che riguarda i
      pattern che le immagini devono contenere.

       Ad esempio:

       Se `img_properties` e' vuota allora le immagini non devono soddisfare
       nessuna proprieta'. Viceversa se `img_properties` e' uguale a
       'pattern_{type}_' allora signifca che le immagini devono
       mostrare il pattern di tipo `type` specificato nella stringa.
       Il pattern puo' essere di un solo tipo.

       I tipi di pattern possibili sono i quattro seguenti:
          a) 'pattern_diff_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve avere i
          pixel di colore tutti diversi.

                 valid        not valid
            |  96 | 255 |   |   0 | 255 |
            | 128 |   0 |   | 255 |  96 |


          b) 'pattern_cross_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve
          avere i pixel sulla diagonale uguali fra loro e i pixel
          sulla antidiagonale uguale fra loro ma pixel delle due
          diagonali devono essere diverse.

               valid          not valid     not valid
            |  96 | 255 |   |  0 | 255 |   | 61 | 61 |
            | 255 |  96 |   | 96 |   0 |   | 61 | 61 |

          c) 'pattern_hrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle righe tutti uguali ma righe adiacenti di colore
          diverso.

                 valid       not valid        not valid
            |   0 |   0 |   | 255 | 255 |    | 43 | 43 |
            | 128 | 128 |   | 0   | 255 |    | 43 | 43 |

          d) 'pattern_vrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle colonne tutti uguali ma colonne adiacenti di colore
          diverso.

                valid         not  valid    not valid
             | 0 | 255 |     | 0  | 0  |    | 22 | 22 |
             | 0 | 255 |     | 0  | 255|    | 22 | 22 |

Implementare la funzione ricorsiva o che usa metodi ricorsivi:
  
      images = ex(colors, D, img_properties)

che prende in ingresso la lista di colori `colors`, la dimensione
delle immagini `D` e una stringa `img_properties` che ne descrive le
proprieta' e generi ricorsivamente tutte le immagini seguendo le
proprieta' suddette.  La funzione deve restituire l'elenco di tutte le
immagini come una lista di immagini.  Ciascuna immagine e' una tupla di
tuple dove ogni intensita' di grigio e' un intero.
L'ordine in cui si generano le immagini non conta.

     Esempio: immagine 2x2 di zeri (tutto nero) e':
        img = ( (0, 0), (0, 0), )


Il timeout per ciascun test è di 1 secondo.

***
E' fortemente consigliato di modellare il problema come un albero di
gioco, cercando di propagare le solo le "mosse" necessarie nella
ricorsione e quindi nella costruzione della soluzione in maniera
efficiente; oppure, in maniera alternativa, cercate di "potare" l'albero di
gioco il prima possibile.
***

Potete visualizzare tutte le immagini da generare invocando

     python test_01.py data/images_data_15.json

questo salva su disco tutte le immagini attese del test 15 e crea
un file HTML di nome `images_data_15.html` nella directory radice
del HW con cui e' possibile vedere le immagini aprendo il file html
con browser web.
'''

def p(colors,D):
    li=[]
    immagine=[]
    if D==1:
        immagine=(pattern_(colors,li,0,len(colors),[]))
    else:
        immagine=pd2(colors,D) 
              
    return immagine

def pd2(colors,D): 
    immagine=pattern1(colors,D)
    immagine=pattern1(immagine,D)
    img=[]
    for i in immagine:
        im=[]
        for j in i:
            im.append(tuple(j))
        img.append(tuple(im))
    return img  

def pattern1(colore,d): 
     if d==1:
         return [[c] for c in colore]
     else:
        li=[]
        immagine=pattern1(colore,d-1)
        
        for i in colore:
            for j in immagine:
                li.append(([i]+j))
        return li
    
def pattern_(colore,li,i,n,img=[]): 
    if len(li) == 1:
        return 
 
    for j in range(i,n):
        li.append(colore[j])
        pattern_(colore,li, j, n)
        le=[]
        le.append(tuple(li))
        img.append(tuple(le))
        li.pop()
    return img
  
def pattern2(colore,d): 

     if d==1:
         return [[c] for c in colore]
     else:
        li=[]
        immagine=pattern2(colore,d-1)
        
        for i in colore:
            for j in immagine:
                im=delvrect(([i]+j))
                if im:
                    li.append(im)
        return li

def tupl(immagine,d):
    img=[]
    im=[]
    for i in range(len(immagine)):
        for j in range(len(immagine[i])):
            img.append(tuple(immagine[i][j]))
            if len(img)%d==0:
                im.append(tuple(img))
                img=[]
    return im

def pattern_vrect_(colore,d): 

    immagine=pattern2(colore,d)
    img=[]
    for i in range(len(immagine)):
        img.append(([immagine[i]])*d)
    mi=tupl(img,d)
    return mi

def delhrect(immagine):
    li=[]
    for i in immagine:
        for j in range(len(i)-1):
            if i[j]==i[j+1]:
                c=0
                break
            else:
                c=1
        if c==1:
            li.append(tuple(i))
    return li

def delcross(immagine):
    li=[]
    c=0
    for i in immagine:
        for j in range(len(i)-2):
            if i[j]==i[j+2] and i[j]!=i[j+1] :
                c=0
            else:
                c=1
                break
        if c==0 and i[0]!=i[1]:
            li.append(tuple(i))
    return li

def pattern_cross_(colore,d):
    im=[]
    immagine=pattern1(colore,d)
    immagine=delcross(immagine)
    for i in immagine:
        img=[]
        for j in range(d//2):
            img.append(i)
            if (len(i)%2)!=0:
                img.append(i[1:]+i[1:2])
                if j==(d//2)-1:
                    img.append(i)
            else:
                img.append(i[::-1])
        im.append(tuple(img))
        
    return im

def pattern_hrect_(colore,d):

    img=[]
    for i in range(len(colore)):
        img.append(tuple(([colore[i]])*d))
    immagine=pattern1(img,d)
    immagine=delhrect(immagine)

    return immagine


def delvrect(immagine):
    li=[]
    for i in range(len(immagine)-1):
        if immagine[i]==immagine[i+1]:
            c=0
            break
        else:
            c=1
    if c==1:
        for i in range(len(immagine)):
            li.append(immagine[i])
        return li

                    
def maestro(immagine,d): 
    img=[]
    im=[]
    ir=[]
    for i in range(len(immagine)):
            img.append(immagine[i])
            if len(img)==d:
                im.append(tuple(img))
                img=[]
            if len(im)==d:
                ir.append(tuple(im))
                im=[]
    return ir
    
def pattern3(colore,d,im):
        if len(im)==d*d:
            return im
        li=[]
        for i in colore:
            if len(im)<d:
                if len(im)==0:
                    p=pattern3(colore, d, im+[i])
                    [li.append(n) for n in p]
                else:
                    if im[-1]!=i:
                        p=pattern3(colore,d,im+[i])
                        [li.append(n) for n in p]
            
            else: 
                if len(im)%d==0:
                    if im[-d]!=i and im[-d+1]!=i:
                        p=pattern3(colore,d,im+[i])
                        [li.append(n) for n in p]
                elif len(im)%d==((d*d)-1)%d:
                    if im[-d]!=i and im[-d-1]!=i and im[-1]!=i:
                        p=pattern3(colore,d,im+[i])
                        [li.append(n) for n in p]
                else:
                    if im[-d]!=i and im[-d-1]!=i and im[-1]!=i and im[-d+1]!=i:
                        p=pattern3(colore,d,im+[i])
                        [li.append(n) for n in p]
        return li         
        

def pattern_diff_(colore,d):
    
    i=pattern3(colore,d,[])
    i=maestro(i, d)

    return i
    
def ex(colors, D, img_properties):
   if max(colors)>255 or min(colors)<0: return
    
   if img_properties=='pattern_diff_':
       immagine=pattern_diff_(colors,D)
       
   elif img_properties=='pattern_cross_':
       immagine=pattern_cross_(colors,D)
        
   elif img_properties=='pattern_hrect_':
        immagine=pattern_hrect_(colors,D)
   
   elif  img_properties=='pattern_vrect_':
        immagine=pattern_vrect_(colors,D)
   else:
        immagine=p(colors,D)
   return immagine
   pass

if __name__ == '__main__':

    pass
