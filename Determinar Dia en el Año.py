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



# inicio de programa 



from  datetime import date
print("Ingrese el numero del mes y del dia ")
M,D= map(int,input().split())
A= int(input("Ingresa el año: "))
S={1: 1,  2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

ND= date.isoweekday(date(A,M,D))

print("Posicion de la fecha en la semana es:  %s" %S[ND])
FCH=(A,M,D)

print(f"Fecha ingresada: {FCH}")

if ND>5:
	DV= ND-5

elif ND<5:
	DV= 5 - ND
	
else: 
	DV= 5


print(f"Dias de diferencia  al viernes: {DV}")
if ND > 5:
	D = D - DV
	if D == 0:
		M = M -1
		if M == 0:
			M = 12
			A = A -1
			D = EJE06T03(M,A)
		D = EJE06T03(M,A)
	FCHF=(A,M,D)

elif ND < 5:
	D = D + DV
	NDM = EJE06T03(M,A)
	while D > NDM:
		D = 1
		M = M + 1
		while M ==13:
			M = 1
			A= A + 1
	FCHF=(A,M,D)
else:
	FCHF=(A,M,D)

print(f"Fecha  del viernes de esa semana: {FCHF}")
print("")
print("")


S2={1: 1,  2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
ND2= date.isoweekday(date(A,12,31))
FCHFA=(A,12,31)
print(f"Ultima fecha  del año :  {FCHFA}")
print("Posicion de la fecha en la semana final del añ0:  %s" %S2[ND2])
if ND2>5:
	DV2= ND2-5

elif ND2<5:
	DV2= 5 - ND2
	
	
print(f"Dias de diferencia  a   viernes: {DV2}")



A2 = A
M2 = 12
D2 = 31


if ND2 > 5:
	D2 = D2 - DV2
	if D2 == 0:
		M2 = M2 -1
		if M2 == 0:
			M2 = 12
			A2 = A2 -1
			D2 = EJE06T03(M2,A2)
		D2 = EJE06T03(M2,A2)
	FCHF=(A2,M2,D)

elif ND2 < 5:
	D2 = D2 + DV2
	NDM2 = EJE06T03(M,A)
	while D2 > NDM2:
		D2 = 1
		M2 = M2 + 1
		while M2 ==13:
			M2 = 1
			A2= A2 + 1
	FCHF2=(A2,M2,D2)
else:
	FCHF2=(A2,M2,D2)



print(f"Fecha  del viernes de esa semana: {FCHF2}")
print("")
print("")

F1= date(A,M,D)
F2= date(A2,M2,D2)

F= F2 - F1

print(f"Direncia entre viernes : {F.days}  dias")

R = F.days//7


if M2 > 0 and M2<=1:
	RF= R -1
	print( f"Viernes de diferencia  {FCHF} entre {FCHF2}:   {RF} viernes")
else:
	RF= R -1
	print( f"Viernes de diferencia  {FCHF} entre {FCHF2}:   {RF} viernes")






