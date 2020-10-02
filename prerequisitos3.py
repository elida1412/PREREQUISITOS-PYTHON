

# Prerequisitos con Python - Parte 3

#condicionALes

import ing as ing

dia = 60
if dia == 60:
    print('Ejecutar cobro')
dia = 4
if dia == 60:
    print('Ejecutar cobro')
dia = 70

#Ahora usted

#1-500     Pacora
#500-1000  Las Cumbres
#1000-3000  El Dorado
#3000-5000  Altos del Maria

if ing >= 1 and ing < 500:
    print('Pacora')
if ing > 500 and ing < 1000:
    print('Las Cumbres')
if ing > 1000 and ing < 3000:
    print('El Dorado')
if ing > 3000 and ing < 5000:
    print('San Francisco')
if ing > 5000:
    print('Altos del Maria')


#Adivine el numero
respuesta = 5 # provea un numero
numero    = 7 # el numero que ud eligio

if numero > respuesta: #condicional para entrar el siguiente codigo
    resp = 'Te fuiste muy arriba'
if numero < respuesta: #condicional para entrar al siguiente codigo
    resp = 'Te fuiste muy abajo'
if numero == respuesta: #condicional que evalua respuesta correcta
    resp = 'Ese es el numero, atinaste'
print(resp)


#pAgo de impuestos
#1. caLculo de ingresos
income = float(input("Ingreso mensual?"))
income = round(income, 2)
#2. Mostrar ingresos
print("\Ingreso del mes:", income)
#3. Calculo de deducciones
#>900 $
#Tome 9.75% como seguro social
#Tome 1.25% como seguro educativo
if income>=900:
  taxRate = 9.75 + 1.25
#4. Tasa de impuestos
print("Tasa:", taxRate, "%")
taxRate = taxRate/100
#5. Calculo deduciones
deduction = income*taxRate
#6. Imprimir tasa de deducción
print("Deducciones:", deduction, "$")
#7. Deducir las deducciones de los ingresos
total = income-deduction
#8. Mostrar monto después de las deducciones
print("Monto total:", total, "$")


#expresiones booleanAS pAra estructuraS condicionALes

edad = 24
if 18 < edad <= 40:
    print('Usted es un adulto joven')


w = 0.8
h = 1.7
if 2.5 > h/w > 1.5:
    print('Ud es normal y no sufre de gigantismo')


haveCar = True
haveGas = True
if haveCar and haveGas:
    print('Puedo pasear en auto')



haveSkills = True
knowPython = True
partTime   = False
LiveIn     = 'PANAMA'
problematic = False
teamwork   = 0.7
if haveSkills and knowPython and (LiveIn == 'PANAMA' or LiveIn == 'COLON') and (not problematic and teamwork > 0.65):
    print('El candidato encaja en el perfil')

#ahora usted
# problema robot

    tiempo = 10
    distancia = 0.5
    velocidad = 0.2

    if 10 > tiempo > 1 and velocidad*tiempo > 4 and distancia > 0.2 and tiempo and (not(velocidad/tiempo**2 > 0.1) or distancia < 1 ) and  (velocidad*tiempo > 0.5 or distancia/tiempo > 10):
        print("Se saco lA chuuuu?????????")


#ciclos for

algunas_provincias = ['PanAma', 'ColOn', 'DArien', 'VerAguas', 'ChIriqui', 'HErrera', 'LOs SAntOs']
for provincia in algunas_provincias:
    print(provincia.upper())
    algunas_provincias = ['PanAma', 'ColOn', 'DArien', 'VerAguas', 'ChIriqui', 'HErrera', 'LOs SAntOs']
en_mayusculas = []
for provincia in algunas_provincias:
    en_mayusculas.append(provincia.upper())
print(en_mayusculas)


#raNge(stArt,stop,step)

list(range(10))

list(range(4, 9))

list(range(1,2))

print(range(10))
for n in range(10):
    print(n)

    algunas_provincias = ['PanAma', 'ColOn', 'DArien', 'VerAguas', 'ChIriqui', 'HErrera', 'LOs SAntOs']
for provincia_num in range(len(algunas_provincias)):
    algunas_provincias[provincia_num] = algunas_provincias[provincia_num].lower()
print(algunas_provincias)


