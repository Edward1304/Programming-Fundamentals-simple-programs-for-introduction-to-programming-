
#24- FUNCION que reciba un valor  N (>0)   y  devuelva  la suma de los enteros desde 1 hasta N.
_______________________________________________________________________________________________
def EJE24T04(N):     #  versión 1
    SE = 0
    for en in range(1,N+1):
                       SE +=  en
    return SE

.                 ______________________________________________________________
def EJE24T04(N):     #  versión 2
    SE = N
    for en in range(1,N):
                       SE +=  en
    return SE
                 ______________________________________________________________
def EJE24T04(N):     #  versión 3
     SE = N * (N + 1) / 2
     return SE
___________________________________________________________________________________________
#25- FUNCION que reciba un valor  N (>0)  y  devuelva  la suma de los  pares desde 1 hasta N.
def EJE25T04(N):     #  versión 1
    Sp = 0
    for par in range(2,N+1):
                       Sp + =  par
    return Sp
??????        se  puede al igual que  en el ejercicio 24    hacer como la versión  2   y  3  ????

________________________________________________________________________________________________
#26- FUNCION que reciba un valor  N (>0)  y  devuelva  la suma de los impares  desde 1 hasta N.
def EJE26T04(N):     #  versión 1
    SI = 0
    for imp in range(2,N+1):
                       SI + =  imp
    return Si
??????        se  puede al igual que  en el ejercicio 24    hacer como la versión  2   y  3  ????

???    como seria utilizando  adecuadamente las dos FUNCIONES  ANTERIORES. (  24    y  25)

???    como sumar  los múltiplos  de    x   hasta N    utilizando version 3 ? como es la formula??
______________________________________________________________________________________________
# EJERCICIOS 17   A  23   usando funciones   del lenguaje

import math as f                  #     CONCEPTOS  IMPORTANTES

nd = 0                     # nro decimales que se quiere tener,
a = round(23.66118,nd)     # redondeo  de un valor a un " nd " si es 0 NO necesario especificar
print(a)                           # EJERCICIOS     17    A  20

                           # CASOS
b = f.ceil(34.1953467)     # redondeo - truncamiento siempre hacia arriba y siempre a "0" decimales
print(b)
c = f.floor(34.1953467)    # redondeo - truncamiento siempre hacia abajo  y siempre a "0" decimales
print(c)
                                   # EJERCICIOS   21   A  23  TRUNCAMIENTO    a   VARIOS decimales
s = 45.17391
ds,es = f.modf(s)                  # con  modf  separa la parte decimal y entera del número
x = 3
c = round(ds,x)                    # redondea   la parte decimal  a x  decimales
if c > ds :                        # si REDONDEADA queda >
           c = c - 1/(10**x)       # le resta lo aumentado
s = es + c                         # obtiene  nuevamente el nro completo
print(s)
                          # las siguientes 2 instrucciones  SON equivalentes a las 8 ANTERIORES
s = 45.17391
c = f.floor(s*10**x)/10**x      # al valor le " corre " el punto decimal,lo TRUNCA a "0" decimales
print(c)                        # y luego le coloca el punto decimal donde corresponde.

from datetime import date

#11) FUNCIÓN recibe una fecha, entregar el número de días que faltan para terminar el año.

def DFTA(A, M , D):                       #  versión de dias faltan para terminar el año
    f_REVISAR  = date(A, M , D)           #  se recibe FECHA a analizar  y se obtiene
    DM = 31
    dft = date(A,12,DM) - f_REVISAR
    return dft

dfta = DFTA(2019, 10 , 23)
print("FALTAN PARA FIN DE AÑO", dfta)

#______________________________________________________________________________________
#10) FUNCIÓN recibe una fecha, entregar el número de días que faltan para terminar el mes.

def DFTM(A, M , D):                       #  versión de dias faltan para terminar el mes
    f_REVISAR  = date(A, M , D)           #   se recibe FECHA a analizar  y se obtiene
    DM = 31                               #   corregir ?? ,  para que funcione para cualquier MES
    dt = date(A,M,DM) - f_REVISAR
    return dt

dt = DFTM(2019, 10 , 23)
print("FALTAN PARA FIN DE MES ", dt)
#_______________________________________________________________________________

def edad_actual(A,M,D):                               #  versión calcular la  EDAD
    f_nacimiento = date(A, M, D)
    print(f_nacimiento)
    f_actual = date.today()                      #  toma  fecha ACTUAL del sistema
    ea = f_actual.year - f_nacimiento.year
    em = f_actual.month -f_nacimiento.month   # corregir para que NO muestre < 0, sino lo adecuado
    ed = f_actual.day - f_nacimiento.day      # corregir para que NO muestre < 0, sino lo adecuado
    return ea, em, ed

eca, ecm, ecd =  edadp(2003,12, 25)
print(eca, ecm , ecd )

_________________________________________________________________________________

import   FII_S
#9) EJERCICIO 09 del taller 4
#PROGRAMA que lea una serie de registros c/u con:   código estudiante, fecha de nacimiento,
#valor de su matrícula, determinar e imprimir:   edad actual de c/estudiante, porcentaje de
##promedio de matrícula de todos los estudiantes.

