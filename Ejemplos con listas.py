#      l i s t a s       --   arreglos
import math as mt
#
def inlst(l, vi):                         # función para INICIALIZAR una lista   lst de l elementos
    lst = []                              # en un valor vi
    for i in range(l):
        lst.append(vi)
    return lst


s = inlst(10,0)   ;
print (s)
ns = s                                       # metodos  que  aplican   a  LISTAS
os =[]
print(s,ns,os)
for i in range(len(s)):
    os.append(s[i])                          # adiciona elementos a una lista
s[2] +=  3                                   # modifica un elemento de una lista
print(s,ns,os)
s.clear()
print(s,ns,os)
s = os
print(s,ns)
ns = s
print(s,ns)
print(s.count(5),s.index(5))
s.insert(2,7)
print(s.count(7),s.index(7),s)
l = [5,10,15,25,10,5,15,5,12]
n = len(l)
l.insert(n,30)
print(l)
l.pop(2)                 # borra elemento de un posición
print(l)
l.remove(25)             # elimina el primer valor
print(l)


#               De un número recibido, retornar los divisores exactos

def dve1(N):                         #   revisar y reformar para si  N es IMPAR mejorar
    dve= []                          #   crea LISTA  vacia
    for dv in range(1, N+1) :        #   GENERA LOS NÚMEROS DESDE 1  HASTA N    EN dv
        if N % dv == 0 :             #   si dv divide EXACTAMENTE A N lo adiciona a la lista
                       dve.append(dv)
    return dve
dv = dve1(500)
print(dv)


def dve2(N):
    dve= []
    li = N // 2                       # Determir la mitad de N, para buscar única/. hasta la 1/2
    for dv in range(1, li+1):         # revisar y reformar para si  N es IMPAR mejorar
        if N % dv == 0 :
                       dve.append(dv)
    return dve                         # revisar y  corregir, le esta faltando el último divisor
dv = dve2(500)
print(dv)


def dve3(N):
    dve= []
    li = int(mt.sqrt(N))
    for dv in range(1, li+1):             # revisar y reformar para si  N es PAR mejorar
        if N % dv == 0 :
                       dve.append(dv)
    return dve                            # revisar y  corregir, le estan faltando varios
dv = dve3(500)                             # después de corregirlo, probar con  50  y 100
print(dv)                                 # si nuevamente falla  para 100, corregirlo


def mnmyprom(vls,promvls):               # vls :  lista a revisar
    cel = len(vls)
    mnp = []                             # lista para los <  al promedio
    myip = []                            # lista para los >= al promedio
    for p in range(cel):
        if vls[p] < promvls :
                    mnp.append(vls[p])
        else :
                    myip.append(vls[p])
    return mnp,myip


def mnprom1(vls,promvls):                          # vls :  lista a revisar
    cel = len(vls)
    mnp = []                                       # lista para los <
    myip = []                                      # lista para los >=
    for p,vl in enumerate(vls):
        if vl < promvls :
                    mnp.append(vl)
        else :
                    myip.append(vl)
    return mnp,myip

#                                    E J E M P L O   :
#      leer una serie de valores  ,  obtener UNA lista con los menores al promedio de todos
#      y una lista con los mayores ó iguales al promedio
#            lv [ 34     29    4      17       45        178 ]     ??  pr  = sumatodos/cantidad
#           ind    0      1    2      3        4          5

vlc= 999999
vlap = int(input(" digitar un valor ,  para Terminar digitar 999999"))
lv = []

while vlap != vlc :
    lv.append(vlap)
    vlap = int(input(" digitar un valor ,  para Terminar digitar 999999"))

prom = sum(lv)/len(lv)
print(lv, round(prom,2))

mn_myp = mnmyprom(lv,prom)
a,b = mn_myp
x = mn_myp[0]
y = mn_myp[1]
print(mn_myp, x , y, a, b)

#lsnp1 = mnprom1(lv,prom)
#print(lsnp1)



#                                         EJERCICIOS        T A L L E R      5

#    EJ01T05

vlc= 999999
vlap = int(input(" digitar un valor ,  para Terminar digitar 999999"))
lv = []                                 #  LISTA   para guardar TODOS los valores
while vlap != vlc :                     #  es estricta/. necesaria esta LISTA
    lv.append(vlap)                     #  lee  valores y  los adiciona a la lista
    vlap = int(input(" digitar un valor ,  para Terminar digitar 999999"))

lstdu=inlst(100,0)                      # crea LISTA para ACUMULAR valores terminados en :

cvl = len(lv)                           #  obtiene tamaño de la lista
for rl in range(cvl) :                  #  Genera todos los INDICES ( posiciones ) de la lista
              du = lv[rl] % 100         #  obtiene los DOS últimos dígitos del elemento de la LISTA

              lstdu[du] += lv[rl]       # adiciona a LSTDU en la posición adecuada según 2 últimos
                                        # dígitos el valor de la lista LV
print(lstdu)  #  mejorar impresion para dar claridad al usuario