#Ahora practique usted
table_periodica = ['na', 'br', 'ca', 'cu', 'au', 'nd', 'ag']
for n in range(len(table_periodica)):
	table_periodica[n] = table_periodica[n].capitalize()
print(table_periodica)



trabalenguas = ['Por', 'desenredar', 'el', 'enredo', 'que', 'ayer', 'enredé.', 'Hoy', 'enredo',
                'el', 'desenredo', 'que', 'desenredé', 'ayer.']
respu = ''
for n in range(len(trabalenguas)):
	respu = respu + trabalenguas[n] + ' '
print(respu)


num_fact = 6
factor= 1
for n in range(factor, 7):
	factor = factor * n
print(factor)


num = 0
for n in range(31):
	num = num + n
print(num)


nombres = [
    'Himura Kenshin',
    'Kamiya Kaoru',
    'Myōjin Yahiko',
    'Sagara Sanosuke',
    'Takani Megumi',
    'Shinomori Aoshi',
    'Saitō Hajime',
    'Makimachi Misao'
]
nombresend= []
for n in range(len(nombres)):
    nombres[n] = nombres[n].lower()
    nombres[n] = nombres[n].replace(" ", "-")
    print(nombres[n])


#interaccion con diccionArios
numeros = {0:'cero', 1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco',
           6:'seis', 7:'siete', 8:'ocho', 9:'nueve', 10:'diez'}
for num in numeros:
    print(num)

for key, value in numeros.items():
    print(key, value)
for key in numeros.keys():
    print(key)
for val in numeros.values():
    print(value)


edades = {'Juan':10, 'Javier': 4, 'Jonas':8, 'Nuria': 20, 'Edith': 18, 'Ana':14}
edadt = 0
for n in edades.values():
    edadt = edadt + n
print(edadt)


#ciclos while
numeros = [1, 4, 9, 10, 120, 22, 43]
reversal = []
while len(numeros):
    reversal.append(numeros.pop())
print(reversal)

#Ahora usted
valor = 3
n = 3
while n < 9:
    valor = valor*(n)
    n += 1
print(valor)


#lista while

lista = list(range(16))
num = []
n = 0
n1 = 0
while n < len(lista):
    if lista[n] % 2 == 1:
        num.append(lista[n])
    n += 1
while n1 < len(num):
    print(num[n1])
    n1 += 1


num = 456
n = 0
final = 0
while final < num:
    n += 1
    final = 0
    final = n**2
print('El número más cercano es {}'.format(str(n-1)))


#break y continue
# item, peso (kg)
items = [('frutas', 320), ('vegetales', 655), ('jugetes', 880), ('cereales', 375), 
         ('detergente', 450), ('hogar', 200), ('farmacia', 499), ('papel', 1000), ('otros', 932)]
contenedor = []
total_weight = 0
for item in items:
    name, weight = item
    if weight > 500:
        continue # no cargar al contenedor
    else:
        total_weight += weight              
        contenedor.append(name)
print(f'Cargamos al contenedor {contenedor} y el peso total de la mercancia es {total_weight} kg')


contenedor = []
total_weight = 0
for item in items:
    name, weight = item
    total_weight += weight        
    if total_weight >= 3750:
        total_weight -= weight
        break # no cargar más de la capacidad máxima
    else:              
        contenedor.append(name)
print(f'Cargamos al contenedor {contenedor} y el peso total de la mercancia es {total_weight} kg')


#Debugging
contenedor = []
total_weight = 0
for item in items:
    name, weight = item
    total_weight += weight        

    if total_weight >= 3750:
        total_weight -= weight
        print(f'\n**carga total al final del ciclo {total_weight}**')        
        break # no cargar más de la capacidad máxima
    else:  
        print(f'cargando {name}, peso actual {total_weight}')
        contenedor.append(name)
print(f'\nCargamos al contenedor {contenedor} y el peso total de la mercancia es {total_weight} kg')


#mAS de continue en ciclos
ufc_champions = ['Stipe Miocic', 'Israel Adesanya', 'Kamaru Usman', 'Khabib Nurmagomedov',
                 'Justin Gaethje', 'Alexander Volkanovski', 'Petr Yan', 'Deiveson Figueiredo']
ufc_champions_short = ['Israel Adesanya', 'Khabib Nurmagomedov', 'Justin Gaethje', 'Deiveson Figueiredo']

