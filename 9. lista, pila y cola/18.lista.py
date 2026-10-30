# es un conjunto de valores identificados por un indice 

#ejercico de lista de numeros aleatorios#

import random
def listaAleatorio(n):
    s=[0]*n
    for i in range(n):
        s=[1]=random.random()
        return s
    numeros=listaAleatorio(8)
print(listaAleatorio(8))    


# tuplas: son listas de valores separadas por comas y  es inmutable#
tupla="a,b,c,d,e "
print(tupla)
tupla[0]
tupla[2:4]

# ejercico con nueros aleatorios#

import random
for i in range (10):
    x=random.random()
    print(x)
    
    
# diccionarios: son similares a a los comuestos por una clave y valor  y son nmutables#
# Estos  son diccionarios en python#
My_dict=dict()
my_other_dict={}
print(type(My_dict))
print(type(my_other_dict))
# Agregar elementos al diccionario #
My_dict["Nombre"]="Alejandro"
My_dict["Edad"]=26
My_dict["Ciudad"]="Quito"
print(My_dict)
# Update values and add idiomas list
My_dict["Edad"]=27
My_dict["idiomas"]=["español","ingles","ruso"]
My_dict.update({"Estatura":1.68})
print(My_dict)
# Acceder a los valores del diccionario #
My_dict={
    "nombre":"Alejandro",
    "edad":27,
    "ciudad":"Quito",
    "idiomas":["español","ingles","ruso"],
    "estatura":1.68,
}
print(my_other_dict)
print(My_dict)
print(len(My_dict))
print(My_dict["nombre"])
My_dict["pais"]="Ecuador"
print(My_dict)
# Eliminar elementos del diccionario #
del My_dict["ciudad"]
print(My_dict)
my_new_dict=My_dict.fromkeys ("Nombre","Alejandro")
print(my_new_dict)