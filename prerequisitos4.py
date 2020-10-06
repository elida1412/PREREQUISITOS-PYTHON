
#Prerequisitos con Python - Parte 4

def distancia(vo, dt, a):
    d = vo*dt + 0.5*a*dt**2
    return d

vo = 2
t = 0.5
a = 1.2
d = distancia(vo, t, a)
print(d)

d = distancia(2, 0.5, 1.2)
print(d)
retorno = print(' ')

print(retorno)

#AHora usted

#area_elipse = calcular_area_elipse (a, b)

import math
def calcular_area_elipse (a, b):
    area_eclipse = a * b * (math.pi)
    return area_eclipse
a = 10
b = 5
area_elipse = calcular_area_elipse (a, b)
print(area_elipse)


t = "520:59:30"
segundos = [3600,60,1]
sum([a * b for a,b in zip(segundos, map(int,t.split(':')))])


#ALcaNce de variABles
def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

b = 2
h = 3
area1 = area_rectangulo(b, h)
area2 = area_triangulo(b, h)
print(area1, area2)


val = 15
def print_val():
    print(val)
print_val()
val

#ahORA USTED

pi = 3.141592654

def area_circulo(r):
    print(pi*r**2)

area_circulo(4)
pi_medio = pi/2

print("El error era que la variable estaba definida dentro de la funcion y no estaba disponible de forma global.")

#DOCUMENTaCION DE CÓDIGO

def area_trapecio(a, b, h):
    area = (a + b)*h/2 # a y b, base y lado superior respectivamente; h es la altura
    return area
# calculando el area de diferentes trapezoides
print(area_trapecio(4, 2, 1))
print(area_trapecio(3, 8, 8))
print(area_trapecio(1, 1, 0.2))
print(area_trapecio(7, 3, 0.5))

# escribiendo lo mismo pero sin funciones
a, b, h = 4, 2, 1
area = (a + b)*h/2
print(area)

a, b, h = 3, 8, 8
area = (a + b)*h/2
print(area)

a, b, h = 1, 1, 0.2
area = (a + b)*h/2
print(area)

a, b, h = 7, 3, 0.5
area = (a + b)*h/2
print(area)


def area_trapecio(a, b, h):
    """
    CALCULA EL AREA DEL TRAPEZOIDE DATA BASE, ALTURA Y PARTE SUPERIOR
                   a
                 ______       _
               /       \      |
              /         \     h
             /___________\   _|_
                   b

    ENTRADAS:
    a:  parte superior del trapezoide
    b:  parte inferior (base) del trapezoide
    h:  altura del trapezoide

    RETORNA:
    area_trapecio: el area del trapecio dada por la ecuación.
    """
    area = (a + b) * h / 2  # a y b, base y lado superior respectivamente; h es la altura
    return area

#ahora usted

def area_paralelogramo(b, h):
    """
    CALCULAR EL AEREA DE UN PARALELOGRAMO
                ________
               /       /  |
              /       /   h
             /_______/   _|_
                 b

    ENTRADAS:
    b:  parte inferior (base) del paralelogramo
    h:  altura del paralelogramo

    RETORNA:
    area_paralelogramo: el area del paralelogramo dada por la ecuación.
    """
    area = (b * h)  # la b representa la base del paralelogramo; la h es la altura del mismo
    return area

#expresione lAmbda

def suma(a, b):
    return a+b

print(suma(3,2))

suma = lambda x,y: x + y
print(suma(3,2))

n2 = lambda n: n**2
print(n2(5))

#intelo usted

n_list = [list(range(10)), list(range(2, 20)), list(range(5, 40, 2))]

def avg(n_list):
    av = sum(n_list)/len(n_list)
    return av

promedio = list(map(avg, n_list))
promedio, " ", n_list

n_list = [list(range(10)), list(range(2, 20)), list(range(5, 40, 2))]

avg = lambda x: sum(x)/len(x)

promedio = list(map(avg, n_list))
promedio

valores = [1, 20, -1, 2, 5, 4, -2, -5, 10]

def impares(v):
    if v%2 != 0:
        return True

vals = list(filter(impares, valores))
print(vals)

valores = [1, 20, -1, 2, 5, 4, -2, -5, 10]

impares = lambda x: x%2 !=0

vals = list(filter(impares, valores))
print(vals)

#iteradores y generadores

def generador(x):
    i = 0
    while i < x:
        yield i
        i += 1


print(generador(6))

for n in generador(6):
    print(n)

#practica

frases = ["Practical GUI", "Advanced Programming", "Building Intelligent", "The AI Workshop", "Data Analysis"]


def enumerador(f, i):
    i = i
    for elementos in f:
        yield (i,elementos)
        i += i

for i, frase in enumerador(frases, 1):
    print("Book {}: {}".format(i, frase))

#generadores

gen = (n + 4 for n in range(10))
gen

for g in gen:
    print(g)

gen = (n + 4 for n in range(10))
gen

for g in gen:
    print(g)

