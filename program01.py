
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

def p(colors,D):#ok
    li=[]
    immagine=[]
    if D==1:
        immagine=(pattern_(colors,li,0,len(colors),[]))
    else:
        immagine=pd2(colors,D) 
              
    return immagine

def pd2(colors,D): #Propieta "" se D=1 OK
    immagine=pattern1(colors,D)
    immagine=pattern1(immagine,D)
    img=[]
    for i in immagine:
        im=[]
        for j in i:
            im.append(tuple(j))
        img.append(tuple(im))
    return img  

def pattern1(colore,d): #Propieta "" se D>1 OK
     if d==1:
         return [[c] for c in colore]
     else:
        li=[]
        immagine=pattern1(colore,d-1)
        
        for i in colore:
            for j in immagine:
                li.append(([i]+j))
        return li
    
def pattern_(colore,li,i,n,img=[]): #Propieta "" se D=1 OK
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
  
def pattern2(colore,d): #ok

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

def tupl(immagine,d):#ok
    img=[]
    im=[]
    for i in range(len(immagine)):
        for j in range(len(immagine[i])):
            img.append(tuple(immagine[i][j]))
            if len(img)%d==0:
                im.append(tuple(img))
                img=[]
    return im

def pattern_vrect_(colore,d): #OK Vrect

    immagine=pattern2(colore,d)
    img=[]
    for i in range(len(immagine)):
        img.append(([immagine[i]])*d)
    mi=tupl(img,d)
    return mi

def delhrect(immagine):#ok
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

def delcross(immagine):#ok
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

def pattern_cross_(colore,d):#ok
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

def pattern_hrect_(colore,d):#ok

    img=[]
    for i in range(len(colore)):
        img.append(tuple(([colore[i]])*d))
    immagine=pattern1(img,d)
    immagine=delhrect(immagine)

    return immagine


def delvrect(immagine):#ok
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


def co(quadrato):#QUESTA è GIUSTA
    if quadrato[0]!=quadrato[1] and quadrato[2]!=quadrato[3] and quadrato[2]!=quadrato[1] and quadrato[1]!=quadrato[3] and quadrato[2]!=quadrato[0] and quadrato[0]!=quadrato[3]:
        return 1
    else:
     return 0

def inverso(imma):#ok

    im=[]
    c=1
    for immagine in imma:
        for i in range(len(immagine)-1):
          j=i+1
          for q in range(len(immagine[i])-1):
                 quadrato=[immagine[i][q],immagine[i][q+1],immagine[j][q],immagine[j][q+1]]
                 if co(quadrato)!=1:
                      c=0
                      break
                 else:
                      c=1
        if c==1:
            im.append(tuple(immagine))
    return im 

def combdiff3(immagine,d):
    
    img=[]
    im=[]
    j=0
    for i in range(len(immagine)):
        im=[]
        im.append(tuple(immagine[i]))
        for j in range(len(immagine)):
                im.append(tuple(immagine[j]))
                if len(im)==d:
                    img.append((im))
                    im=[tuple(immagine[i])]
    #print(img)
    return img


def com(immagine,d): #Propieta "" se D=1 OK
    img=[]
    im=[]
    ir=[]
    c=0
    for i in range(len(immagine)):
        for j in range(len(immagine[i])-d):
            qu=[immagine[i][j],immagine[i][j+1],immagine[i][j+(d-1)],immagine[i][j+d]]
            c=co(qu)
            if c==0:
                #print(immagine[i])
                break
                
        if c==1:
            #print(immagine[i])
            for j in range(len(immagine[i])):
                img.append(immagine[i][j])
                if len(img)==d:
                    im.append(tuple(img))
                    img=[]
            ir.append(tuple(im))
            im=[]
    return ir
                    
def maestro(immagine,d): 
    img=[]
    im=[]
    ir=[]
    for i in range(len(immagine)):
        for j in range(len(immagine[i])):
            img.append(immagine[i][j])
            if len(img)==d:
                im.append(tuple(img))
                img=[]
        ir.append(tuple(im))
        im=[]
    return ir
    
def pattern3(colore,d): #Propieta "" se D>1 OK
     if d==1:
         return [[c] for c in colore]
     else:
        li=[]
        immagine=pattern3(colore,d-1)
        
        for i in colore:
            for j in immagine:
                if i!=j[0]:
                    li.append([i]+j)
                    
        return li
    
def pattern_diff_(colore,d):
    
    i=pattern3(colore,d*d)
    i=maestro(i,d)
    immagine=inverso(i)
    
    #immagine=inverso(immagine)
    return immagine
    
def ex(colors, D, img_properties):#ok
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

    print(ex([0, 128, 196, 255], 3, "pattern_diff_"))
    pass
