


#!/usr/bin/env python
import sys
import string
last_autres = "n"
last_tel = 1
tail = 1
for line in sys.stdin:
    line = line.strip()
    splits = line.split("^")
    cur_tel = splits[0]
    autres = splits[1]
    splitss = autres.split(" ")
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
  


############cat customers.dat countries.dat|./smplMapper.py|sort|./smplReducer.py
    ##### algorithme:::: on a envoyer les donnees sen arrageant de sorte que le numero de télephone sorte en premier okkkk
    ###### on sait que la taille des deux enregistrements sont differentes mais on a remplacé par des -1, ce quon peut faire
    #### on regarde si les numeros de telephone sont les memes , super cela suppose deja que c'est la meme personne de toute facon le 
    ### mapper ne vas pas envoyer la meme valeur deux fois a moins que ce ne fut dupliquer 
    ### et donc on pourrait quand meme verifier que les autres attributs (dept,ville etc) sont à -1 dans au moins une liste
    #### et donc on pourras faire notre jointure dans ce cas .............;;;
    ### si les numeros de telephones ne sont pas les memes, bah deja il faut au moins s'assurer de tester avec tous les autres 
    ###du coup on continu
    
