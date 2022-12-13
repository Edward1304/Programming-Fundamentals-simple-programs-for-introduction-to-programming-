#             Solución 1 de 4 al ejercicio ZZZ planteado de juntar dos  LISTAS elemento a elemento
#             y al terminar la mas corta  retomarla nueva/. hasta terminar la mas larga


def JUNTAR (LAA,LBB):
    LIS = []
    B = len(LAA)
    C = len(LBB)
    if (B>=C):
        MAY = B
        MEN = C
    else:
        MAY = C
        MEN = B
    if (MAY==B):
     Y = (2*MEN)
     H = 1
     while (Y<MAY):
         Y = (Y+C)
         for A in range (0,MEN):
          LBB.append(LBB[A])
     for A in range (0,MEN,1):
        LIS.append(LAA[A])
        LIS.append(LBB[A])
     for A in range (MEN,MAY):
         LIS.append(LAA[A])
         LIS.append(LBB[A-(MEN*H)])
    else:
     Y = (2*MEN)
     H = 1
     while (Y<MAY):
         Y = (Y+B)
         for A in range (0,MEN):
          LAA.append(LAA[A])
     for A in range (0,MEN,1):
      LIS.append(LBB[A])
      LIS.append(LAA[A])
     for A in range (MEN,MAY):
        LIS.append(LBB[A])
        LIS.append(LAA[A-(MEN*H)])
    return (LIS)

LA = [10,20,30,40,50,60,70,80,90,100]
LB = [1,2,3,4,5,6,7,8]                  # listas para probar JUNTAR
Y = JUNTAR (LA,LB)                      # Observar funcionalidad con lARGA primero y luego CORTA
Z = JUNTAR (LB,LA)                      # y al contario

print ("Sol 1", Y)

#====================================================================================

#             Solución 2 de 4 al ejercicio ZZZ planteado de juntar dos  LISTAS elemento a elemento
#             y al terminar la mas corta  retomarla nueva/. hasta terminar la mas larga

def unir( y,z):
    lyz=[]
    ly = len(y)
    lz = len(z)
    ry = 0
    for rz in range(lz):
                        lyz.append(y[ry])
                        lyz.append(z[rz])
                        ry+=1
                        if ry >= ly :
                                ry = 0
    return lyz

def mezclar( a, b):
    la = len(a)
    lb = len(b)
    if la <= lb :
                 ab = unir(a,b)
    else :
                 ab = unir(b,a)
    return ab

LA = [10,20,30,40,50,60,70,80,90,100]
LB = [1,2,3,4,5,6,7,8]                 # lista para probar  mezclar
Y = mezclar(LA,LB)                     # Observar funcionalidad con lARGA primero y luego CORTA
Z = mezclar(LB,LA)                     # y al  contrario

print(" Sol 2 " , Y)

#==========================================================================================
#             Solución 3 de 4 al ejercicio ZZZ planteado de juntar dos  LISTAS elemento a elemento
#             y al terminar la mas corta retomarla nueva/. hasta terminar la mas larga.

def unir1( y,z,p):
    yz = []
    ly = len(y)
    lz = len(z)
    ry = 0
    if p == 1:
            for rz in range(lz):                  #   unirf(y,z,ly,lz,yz,ry), CREAR esta función
                        yz.append(y[ry])          #   para que no le quede casi que REPETIDO
                        yz.append(z[rz])          #   este código  con el del  "else"
                        ry+=1
                        if ry >= ly :
                                    ry = 0
    else :
            for rz in range(lz):                  #  unirf(z,y,lz,ly,yz,ry), utilizar la FUNCIÓN
                        yz.append(z[rz])          #  propuesta 7 instrucciones antes
                        yz.append(y[ry])
                        ry += 1
                        if ry >= ly :
                                    ry = 0
    return yz

