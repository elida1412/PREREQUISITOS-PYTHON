# Prerequisitos con Python - Parte 5

#mAnejo de errores
#su turno

a = 5
b = 0

try:
    print(a / b)

except ZeroDivisionError:
    print("Error, no se puede divir por cero")

#leyendo y escribiendo Archivos

with open('files/bookstore.txt', 'r') as f:
  data = f.readlines()[7]

print(data)

#Utilice la documentación de python para leer cada línea del archivo. E imprima su resultado
with open('files/bookstore.txt', 'r') as f:
    lineas = f.read().splitlines()

    for linea in lineas:
        print(linea)

#Finalmente imprima los datos y tambien cree un archivo llamado filter.txt. Nota, para escribir un archivo:
#path = # ubicacion del archivo
#open(path, 'w') as f:
    #f.write(data)

with open('files/dates.txt', 'r') as f:
    lineas = f.readlines()[3:8]
    resultados = []
    for x in lineas:
        resultados.append(x.split('\t')[2])

print("\n".join(resultados))

path = 'files/filter.txt'
with open(path, 'w') as fw:
    for items in resultados:
        fw.write("%s\n" % items)

#OOP (PROGRAMaCION ORIENTaDA a OBJETOS)

#OBJETOS VS CLaSES

class Ropa:
    def __init__(self, color='rojo', talla='S', estilo='camisa', precio=0):
        self.color = color
        self.talla = talla
        self.estilo = estilo
        self.precio = precio

    def cambiar_precio(self, precio):
        self.precio = precio

    def cambiar_talla(self, talla):
        self.talla = talla

ropa_mujer = Ropa('azul', 'S', 'falda', 10)
print(ropa_mujer.color)

ropa_mujer.precio

ropa_mujer.cambiar_precio(1)
ropa_mujer.precio

ropa_hombre = Ropa('verde', 'XL', 'pantalon', 20)
ropa_hombre.talla

ropa_hombre.cambiar_talla('M')
ropa_hombre.talla

cliente = Ropa()
print(cliente.talla, cliente.precio, cliente.estilo)

#AHORA USTED

#Objetivo, crear una clase, que tenga:

#El valor por defecto de la clase es 1 y su numbre 'pow2'

#Atributos

#nombre de funcion
# #dato
#Métodos:

#elevar al cuadrado (pow2)
#calcular el módulo (mod2)
#elevar al cubo (pow3)
#La clase debe estar dentro de la carpeta other_functions
#el archivo debe estar a un nivel superior

#- <app_folder>
   # - <python_main_file>
   # - <class_folder>
    #  - <python_class>
class Calcular:
    def __init__(self, valor=1):
        self.valor = valor

    def pow2(self, valor):
        self.valor = valor * valor

    def mod2(self, valor):
        self.valor = self.valor % valor

    def pow3(self, valor):
        self.valor = valor * valor * valor


potencia = Calcular(10)

potencia.mod2(4)
print(potencia.valor)
#La clase debe estar dentro de la carpeta other_functions
#el archivo debe estar a un nivel superior
#link generado pARA el Archivo
#C:\Users\Elida Dominguez\Documents\ESCRITORIO\Python inteligencia Artificial\Clase Calcular