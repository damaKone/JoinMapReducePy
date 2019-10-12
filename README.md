# JoinMapReducePy

Les étapes de notre algorithme


mapper
####Code du mapper

reducer
####Code du reducer


































hadoop jar /storeU/softs/hadoop-2.8.1/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar -file ./mapper.py -mapper ./mapper.py -input /datasets/appels/users.txt -input /datasets/appels/calls.txt -output tmp/mayi  
### pour executer la requete

wc$ hdfs dfs -cat tmp/mayi/part*  ####pour lire le resultat

