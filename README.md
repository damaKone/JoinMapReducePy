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

reducer
####Code du reducer


































hadoop jar /storeU/softs/hadoop-2.8.1/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar -file ./mapper.py -mapper ./mapper.py -input /datasets/appels/users.txt -input /datasets/appels/calls.txt -output tmp/mayi  
### pour executer la requete

wc$ hdfs dfs -cat tmp/mayi/part*  ####pour lire le resultat

