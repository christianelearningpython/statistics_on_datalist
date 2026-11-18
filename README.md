# statistics_on_datalist

Petit programme en ligne de commande qui analyse une liste de nombres saisie par l'utilisateur : il calcule la somme, la moyenne et compte combien de nombres dépassent la moyenne.

Projet réalisé dans le cadre de mon apprentissage de Python sur OpenClassroom (cours : Apprenez les bases Python).

Fonctionnalités
- Saisie d'une liste de nombres entiers séparés par des virgules
- Découpage de la chaîne en éléments avec split(",")
- Conversion de la liste de chaînes en liste d'entiers
- Calcul de la somme et de la moyenne 
- Comptage des nombres supérieurs à la moyenne
- Affichage de chaque étape pour bien visualiser la transformation des données

Ce que j'ai appris
- Récupérer une saisie avec input() et la découper avec split()
- Manipuler les listes : len(), append(), parcours avec for
- Convertir des types (str vers int) et comprendre la différence entre une liste de chaînes et une liste d'entiers
- Calculer une somme et une moyenne avec une boucle
- Réécrire une boucle while en boucle for plus lisible (les versions while sont conservées en commentaire dans le code)

Limites actuelles et pistes d'amélioration
- Aucune vérification des saisies : un texte non numérique (par exemple a,b,c) ou une saisie vide fait planter le programme avec une ValueError

Autrice
@ChristianeLearningPython
