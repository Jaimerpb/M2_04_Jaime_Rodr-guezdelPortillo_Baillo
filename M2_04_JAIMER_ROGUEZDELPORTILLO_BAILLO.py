#1) Trabajemos con listas y tuplas
#Las tuplas no se pueden modificar
#Crea una lista y una tupla que contenga strings (al menos 3 elementos)
from audioop import reverse


FRUITS=["manzana","platano","pera"]
fruits=("kiwi","melocotón","fresas")
#Muestra la lista y la tupla
print(FRUITS)
print(fruits)
#Muestra el 2º elemento de la lista y el penúltimo de la tupla
print(FRUITS[1])
print(fruits[-2])
#Modifica (si se puede) algún elemento de la lista y de la tupla. Y mostrar el resultado:
FRUITS[2]= "sandía"
print(FRUITS)
#Muestra el tamaño de la lista y de la tupla.
print(len(FRUITS))
print(len(fruits))
#Realiza una búsqueda de un elemento dentro de la lista y de la tupla. Mostrar si devuelve True o False.

      
print(FRUITS[0])
FRUITS[0] in FRUITS

     
print(fruits[1])
fruits[1] in fruits
#Añade (si se puede) algún elemento a la lista y a la tupla. Mostrar de nuevo la lista y la tupla para verificar si se ha realizado correctamente la acción.
FRUITS.append("mango")
print(FRUITS)

#Borra o elimina (si se puede) el contenido de la lista y de la tupla. Mosstrar de nuevo la lista y la tupla para verificar si se ha realizado correctamente la acción.
FRUITS.clear()
print(FRUITS)

#2) Trabajemos con sets y diccionario.
#Crea una set y un diccionario que contengan strings (al menos 3 elementos en el caso del set y 3 conjuntos de clave:valor en el caso del diccionario).

musica_genres=set(["country","metal","hip-hop"])
subgenres={"Blues":"Classic Blues","Metal":"Heavy Metal","Jazz":"Afro-Cuban jazz"}
#Muestra el set y el diccionario
print(musica_genres)
print(subgenres)
#Muestra (si se puede) el 2º elemento del set y el valor del primer clave-valor del diccionario.
print(subgenres["Blues"])
#Modifica (si se puede) algún elemento del set o del diccionario. Y mostrar el resultado.
subgenres["Jazz"]="Acid Jazz"
print(subgenres)

#Muestra el tamaño del set y del diccionario.
print(len(subgenres))
print(len(musica_genres))
 #Borra o elimina (si se puede) el contenido del set y del diccionario. Mosstrar de nuevo el set y el diccionario para verificar si se ha realizado correctamente la acción

subgenres.clear()
print(subgenres)
musica_genres.clear()
print(musica_genres)

#3) Realizar un programa que pida al usuario 3 números que pueden ser flotantes (no es necesario realizar bucles aún, podemos repetir el código), estos números se deberán introducir en una lista. Cuando se haya finalizado la introducción de los datos, se mostrará el sumatorio de toda la lista. Guardar el sumatorio en una variable que se llame "sumatorio"

num3ros=[float(input()),float(input()),float(input())]
print(num3ros)
sumatorio=sum(num3ros)
print("Result : " ,sumatorio)
#4)Sobre el ejercicio anterior, queremos mostrar la media aritmética de los elementos de esa lista. Indicar la instrucción necesaria para obtenerla.
arithmetic_average= sum(num3ros)/len(num3ros)
print("Average : ",arithmetic_average)
