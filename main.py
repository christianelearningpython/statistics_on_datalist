# Ecrivez votre code ici !

print("Saisissez une liste de nombres séparés par des virgules : ")
nombres=input()
print(f"La chaine saisie est : {nombres}")

liste=nombres.split(",")
print(f"Je split chaque nombre avec le séparateur , toujours en str : {liste}")

nb_elements=len(liste)
print(f"La liste contient {nb_elements} elements.")

""" conversion de la liste en une liste de int
i=0
liste_entiers=[]
while i < nb_elements :
    a=int(liste[i])
    liste_entiers.append(a)
    i+=1
"""

liste_entiers=[]
for element in liste :
   entiers = int(element)
   liste_entiers.append(entiers)

print(f"Je convertis les éléments dans une nouvelle liste d'int : {liste_entiers}")

""" sommes des entiers dans la liste_entiers
j=0
somme=0
while j < nb_elements :
    somme+=liste_entiers[j]
    j+=1
print(f"la somme de cette liste est {somme}.")
"""

#on manipule une liste d'entiers /!\ pas une liste de str
somme=0
for element in liste_entiers :
    somme+=element
print(f"La somme de cette liste est {somme}.")

moyenne=round(somme/nb_elements,2)
print(f"La moyenne de cette liste est {moyenne}.")

""" le nombre d'éléments dans liste_entiers > moyenne
k=0
sup_moyenne=0
while k < nb_elements :
    if liste_entiers[k] > moyenne :
        sup_moyenne+=1
    k+=1
"""

sup_moyenne=0
for element in liste_entiers :
    if element > moyenne :
        sup_moyenne +=1

print(f"Il y a {sup_moyenne} nombres supérieurs à la moyenne.")
