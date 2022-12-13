#Pof favor revisar  la ultima parte, es un error de sintaxis para
# transformar el  formato d fechas para que se restar
def EJE05T03(año):
    if año % 4 != 0: R = False
    elif año % 100 == 0:                       #<---Funcion que  define si el año
        if año % 400 == 0: R = True            # es bisiesto
        else: R = False
    else: R = True
    return R

def FNCNS(A):
	S=(EJE05T03(A))                    #<---Funcion que  hace el nuemro de semanas de un año
	if S == True:                      # sin importar si es bisiesto o no
		NDSEX= 366//7
		return NDSEX
	else:
		NDSEX= 365//7
		return NDSEX

def REDONNUMSEM(D):                   #<--funcion que  saca las semanas exactas de
	R= D//7                           #los dias que sea
	return R


#Punto  43  taller 04                             #<----Mi propuesta para la solucion de este punto , rige
from datetime import date                         #en hallar  la semana  en que esta la fecha ingresada
D= int(input("Ingrese el Dia:   "))               # y la de la ultima del año, al hacer esto se puede hallar
print("")             # debe validar              # el dia viernes de esas semanas
M= int(input("Ingrese el Mes:   "))               # despues de esto , se hace la direncia de dias que hay entres esas dos
print("")              #  debe validar            # esas dos fecha entre los viernes, los cueles se  operaran en semanas completas
A= int(input("Ingrese el Año:   "))               # y  de ahi se obtienen  la cantidad exactas de viernes que faltan para terminar el año
print("")               # debe validar
print(f"Fecha ingresada: {D} / {M} / {A} ")
print("")
FCH1= date(A,M,D)
NDSA=FNCNS(A)
print(NDSA)
print("")
print(f"--Fecha actual:  {FCH1}")     #  ??? actual ??    INGRESADA 1
print("")
NS= FCH1.isocalendar()
print("--Numero de la semana fecha ingresada :",NS[1])
print("")
F1 = NS[1]
FF= NDSA
DFDS= round (FF - F1)
print(f"--Semanas que faltan para  que se termine el año : {DFDS}  Semanas")
print("")
import time
NSF= F1
FCH= time.asctime(time.strptime(f"{A} {F1-1} 5" , "%Y %W %w"))
print(f"--EL viernes de  la semana  de la fecha {FCH1}    =",FCH)
print("")
NSFA= FF
FCHF=time.asctime(time.strptime(f"{A} {NDSA-1} 5" , "%Y %W %w"))
print(f"--El ultimo viernes del año{A} =",FCHF)
print("")  # hasta este punto el programa funciona correctamente
print("")
from datetime  import date
FCHF1 = date(FCH([4],[2],[1]))     # <--la idea en esta parte es buscar como transformar la fecha a una fecha
FCHF2= date(FCHF([4],[2],[1]))     # que se pueda  restar para hallar los dias de  direncia.
R = FCHF2 - FCHF1                  #<----En esta parce , lo que se hace es restar  las dos fechas para hallat los dias
R1=(R.days)                        # que son los dias que separan los viernes que  desde la semana de la fecha hasta
print(R1)                          #hasta el ultimo viernes del mes, los cuales son semanas exactas que se transforman
                                   #en  viernes que hay
NDVIER= REDONNUMSEM(R1)
print (f"Numero de viernes que faltan desde la semana {F1},  hasta que se acabe el años, son : {NDVIER} viernes")

