def mezclar1( a, b):
    ab = []
    la = len(a)
    lb = len(b)
    if la <= lb :
            ab = unir1(a,b,1)       # 1  para indicar que PRIMERO adiciona los de primera LISTA
    else :
            ab = unir1(b,a,2)       # 2  para indicar que PRIMERO adiciona los de segunda LISTA
    return  ab

LA = [10,20,30,40,50,60,70,80,90,100]
LB = [1,2,3,4,5,6,]                      # lista para probar  mezclar1 la prueba
Y = mezclar1(LA,LB)                      # Observar funcionalidad con lARGA primero y luego CORTA
Y = mezclar1(LB,LA)                      # y al  contrario
print(" for3 " , Y)


#======================================================================================
#             Solución 4 de 4 al ejercicio ZZZ planteado de juntar dos  LISTAS elemento a elemento
#             y al terminar la mas corta retomarla nueva/. hasta terminar la mas larga

def ZZZ(listaa,listab):                      #   trenza dos listas que tiene igual cantidad
	longitud = len(listaa)                   #   de elementos
	lista_resultado = []
	for i in range(longitud):
		lista_resultado.append(listaa[i])
		lista_resultado.append(listab[i])

	return lista_resultado


def crecer(p,q):                          # hacer que la lista corta quede con la misma cantidad
    lp = len(p)                           # de elementos a la lista larga
    lq = len(q)
    if lp < lq :
                coc = lq // lp             # Número de veces exactas que la corta CABE en la larga.
                res = lq % lp              # los que faltaron para que los dos listas sean iguales
                for r in range(coc-1):     # Extiende la corta sobre si misma las veces necesarias
                    for i in range(lp) :                                                               # extend
                        p.append(p[i])
                for r in range (res) :     # le adiciona el resto pendiente
                       p.append(p[r])
                lp += lp
    elif lp > lq :                         #  proceso IGUAL al anterior para caso contrario
                coc = lp // lq             #  en tamaño de listas
                res = lp % lq
                for r in range(coc-1):
                    for i in range(lq) :
                        q.append(q[i])
                for r in range (res) :
                        q.append(q[r])
                lq += lq



 # lo planteado en el  VERDADERO y el FALSO del " if "  deb hacerse en una SOLA FUNCIÓN
 # que sirva para ambas situaciones.

 #   ya las dos listas quedaron de igual tamaño, utilizando ZZZ unirlas apropiadamente
 #   para que la recibida primero se combine con la otra



 #   En las soluciones  1 2 se combinaron las dos listas así : un elemento de la lista LARGA
 #   y uno de la lista CORTA

 #   En la solución 3  se combino uno de la lista que se enviá de PRIMERA y uno de la SEGUNDA, etc

 #   La solución 4 a terminar por UD debe quedar como en la 3 uno de la PRIMERA y uno .......


 #   HAcer solución 5: combine uno de la primera con uno de la segunda, etc    Y
 #                     si termina la CORTA la retome en sentido contrario a como lo hizo anterior/.
 #                     Hacerla en base a la solución 4, que las dos listas queden de igual tamaño
 #                     utilizando algunos de los conceptos que se explican a continuación.

#=========================================================================================



z = [ 3, 8, 34, 32,  57, 21, 22,  98, 65]

c = z                    #   crea una copia de una LISTA ,  ambas quedan como si fuera una sola
                         #   lo que se haga en una tiene efecto en la otra.
print(c)
c[1]= 10          #   sin hacerlo z[1] queda valiendo 10
z.sort()          #   se ordenan LISTA z y  sin haberlo indicado LISTA c  queda ordenada
print (c, z)




cc = list(z)          #   crea una copia de una LISTA , quedan c/u INDEPENDIENTE de la otra.                       #   lo que se haga en una tiene efecto en la otra.
cc[2] = 7             #   NO sucede nada en z
z[1] = 45             #   NO sucede nada en cc
print(cc,z)



z.extend(z)          # la lista Z se copia sobre si misma o sea se duplica, en este ejemplo.
print (z)