count = 0
for champ in ufc_champions:
    if champ not in ufc_champions_short:
        print('No fue encontrado este campeon')
        continue
    else:
        count = count + 1
        print(f'Contado el campeon {champ}')
print('Total de campeones encontrados ->', count)

#intentelo ud AHora
palabras = ['Cretino', 'Vida mía', 'Baboso', 'Bocachancla','Cielo', 'Cielito', 'Mi vida', 'Mi luz', 
            'Luz de mis ojos', 'Bebecita', 'Cariño', 'Papacito', 'Zoquete', 'Cariño mío', 'Patan', 'Cari', 
            'Corazón', 'Mi rey', 'Lerdo','Osito', 'Bombón', 'Charlatan', 'Dulzura', 'Galletita', 
            'Fanfarrón']
ofensas = ['Baboso', 'Bocachancla', 'Charlatan', 'Cretino', 'Fanfarrón', 'Lerdo', 'Patan', 'Zoquete']

count = 0
for piropos in palabras:
    if piropos not in ofensas:
        piropos2 = piropos
        print(piropos2)
        continue

#zip y enumerate
item = ['frutas', 'vegetales', 'juguetes', 'cereales', 'detergente', 'hogar', 'farmacia', 'papel', 'otros']
peso = [320, 655, 880, 375, 450, 200, 499, 1000, 932]
print(list(zip(item, peso)))

#same as below comments
#elementos = zip(item, peso)
#for item, peso in elementos: # same as below

for n, w in zip(item, peso):
 print(n, w)


elementos = zip(item, peso)
item, peso = zip(*elementos)
print(item)
print(peso)
for i, elemento in zip(range(len(items)), item):
    print(i, elemento)
for i, elemento in enumerate(item):
    print(i, elemento)

#Ahora intentelo usted
x0 = [0, 1, -2, 14, -5, 4, 5]
x1 = [1, 3, 5, 7, 9, 11, 13]
x2 = [2, 4, 6, 8, 10, 12, 14]
letras = ['A', 'B', 'C', 'D', 'F', 'E', 'F']

#Haga un izp de la lista inferior

ya = zip(x0, x1, x2)
yb = zip(letras, ya)

#yc = zip(ya, yb)
for ya, var1, in zip(range(len(letras)), yb):
    print(var1)

tup = ((1,-1), (2,-2), (3,-3), (4,-4), (5,-5))
pos , neg = zip(*tup)
print(pos)
print(neg)

#Utilice zip para convertir la siguiente matriz 5x4 en una matriz 4x5
matriz5x4 = (( 1, 2, 3, 4),
            ( 5, 6, 7, 8),
            ( 9,10,11,12),
            (13,14,15,16),
            (17,18,19,20))

matriz4x5 = [] 
splitmat = zip(*matriz5x4)
matriz4x5 = [list(var2) for var2 in splitmat]

twilight = ['Bella Swan', 'Edward Cullen', 'Jacob Black', 'Charlie Swan',
            'Carlisle Cullen', 'Esme Cullen', 'Alice Cullen']

#listA de comprension
algunas_provincias = ['PanAma', 'ColOn', 'DArien', 'VerAguas', 'ChIriqui', 'HErrera', 'LOs SAntOs']
en_mayusculas = []
for provincia in algunas_provincias:
    en_mayusculas.append(provincia.upper())

print(en_mayusculas)
en_mayusculas = [provincia.upper() for provincia in algunas_provincias]
print(en_mayusculas)

# con for loop
x = []
for i in range(10):
    x.append(i ** 3)
print(x)

# con listas de comprensión
x = [i ** 3 for i in range(10)]
print(x)

# solo listar de los numeros que son pares su valor al cubo
x = [i**3 for i in range(10) if i%2 == 0]
print(x)
#Ahora usted
conquistadores = ['Vasco Núnez de Balboa', 'Luis de Moscoso Alvarado', 'Juan de Cárdenas',
                  'Pedro de Heredia', 'Gutierre de Miranda', 'Juan de Salcedo']

major_league_players = {'Mel Allen':1978, 'Red Barber':1978, 'Jerry Coleman':2005,
          'Joe Garagiola, Sr.':1991, 'Curt Gowdy':1984, 'Ken Harrelson':2020,
          'Al Helfer':2019, 'Russ Hodges':1980}
print(player)