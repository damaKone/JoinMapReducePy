# JoinMapReducePy

Les étapes de notre algorithme
1_Mettre les informations contenues dans les fichiers Users.txt et Calls.txt sous forme de clé valeur; 
pour Users , on prendra pour clé le numero du telephone se l'utilisateur;
pour Calls , on prendra pour clé le numero du telephone appellant.
Ainsi donc on aura sur chaque ligne le numero du telephone plus soit les informations de l'utilisateur, soit les informations de l'appel. Cela va pouvoir etre implémenté au niveau du mapper.
2_Quand on aura mis les différents élements sous forme de clé valeur, on pourra alors comparer les différentes clé;
ainsi donc , on va comparer chaque premier element de chaque ligne avec les autres( ce qui correspond bien sûr au numero du télephone).
Quand on trouve que les 2 numeros du telephone sont les meme, on verifie alors  qu'ils ne proviennent pas de la meme source
c'est à dire on s'assure que l'un vient de Calls et l'autre de Users pour pouvoir faire la jointure.
Si ces tests sont faits et que tout passe ,alors on pourra afficher ce numero de télephone avec les informations de l'utilisateur et de l'appel.
Cela va pouvoir etre implémenté au niveau du reducer



Mapper
####Code du mapper

#je sais pas si tu as changer les variables du mappers.c'etait ce mapper.py j'avais comme ancienne version 


#!/usr/bin/env python

import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split(",")

    if (len(words)==5):
              infoUsers=words[0]+"^"+words[1]+"^"+words[3]+"^"+words[4]
              print '%s^%s'%(words[2], infoUsers)
    else:
              infoCalls=words[1]+"^"+words[2]
              print '%s^%s'% (words[0],infoCalls)
reducer
####Code du reducer



#!/usr/bin/env python
import sys
import string
#pour stocker les les elements de la ligne prcedente
last_autres = "n"
#pour stocker l'ancien numero de telephone
last_tel = 1
#pour stocker la taille des autres elements de la ligne precedente
tail = 1
for line in sys.stdin:
    #pour enlever les blancs
    line = line.strip()
    #pour separer a partir de ^
    splits = line.split("^")
    #on recupere le numero de telephone
    cur_tel = splits[0]
    # on recupere les autres elements sachants qu'ils sont separé par un blanc 
    autres = splits[1]
    #pour separer les autres elements quin a recuper dans le but de calculer la taille
    splitss = autres.split(" ")
    # on rcupere la taille des autres elements qui restent quand on recupere le numero du telephone;
    ## car ca peut etre soit les informations de l'utilisateurs soit de l'appel
    s = len(splitss)     
    if cur_tel == last_tel :
       if s == 4 and tail == 2 :
        print'%s\t%s\t%s' %(cur_tel,autres,last_autres)
        x = cur_tel
        cur_tel = last_tel
        last_tel = x
        y = s
        s = tail
        tail = y
        last_autres = autres
      elif s == 2 and tail == 4 :
       print'%s\t%s\t%s' %(cur_tel,last_autres,autres)
       x = cur_tel
       cur_tel = last_tel
       last_tel = x
       y = s
       s = tail
       tail = y
       last_autres = autres
    else:
        x = cur_tel
        cur_tel = last_tel
        last_tel = x
        y = s
        s = tail
        tail = y
        last_autres = autres
        continue
































hadoop jar /storeU/softs/hadoop-2.8.1/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar -file ./mapper.py -mapper ./mapper.py -input /datasets/appels/users.txt -input /datasets/appels/calls.txt -output tmp/mayi  
### pour executer la requete

wc$ hdfs dfs -cat tmp/mayi/part*  ####pour lire le resultat

