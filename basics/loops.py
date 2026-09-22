## Python Basics - Loops
## Author: Mamadou Doumbia

#Pour afficher les nombres de 1 - 10 : 
for nombre in range(1, 11):
  print(nombre)

##Pour les nombres pairs de 1 à 10 :
#Methode 1:
for nombre in range(1, 11):
  if nombre % 2 == 0 :
    print(nombre)

#Method 2:
print("Method 2")
for nombre in range(2, 11, 2):
    print(nombre)

#Calcul de la somme des nombres de 1 à 10 :
print("Calcul de la somme des nombres de 1 à 10 :")
somme=0
for nombre in range(1, 11):
   somme = somme + nombre
print("La somme des nombres de 1 à 10 est :", somme)

#Demander 5 nombres à l’utilisateur et afficher leur somme
print("Demander 5 nombres à l’utilisateur et afficher leur somme")
somme=0
for i in range(5):
    nombre = int(input("Entrez un nombre : "))
    somme = somme + nombre
print("La somme des 5 nombres est :", somme)

##Loop while
#Afficher les nombres de 1 à 10 avec while
i = 1
while i <= 10:
    print(i)
    i += 1
#Demander un nombre tant qu’il est positif
nombre= int(input("Entrez un numero svp: "))
while nombre > 0:
    print("Nombre positif:", nombre)
    nombre= int(input("Entrez un numero svp: "))
