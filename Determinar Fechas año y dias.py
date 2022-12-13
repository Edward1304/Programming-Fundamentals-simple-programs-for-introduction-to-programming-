    
#24- FUNCION que reciba un valor  N (>0)   y  devuelva  la suma de los enteros desde 1 hasta N.
_______________________________________________________________________________________________
def EJE24T04(N):     #  versión 1
    SE = 0
    for en in range(1,N+1):                  #  1      2       3      4     5
                       SE +=  en
    return SE

#                 ______________________________________________________________
def EJE24T04(N):     #  versión 2
    SE = N
    for en in range(1,N):
                       SE +=  en
    return SE
#                 ______________________________________________________________
def EJE24T04(N):     #  versión 3
     SE = N * (N + 1) / (2*1)
     return SE
___________________________________________________________________________________________
#25- FUNCION que reciba un valor  N (>0)  y  devuelva  la suma de los  pares desde 1 hasta N.
def EJE25T04(N):     #  versión 1                                                                          # 1  10  :  2  4   6   8  10    30
    Sp = 0                                        # suma de                                                              # 1  15  :  3  6   9  12  15    45
    for par in range(1,N+1,2):                                                                      #    n * ( n + 2)/ ( 2*2)     30
                                Sp +=  par                                                       #    n * (n + 3 ) / (2*3)    15 *18 / 6   45
                                                                                                 #    n * ( n + MD ) / (2* MD)

    return Sp



??????        se  puede al igual que  en el ejercicio 24    hacer como la versión  2  y  3  ????

________________________________________________________________________________________________
#26- FUNCION que reciba un valor  N (>0)  y  devuelva  la suma de los impares  desde 1 hasta N.
def EJE26T04(N):     #  versión 1
    SI = 0
    for imp in range(1,N+1,2):                       SUMATODOS - SUMAPARES
                       SI +=  imp
    return SI
??????        se  puede al igual que  en el ejercicio 24    hacer como la versión  2   y  3  ????

???    como seria utilizando  adecuadamente las dos FUNCIONES  ANTERIORES. (  24    y  25)

???    como sumar  los múltiplos  de    x   hasta N    utilizando version 3 ? como es la formula??
______________________________________________________________________________________________

# EJERCICIOS 17   A  23   usando funciones   del lenguaje

import math as f                  #     CONCEPTOS  IMPORTANTES

nd = 0                     # nro decimales que se quiere tener,
a = round(23.66118)     # redondeo  de un valor a un " nd " si es 0 NO necesario especificar
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
__________________________________________________________________________________________
#34-  FUNCION  que reciba un valor entero mayor que cero, obtener y entregar  el
#cubo perfecto más cercano al valor recibido.
.
def EJ34T04(N):
    PT = 1/3
    RC =  pow(N,PT)           #      RC = N ** 1/3         RC = pow(N,3)
    ERC = int(RC)             #      toma la parte de RC
    if RC == ERC:
             rpta = N            40      3.41        3 ** 3      27
    else :                                           4 ** 3      64
            CPA = pow(ERC,3)                             # cubo perfecto  anterior a  N           # 45   pow(45,1/3) = 3.55689
            CPS = pow(ERC+1,3)                           # cubo perfecto  siguiente a N           #    0,55689   -->   4.0    64 a 45 --> 19
            if N - CPA < CPS - N :                       # Aanalizar cual esta mas cerca de  N    #                    3.0    27 a 45 --> 18
                                 rpta = CPA
            else :
                                 rpta = CPS
    return rpta

_________________________________________________________________________________________

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

#12) FUNCIÓN recibe dos fechas, entregar el número de días transcurridos entre las dos fechas.
import datetime as x
def nd_entrefechas(D1,M1,A1,D2,M2,A2):
    F1 = x.date(A1,M1,D1)
    F2 = x.date(A2,M2,D2)
    nd = abs(F1 - F2)
    nd = nd.days

    return nd

d= nd_entrefechas(10,2,2019, 23,2,2020)
print(d)


"""CT = 6,2,2,5,0,3,5,1,4,6,2,4
CL = [6,2,2,5,0,3,5,1,4,6,2,4]
print (type(CT), CT)
print (type(CL), CL)"""

# FUNCIONES NECESARIAS:

def EJE05T03(año):
    if año % 4 != 0: R = False
    elif año % 100 == 0:
        if año % 400 == 0: R = True
        else: R = False
    else: R = True
    return R

def EJE06T03(mes,año):
    while mes >= 1 and mes <= 12:
        M_30 = 4,6,9,11
        M_31 = 1,3,5,7,8,10,12
        if mes in M_30:
            return 30
        elif mes in M_31:
            return 31
        elif mes == 2:
            if EJE05T03(año):
                return 29
            else: return 28
    return 0

# ejercicio 39 clave del mes

def clave(A,M):
    if A >= 2000:
        C = 6,2,2,5,0,3,5,1,4,6,2,4
    else:
        C = 5,1,1,4,-1,2,4,0,3,5,1,3
    M = C[M-1]
    return M

# ejercicio 40   dia de la semana
def dia_semana(D,M,A):
    ult_2_A = A % 100
    cuart_ult2 = int(ult_2_A / 4)
    clave_M = clave(A,M)
    suma = ult_2_A + cuart_ult2 + D + clave_M
    resid = suma % 7         #  0    a   6
    resid += 1
    if EJE05T03(A):
        if M == 1 or M == 2:
            resid -= 1
            if resid == 0 :
                           resid = 7
    return resid

#EJ  29 FUNCION  que recibe un valor N (>0) y devuelva la suma de los términos de la siguiente serie:
#       1   2   4   7   11   16   22   29     ¿?  . . . . . . . . . . . . . . .   N

def Suma_terminos_en_serie(N):
    secuencia_terminos=1
    numero=1
    suma_terminos=0

    while numero < N:
        suma_terminos+=numero
        numero+=secuencia_terminos
        secuencia_terminos+=1
    return suma_terminos

test= Suma_terminos_en_serie(10)
print(test)
"""
j = 40             #   ejemplo de for ,  para lo que le explico enseguida
k = 3
for i in range(1,j,k):
             print(i,k)
             k += 1


       #  no es práctco hacerlo con  for, porque CUANDO lo define asi se queda,
       #   así haga modificacione a las variables del for

for numero in range(1,N+1,secuencia_próximo_termino):

    # Si inicializo la variable recorrido_numero en 1,la suma hasta 29 estaría correcta, sin embargo
        #los cálculos no me dan, por lo que la inicalizo en 0, sin em bargo no logro evidenciar el error

        recorrido_numero+=1
        numero+= recorrido_numero
        suma_terminos=numero+recorrido_numero
        secuencia_próximo_termino+=1

    return suma_terminos

#EJ
"""
#EJ 27
def Sumatoria_primos_1_hasta_N(N):
    suma_primos=5
    for numero in range (5,N+1,21):                            #  in = 1
        es_primo= F1.Saber_si_es_primo_o_no_e2(numero)        #  while in < N:
        if es_primo== True:                                   #
            suma_primos+=numero#
    return suma_primos


#EJ 28
def Sumatoria_no_primos_1_hasta_N(N):          #     ej24 - ej27
    suma_no_primos=0
    for numero in range (1,N+1,1):
        es_primo= F1.Saber_si_es_primo_o_no_e2(numero)
        if es_primo== False:
            suma_no_primos+=numero

    return suma_no_primos

test=  Sumatoria_no_primos_1_hasta_N(5)
print(test)



