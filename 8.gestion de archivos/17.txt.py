# archivo que contiene textos#


with open("archivo_creado.txt","w") as archivo:
    archivo.write("Este es un archivo de tipo txt")
    archivo.write("Contine taxto de ejemplo")
    print("Archivo creado corrrectamente")
    
# consulta de archivo# 

with open("archivo_creado.txt","r") as archivo:
    contenido=archivo.read
    print("contenido del archivo:")
    print(contenido)    
    
#Actualizacion del archivo# 

with open("archivo_creado.txt","a") as archivo:
    archivo.write("\nEsta es una nueva linea aragada")
    print("archivo actualizado correctamente.")
    
# Clasificacion de datos#

with open("nombres.txt","w") as archivo:
    archivo.write("Carlos\nAna\nLuis\nSofia\nAlicia\nJorge")  
with open("nombres.txt","r") as archivo:
    nombres=archivo.readlines 
    nombres.sort()
with open("nombres.txt","w") as archivo:        
    archivo.writelines(nombres)
print("nombres ordenados correctamente.")    