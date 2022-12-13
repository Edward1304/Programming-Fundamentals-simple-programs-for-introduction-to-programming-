#   TALLER 05

#   EJE01T05

def inlst(l, vi):                         # función para INICIALIZAR una lista   lst de l elementos
    lst = []                              # en un valor vi
    for i in range(l):
        lst.append(vi)
    return lst

vlr = int(input("Digitar un valor, para terminar digitar 999999 : "))
lv = []
while vlr != 999999:
    lv.append(vlr)
    vlr = int(input("Digitar un valor, para terminar digitar 999999 : "))
lstdu = inlst(100,0)
for rl in range(len(lv)):
    du = abs(lv[rl]) % 100      # sacando abs ya nos sirve el problema para cualquier entero <> 0
    lstdu[du] += lv[rl]         # ya que sin este, al digitar enteros negativos, no se podría utilizar modulo (%)
for i in range(len(lstdu)):
    if lstdu[i] > 0:
        print(f"Suma de valores leídos cuyos ultimos 2 dígitos terminan en {i} : {lstdu[i]}")

#   EJE02T05

from F_T02 import EJE05T02

vlr = int(input("Digitar un valor, para terminar digitar 999999 : "))
lv = []
while vlr != 999999:
    lv.append(vlr)
    vlr = int(input("Digitar un valor, para terminar digitar 999999 : "))
lstdu = inlst(10,0)
for i in range(len(lv)):
    du = abs(lv[i]) % 100
    randu = EJE05T02(du) - 1
    lstdu[randu] += lv[i]
ran1 = 0
ran2 = 9
ran3 = 0
for X in range(10):
    if X > 0:
        ran1 += 10
        ran2 += 10
        ran3 += 1
    rta = f"Suma de valores leídos que terminan en rango {ran1} a {ran2} : {lstdu[ran3]}"
    print(rta)


#   EJE03T05

# Elaborar un PROGRAMA que lea una serie de registros c/u con: código de empleado,
# fecha nacimiento y sueldo mensual.
# Determinar e imprimir:  la cantidad de empleados que nacieron: el primer día del año,
# el segundo día del año, el tercer día del año, ………, hasta el día 366 del año.

def convierte_fecha(F):                 # Recibe una fecha de tipo string (str)
    F = F.split("/")                    # la convierte en tupla y devuelve d,m,a
    F = int(F[0]),int(F[1]),int(F[2])   # d/m/a ---> d,m,a
    return F                            # Ejm: recibe la cadena '18/2/2001' y devuelve 18,2,2001

def nd_van_año(D,M,A):                  # Devuelve el número de dias que han tarnscurrido del año
    DT = D                              #   hasta la fecha.
    for ma in range(1,M):
        DT += EJE06T03(ma,A)
    return DT

from T03 import EJE06T03

ED = "S"
l_diasaño = inlst(366,0)
while ED == "S" or ED == "s":
    codigo = int(input("Código del empleado : "))
    f_nacimiento = str(input("Fecha de nacimiento(d/m/a) : "))
    dia,mes,año = convierte_fecha(f_nacimiento)
    sueldo = int(input("Sue ldo : "))
    diadelaño = nd_van_año(dia,mes,año)
    l_diasaño[diadelaño - 1] += 1
    ED = input("Digite 'S' para continuar : ")
for X in range(len(l_diasaño)):
    if l_diasaño[X] > 0:
        print(f"Empleados que nacieron el dia {X+1} del año : {l_diasaño[X]}")

#   EJE04T05

# FUNCIÓN que reciba varios valores, obtener y entregar el menor de los valores recibidos.
# Ejemplo recibe   25   14   38    21   47    64    2    25    36     81    45.  ENTREGA  2

def EJE04T05(L):
    mnr = min(L)
    return mnr

"""L = 25,14,38,21,47,64,2,25,36,81,45
print(EJE04T05(L))"""

#   EJE05T05

# FUNCIÓN que reciba varios valores, obtener y entregar 1 si el menor es el primero, 2 si el menor de todos es el segundo,
# 3 si el menor es el tercero, 4 5 6 7………………………
# Ejemplo recibe   25   14   38    21   47    64    2    25    36     81    45.  ENTREGA  7.

def EJE05T05(L):        # Devuelve la posición del menor
    L = list(L)
    mnr = min(L)
    P = L.index(mnr) + 1
    return P

"""L = 25,14,38,21,47,64,2,25,36,81,45
print(EJE05T05(L))"""

#   EJE06T05

# FUNCIÓN que reciba un valor entero, tomar su valor absoluto. Entregar los números primos que sean
#  menores o iguales al valor absoluto del valor recibido.
# Ejemplo recibe  25      ENTREGA 2   3   5   7   11   13    17   19   23.

from T03 import es_primo

def EJE06T05(E):
    E = abs(E)
    L = []
    for X in range(E+1):
        if es_primo(X):
            L.append(X)
    return L

"""print(EJE06T05(25))"""

#   EJE07T05

# FUNCIÓN que reciba varios valores de P, entregar los valores de P en forma inversa a como los recibió.
# Ejemplo recibe   25   14   38   21   47    64    45.  DEVUELVE ó ENTREGA  45   64   47 21   38   14   25.

def EJE07T05(P):
    P = list(P)
    P.reverse()
    return P

"""L = 25,14,38,21,47,64,45
print(EJE07T05(L))"""

#   EJE08T05

# FUNCIÓN que reciba varios valores X  y un valor Z, obtener y entregar a cuál de los valores de X es igual Z.
# EJEMPLO:   recibe en X: 45   12   7     21    64     47   84   y   en   Z   64,     entrega  5.

def EJE08T05(X,Z):
    X = list(X)
    P = X.index(Z) + 1
    return P

"""X = 45,12,7,21,64,47,84
Z = 64
print(EJE08T05(X,Z))"""

#   EJE09T05

# FUNCIÓN que reciba varios valores de A, obtener y devolver los valores de
# A que sean menores al promedio de todos los A.

def EJE09T05(A):
    A = list(A)
    L = []
    sumA = sum(A)
    cantA = len(A)
    promA = sumA / cantA
    for X in range(len(A)):
        if A[X] < promA:
            L.append(A[X])
    return L

"""L = [2,10,4,8,6]
print(EJE09T05(L))"""

#   EJE10T05

# FUNCIÓN que reciba un valor entero, tomar su valor absoluto.  Entregar los dígitos que tiene el valor recibido.
# EJEMPLO:   recibe   45273241    entrega   4    5    2    7    3    2   4    1.

def EJE10T05(E):
    E = abs(E)
    L = []
    D = 0
    while E > 0:
        D = E % 10
        E //= 10
        L.append(D)
    L.reverse()
    return L

"""A,B,C,D,E = EJE10T05(28214)
print(A,B,D,E)"""

#   EJE11T05

# FUNCIÓN que reciba un valor Q, entregar el valor de Q modificado así: el primer digito de último,
# el último de primero, el segundo de penúltimo, el penúltimo de segundo y así sucesivamente hasta
# obtener el valor recibido en sentido contrario.
# Ejemplo recibe 25143876.  DEVUELVE ó ENTREGA  67834152.

def EJE11T05(Q):
    L = EJE10T05(Q)
    L.reverse()
    Q = ""
    for i in range(len(L)):
        Q += str(L[i])
    Q = int(Q)
    return

"""X = EJE11T05(2187)
print(X)
print(X + 1000)"""
