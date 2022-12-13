#Taller  5

#Avance
# Edward Fabian Goyeneche	
#Laura Natalia Hurtado 
#subgrupo G

#PNT1TLL5
from FNFDC import FN5TLL2

def EMLIST (L, V1):
	L1=[]
	for i in  range (1): 
		L1.append(V1)
	return L1


print("Al terminar  los registros , ingrese '0'  para  culminar")
VFS=int(input("Ingrese un valor, para continuar o salir"))
LS=[]
while VFS != 0:
	LS.append(VFS)
	VFS =int(input("Ingrese un valor, para continuar o salir"))
LSD=EMLIST(100,0)
for R in range(len(LS)):
	D= abs(LS[R]) % 100
	LSD[D] += LS[R]
for i in range(len(LSD)):
	if LSD[i] > 0 :
		print(f" La Suma de los valores  que los  2 ultimos dijitos  ternminan en {1}: {LSD[in]}")




#PNT2TLL5


VFS= int(input("Ingrese un valor, para continuar o salir"))
LS = []
while VFS != 0:
	LS.append(VFS)
	VFS = int(input("Ingrese un valor, para continuar o salir"))
LSD= EMLIST(10,0)
for i in range(len(LS)):
	D= abs(LS[i]) % 100
	RD= FN5TLL2(D) - 1
	LSD[RD] += LS[i]
RG1 = 0
RG2 = 9
RG3 = 0

for N in range(10):
	if N > 0:
		RG1 += 10
		RG2 += 10
		RG3 += 1
	RT = f"Resultado de la suma que estan entre{RG1} a {RG2}: {[RG3] LSD} "






def DTRSACAA(D,M,A):
	DTR = D

	for AM in  range(1,M):
		DTR += FN6TLL3(AM,A)
	return DTR



def CNVRTFCH(FCH):
   FCH = int(FCH[0]),int(FCH[1]),int(FCH[2])
   return FCH



OPS = "S"
 DA = EMLIST(366,0)
 while OPS == "S" or OPS == "s":
 	CDG = float(input("Ingrese Codigo del EMPLEADO: "))
 	FCHNA= str(input("Ingrese la  fecha de nacimiento (Dias / Mes / Año"))
 	D,M,A= CNVRTFCH(FCHNA)
 	SLD= int(input("Ingrese el SUELDO: "))
 	DDA= DTRSACAA(D,M,A)
 	DA[DDA - 1] += 1
 	OPS = input ("-S-  para continuar: ")
for N in range(len(DA)):
	if DA[N]> 0:


		print(f"Los EMPLEADOS  que nacimiento en el dia {X+1} del Año: {DA[N]}")

