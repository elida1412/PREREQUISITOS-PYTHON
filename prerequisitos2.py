
## Bienvenidos a prerequisitos con Python - Parte2

# Escriba una expresion que calcule el promedio de...
# 30, 16, 40
a =((30 + 16 + 40)/3)
print('Resultado esperado: ')
print(a)

#¿Qué linea de python está bien formulada?

print(((1+ 24)) + -10//2)
print((22 - 12)%(3 + 2))
print ((2 + 16 + 3) / 17)
print(8/3 - 6*6)

x = ((6*2) + (2.8*2))
y = (0.5 * 12)
z = y /'z'
print (round(z))

#variAbles y operadores de AsignAcion

# un recipiente cilindrico de agua tiene (en pie cubicos)
recipiente1 = 1e3
# Se tiene otro recipiente de agua (in cubic metres)
recipiente2 = 1.8e3

# haga las siguientes operaciones
# decremente la variable del recipiente 2 al 20%
recipiente2 = recipiente2*0.8
# añada la variable de recipiente 1 a recipiente 2
recipiente2 = recipiente1 + recipiente2
# incremente el volumen del recipiente 1 al 5%
recipiente1 = (recipiente1*1.05) + recipiente1
# decremente el recipiente 1 por 15%
recipiente1 = recipiente1 - (recipiente1*0.85)
# decremente el 0.3% del recipiente 1, 
recipiente1 = recipiente1 - (recipiente1*0.99997)
# decremente el 1% del recipiente2
recipiente2 = recipiente2 - (recipiente2*0.99)
# sume ambas variables en el recipiente1
recipiente1 = recipiente1 + recipiente2
# imprima el nuevo valor de las variables
print('Resultado esperado: ', recipiente1, recipiente2)

#Enteros flotANtes
print(3+2.5)
print(int(3+2.5))
print(2 + float(2))
print(2+2)
print(type(2+2.0))

#compArAdores booleanos y operadores boleaNos

tengoHambre = True
print(tengoHambre)
tengoCOVID = False
print(tengoCOVID)
print(10 > 2)
print(2.2 > 2.2)


a = 0.3
b = 0.1 + 0.1 + 0.1
print(a == b)
print(a != b)
tengoSed = True
yaComi = False
esVerdad = False
print(tengoSed and yaComi and esVerdad)
print(tengoSed or yaComi or esVerdad)
print(tengoSed and not yaComi and not esVerdad)


# temperatura de pais vs área de estudio
tempPTY, areaPTY = 38.5, 102
tempCOL, areaCOL = 29.2, 150
# temp/m2
tempm2_pty = tempPTY/areaPTY
tempm2_col = tempCOL/areaCOL
# escriba el restante de código que indica si la temp/m2 de pty es mayor a la temp/m2 de col
print('Resultado: ', tempm2_pty > tempm2_col)


#preguntAs
#¿Porqué en Python para comparar no podemos utilizar = sino ==? 
#El iguAL es utilizado pARa ASigANAr un vaLor y el iguAL pAra compAraR.

#strings
print('a', "hola")
print('Nos veremos "tentativamente" a las 1:00p.m. hoy miércoles')
print('"Nos veremos \"tentativamente\" a las 1:00p.m. hoy miércoles"')
inicio = 'Inteligencia Artificial'
final = 'para Internet de Cosas'
print(inicio + ' ' + final)
print(inicio*10)
data = "0123456789"
print(len(data))


# Quiz

#TODO:  Arregle lo que está mal
quote = 'Ser-O-No-'"Ser"'-'"He allí"'-El Dilema'
# LA RESPUESTA ESPERADA DEBE SER:  Ser-O-No-Ser-He allí-El Dilema
print(quote)
fruta = 25
vegetales = 12
total_fruta_y_vegetal = fruta + vegetales
print('Resultado esperado ', total_fruta_y_vegetal, ' y tipo ', type(total_fruta_y_vegetal) )


#ANAlisis de logger sencillo
username = 'Ignacio'
ts = "04:50"
url = "http://minegocio.com/id/nmasaya/me"
print(username + " exited the url " + url + " at " + ts)


#calcular el largo del nombre
nombre = "Antonio"
seg_nombre = "luis"
apellido = "Dominguez"
name_length = len(nombre + seg_nombre + apellido)
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
print(type(True))
ctr = int(4.0)
print(ctr)
print(type(ctr))

#Tipos y tipos de conversion

ctr = int(4.0)
print(ctr)
print(type(ctr))


casa = 13
direccion = 'Ave Tesseract-Midgard'
provincia = 'Zanakard'
print(type(casa))
print(type(direccion))
full_dir = str(casa) + ' ' + direccion + ', ' + provincia
print(full_dir)


#encuentre los tipos de datos

print(type("12"))
print(type(12.3))
print(type(len('i am a string')))
print('inteligencia artificial'.title())

#metodos y cadenas

materia = 'INTELIGENCIA ARTIFICIAL'
print(materia.islower())
print('Abaco 3 Casas 4 Peces 3 Cadenas tres veces treinta y tres veces'.count('tres'))
print("3.2".islower())
print("12123".isnumeric())

#practica

'leonardo caballero'.islower()
True
'leonardo CABALLERO'.islower()
False

'leonardo'.isalpha()
True
'leonardo caballero'.isalpha()
False


j = 2
k = 3
print(f'{2} {4} {6} ')


#listas

print("Hi {var1} {var2}".format(var1 = "java", var2 = "soy yo"))
materias = ["Robotica", "IA", "Control", "Tecnologia Mecanica"]
print(materias[0], materias[2], materias[-1])


valores = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

primeros_tres = valores[:3]
print(primeros_tres)
primeros_tres = valores[0:3]
print(primeros_tres)


ultimos_tres = valores[5:]
print(ultimos_tres)
ultimos_tres = valores[5:8]
print(ultimos_tres)
intermedio = valores[2:6]
print(intermedio)


calificacion = 'Su calificación aprueba'
items = ['Pasta', 'Cepillo', 'Bolsa de Basura']
print(len(calificacion))
print(len(items))
print(calificacion[1:18])


mi_lista = 'Estaremos a la una de la tarde para las clases'
print('ar' in mi_lista)

nombres = ['Maria', 'Ana', 'Estela', 'juan']
print('Juan' in nombres, 'Juan' not in nombres)

m = 'abc'
m[0] = 'c'


n = ['xwb', 'abc', 'def']
print(n)
n[0] = 'wxy'
print(n)


#Ahora usted

# Use indexing para determinar el número de días en el mes 8
mes = 8
dias_del_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
num_dias =  dias_del_mes[mes-1]
print(num_dias)

# Imprima los ultimos tres elementos de la lista
dias = ['Feb 8, 1980', 'Dic 8, 1949', 
        'Mar 20, 1492', 'Abril 12, 1999',
        'Jun 12, 2010']
print(dias[2:])


p1 = "Quisiera que se terminara la materia"
p2 = ["Quisiera", "que", "se", "terminara", "la", "materia"]
print(p2[4])
print(p2[0])
print(p1[30])
print(p2[0:2])

#mAS de listA e inmutAbilidaD
nombre = 'Coimbra'
jugador = nombre
nombre = 'Pepe'
print(nombre)
print(jugador)


lista_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lista_2 = lista_1
lista_1[3] = 'j'
print(lista_1)
print(lista_2)


lista_1 = [2, 14, 20, -1, -5, 4]
print(max(lista_1))


lista_2 = ['Aries Mu', 'Cygnus Hyoga', 'Pegasus Seiya', 'Pegasus Tenma', 'Sagitarius Aiolos', 'Libra Dohko']
print(max(lista_2))

max([12, 'Shaka'])

numbers = [24, 48, 54, 65, 24, 12, 1]
print(sorted(numbers))


days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(sorted(days_of_week, reverse=True))
print("-".join(['No', 'te', 'voy', 'a', 'decir']))
print("-".join(['No' 'te' 'voy' 'a' 'decir']))


a = ['1', '2', '3']
a.append('5')
print(a)

#intentelo usted

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#cuAl sera lA saLida del siguiente codigo?
names = ["Uno", "Dos", "Tres", "Cuatro"]
print(" & ".join(sorted(names)))
names = ["Norberto", "Ignacio", "Luis", "Tito"]
names.append("Armando")
print(sorted(names))


#tuples
lat_long = (24.21254, 145.04011)
print(lat_long)
print('La latitud  es: {}'.format(lat_long[0]))
print('La longitud es: {}'.format(lat_long[1]))


tesser = 12, 14, 20, 34
D1, D2, D3, D4 = tesser
print('Las dimensiones del tesser son {}x{}x{}x{}'.format(D1,D2,D3,D4))
print(f'Las dimensiones del tesser son {D1}x{D2}x{D3}x{D4}')


#intentelo usted
tuple_a = 2, 8
tuple_b = (8, 2)
print(tuple_a == tuple_b)
print(tuple_a[1])

#sets
nombres = ['Ana', 'Gabriel', 'Juan', 'Laura', 'Roberto', 'Laura', 'Nestor', 'Ana', 'Cecibel']
print(nombres, len(nombres))
print(set(nombres), len(set(nombres)))



mi_set = set([1, 2, 4, 5, 19, 20])
print(mi_set)
mi_set.add(-1)
print(mi_set)
mi_set.pop()
print(mi_set)

#ahora usted
a = [1, 2, 2, 4, 4, 4, 8, 8, 8, 8]
b = set(a)
print (b)
print(len(a) - len(b))


a = [0, -1, -1, 2, 1, 2, 7, 9, 12, 15]
b = set(a)
b.add(111)
b.pop()
print(b)

#DiccionArios y operadores de identidades
my_dict = {'January':1, 'February':2, 'March':3}

print(my_dict['February'])
print(my_dict)

my_dict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 
           'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
print(my_dict)
print('Monday' in my_dict)

print(my_dict.get('September'))
print(my_dict.get('Monday'))
print(my_dict['Monday'])

mes = my_dict.get('Monday')
not_null = mes is not None
print(not_null)


#intentelo usted

dicci = {'Panama':5.9, 'Costa Rica':6.2, 'Colombia':8.4, 'Mexico':1.2}
print(dicci)
datos = {'Ana':{'edad':24, 'peso':110, 'sexo':'F', 'estudiante':True},
         'Javi':{'edad':12, 'peso':90, 'sexo':'M', 'estudiante':False}}
print(datos)
print(datos.get('Javi'))
print(datos.get('Juan'), 'No existe Juan')
print(datos['Javi']['peso'])
print(datos['Ana']['estudiante'])
print(datos['Javi']['estudiante'])


#crear un diccionArio

fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
print (fruits['Apple'])
print (fruits['Orange'])

Fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
key_to_lookup = 'a'
if key_to_lookup in Fruits:
  print ("Key exists")
else:
  print ("Key does not exist")


items = {
'harina': [20, 10, 15, 8, 32, 15],
'carne': [3,4,2,8,2,4],
'pan': [2, 3, 3],
'cc': [0.3, 0.5, 0.8, 0.3, 1]
}
print(items['harina'][2])
print(items['carne'][2])
print(items['pan'][2])
print(items['cc'][2])

#estructura de datos compuesta
datos = {'Ana':{'edad':24, 'peso':110, 'sexo':'F'},
         'Javi':{'edad':12, 'peso':90, 'sexo':'M'}}
print(datos)
print(datos.get('Javi'))
print(datos.get('Juan'), 'No existe Juan')
datos['Javi']['peso']

datos = {'Ana':{'edad':24, 'peso':110, 'sexo':'F', 'Estudiante': 'True'},
         'Javi':{'edad':12, 'peso':90, 'sexo':'M',  'Estudiante': 'False'}}
print(datos)
print['Ana']['estudiante']