ctes = 0
ces18 = 0
vmatmy = -1
sumtmat = 0
cmnant = 0
vmeant = float("-inf")
ED = "S"
while ED == "S" :
            ces = FII_S.leemyo(10000)
            ane = FII_S.leemyo(1950)
            mne = FII_S.leerg(1,12)
            dme = FII_S.EJE06T03(mne,ane)
            dne = FII_S.leerg(1,dme)
            vme = FII_S.leerg(10,1000000)
            if ( vme < vmeant ) :
                            cmnant += 1
            vmneant = vme
            ctes += 1
            sumtmat +=  vme
            if vme > vmatmy :
                            vmatmy = vme
                            estmymat = ces
            ea,em,ed = edad_actual(ane, mne, dne)
            if ea >= 18 :
                       ces18 += 1
            print( ces, ea, em , ed)
            ED = input( " digitar   S para continuar  ó  N  para terminar ")
promat = sumtmat/ ctes
por18 = ces18 / ctes *  100
print ( por18 , estmay, promat ,cmnant)

#33- FUNCION  que reciba un valor entero mayor que cero,  entregar  ‘S’  si es un cuadrado
#                perfecto ó  ‘N’ sino lo es.

def EJ33T04(N):
    RC =  sqrt(N)                       #      RC = N ** 1/2         RC = pow(N,2)
    if RC == int(RC):
                       rpta = "S"
    else :
                       rpta ="N"
    return rpta
____________________________________________________________________________________________
#34-  FUNCION  que reciba un valor entero mayor que cero, obtener y entregar  el
#cubo perfecto más cercano al valor recibido.
.
def EJ34T04(N):
    PT = 1/3
    RC =  pow(N,PT)           #      RC = N ** 1/3         RC = pow(N,3)
    ERC = int(RC)             #      toma la parte de RC
    if RC == ERC:
             rpta = N
    else :
            CPA = pow(ERC,PT)                             # cubo perfecto  anterior a  N           # 45   pow(45,1/3) = 3.55689
            CPS = pow(ERC,PT)                             # cubo perfecto  siguiente a N           #    0,55689   -->   4.0    64 a 45 --> 19
            if N - CPA < CPS - N :                        # Aanalizar cual esta mas cerca de  N    #                    3.0    27 a 45 --> 18
                                 rpta = CPA
            else                 rpta = CPS
    return rpta

_________________________________________________________________________________________
# 18- FUNCION  que recibe un valor  N (>0)  y devuelva el valor de N aproximado (redondeado)
# a 1 decimal.   EJEMPLO  recibe   23.579264,  lo devuelve como  23.6;
#recibe 23.419 devuelve 23.4

def EJE18T04(N):
    NR = round(N,1)
    return NR
a =  EJE18T04(23,579264)
print(a)


#15) FUNCION que recibe 3 valores (> =0) y devuelve el MCM (mínimo común múltiplo) de los 3.
def MCMT(A,B,C):
    if A > 0 and B > 0   and  C > 0:
        A,B = ORDEN3(A,B,C)
        myr = C
        while True:
            if myr % A == 0 and myr % B == 0:
                return myr
            myr += C                                                                                   #??   mejor ir aumentando el myr c/vez en B, asi funciona
    else:
            return -1

MCXYZ = MCMT(X,Y,Z)
print(MCXYZ)

#16) FUNCION que recibe 5 valores y devuelve el MCM (mínimo común múltiplo) de los 5.
def MCMC(A,B,C,D,E):
                                                             # Devuelve el mínimo común múltiplo de dos números.
    if A > 0 and B > 0   and  C > 0  and D > 0 and E > 0:
.       A,B,C,D,E = ORDEN5(A,B,C,D,E)     ?? #  analizar   el efecto de esta instrucción ??
        mcm3 = MCMT(A,B,C)
        mcm5 = MCMT(mcm3,D,E)
        return mcm5
    else:
        return -1


# 57-PROGRAMA que lea una serie de valores, determinar e imprimir el menor de todos
# los valores y el promedio de los valores leídos antes del mayor.

mntv = float("inf")
mytv = -mntv
sanm = 0          ?? #  analizar   el efecto de esta instrucción ??
canmy = 0         ?? #  analizar   el efecto de esta instrucción ??
stv = 0
ctv = 0
ED = "S"
while  ED == "S"  :
                vlr = int(input())
                stv += vlr
                ctv += 1
                if vlr < mntv :
                         mntv = vlr
                if vlr > mytv :
                         mytv = vlr
                         sanmy = stv - vlr
                         canmy = ctv - 1
                ED =  input(" para continuar S  ó para terminar N ")
if canmy > 0  :
        prom = sanmy / canmy
        print(prom)
else :
        print (" no hubo  valores antes del mayor")


??       Puede y sera muy practico basarse en el anterior.

# 57 b -PROGRAMA que lea una serie de valores, determinar e imprimir el menor de todos
# los valores y el promedio de los valores leídos después del mayor.



#         EJERCICIOS     DEL  TALLER   03      SOLIICTADOS

def EJE10T03(dia,mes,año,nd):            # nd ( numero de días que se van a retroceder)
    dia = dia - nd
    while dia <= 0:
        mes = mes - 1
        if mes == 0:
            mes = 12
            año = año - 1
            dia = dia + EJE06T03(mes,año)
        else: dia = dia + EJE06T03(mes,año)
    return dia,mes,año
D, M, A = EJE10T03(15, 11, 2020, 45)
print(D,M ,A )
______________________________________________________________________________________
def EJE10aT03(dia,mes,año,nd):            # nd ( numero de días que se van a AVANZAR)
    dia = dia + nd
    DM = EJE06T03(mes,año)
    while dia > DM
        dia = dia - DM
        mes = mes + 1
        if mes >12 :
            mes = 1
            año = año + 1
        DM = EJE06T03(mes,año)
    return dia,mes,año
D, M, A = EJE10T03(15, 11, 2020, 45)
print(D,M ,A )

