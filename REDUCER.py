


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
  ### Quand on enlève la premiere ligne qui est le numero du telephone, alors les elements qui restents ont soit la taille = 4 (si c'est les informations de l'utilisateur)
####  soit la taille = 2 (si c'est les informations sur l'appel) 
## et donc si on trouve deux numeros qui sont pareils et que la taille des autres informations sont != , on peut faire la jointure en envoyant un print
##on doit juste faire attention a l'ordre , c'est pour cela il a fallu faire deux tests de if


############cat customers.dat countries.dat|./smplMapper.py|sort|./smplReducer.py
    ##### algorithme:::: on a envoyer les donnees sen arrageant de sorte que le numero de télephone sorte en premier okk
    #### et donc on pourras faire notre jointure dans ce cas .............;;;
    ### si les numeros de telephones ne sont pas les memes, bah deja il faut au moins s'assurer de tester avec tous les autres 
    ###du coup on continu
    
