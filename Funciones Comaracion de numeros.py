#import random,math,msvcrt

# MENOR
def mnc():
    X = 0
    while X >= 0:
        X = int(input("Digite un número menor que 0 :"))
def mnr(P):
    X = int(input(f"Digite un número menor que {P} :"))
    while X >= P:
        X = int(input(f"Digite un número menor que {P} :"))
    return X
def mnr_3(X,Y,Z):
    if(Z > X < Y): RT = X
    elif(Z > Y < X): RT = Y
    else: RT = Z
    return RT
# DIFERENTE
def dfc():
    X = 0
    while(X == 0):
        X = int(input("Digite un número diferente de 0 :"))
    return X
def dfr(P):
    X = int(input(f"Digite un número diferente de {P} :"))
    while X == P:
        X = int(input(f"Digite un número diferente de {P} :"))
    return X
def dfo_1(A):
    X = int(input(f"Digite un número diferente de {A} :"))
    N = 1
    while X == A and N < 3 :
        X = int(input(f"Digite un número diferente de {A} :"))
        N = N + 1
    if X == A: return
    else: return X
# MAYOR
def myc():
    X = 0
    while X <= 0:
        X = int(input("Digite un número mayor que 0 :"))
def myr(P):
    X = int(input(f"Digite un número mayor que {P} :" ))
    while(X <= P):
        X = int(input(f"Digite un número mayor que {P} :" ))
    return X
def myc_dfr(P):
    X = int(input(f"Digite un número mayor que cero y diferente de {P} :"))
    while X == P or X <= 0:
        X = int(input(f"Digite un número mayor que cero y diferente de {P} :"))
    return X
def myc_dfrs(P,Q):
    X = int(input(f"Digite un número mayor que cero y diferente de {P} y {Q} :"))
    while X == P or X == Q or X <= 0:
      X = int(input(f"Digite un número mayor que cero y diferente de {P} y {Q} :"))
    return X
def myo_dfo(P,Q):
    X = int(input(f"Digite un número mayor que {P} y diferente de {Q} :"))
    while X <= P or X == Q:
        X = int(input(f"Digite un número mayor que {P} y diferente de {Q} :"))
    return X
def myo_dfos(P,Q,R):
    X = int(input(f"Digite un número mayor que {P} y diferente de {Q} y {R} :"))
    while X <= P or X == Q or X == R:
      X = int(input(f"Digite un número mayor que {P} y diferente de {Q} y {R} :"))
    return X
def myoOdfo(P,Q):
    X = int(input(f"Digite un número mayor que {P} ó diferente de {Q} :"))
    while X <= P and X == Q:
      X = int(input(f"Digite un número mayor que {P} ó diferente de {Q} :"))
    return X
def myoOdfosS2(P,Q,R):
    X = int(input(f"Digite un número mayor que {P} ó diferente de {Q} y {R} :"))
    while (X <= P and X == Q) or (X == R):
        X = int(input(f"Digite un número mayor que {P} ó diferente de {Q} y {R} :"))
    return X
def myrdtos(W,X,Y,Z):
    if(W >= X and W >= Y and W >= Z):
        myr = W
        P = "primer"
    elif(X >= W and X >= Y and X >= Z):
        myr = X
        P = "segundo"
    elif(Y >= W and Y >= X and Y >= Z):
        myr = Y
        P = "tercer"
    else:
        myr = Z
        P = "cuarto"
    return f"El número mayor es {myr} y es el {P} valor."
    """myr = max(W,X,Y,Z)
    if myr == W: P = "primer"
    elif myr == X: P = "segundo"
    elif myr == Y: P = "tercer"
    else: P = "cuarto"
    return f"El número mayor es {myr} y es el {P} valor."""
# PRIMO
def es_primo(N):
    if N == 1 or N == 0:
        return False
    elif N == 2:
        return True
    elif N > 2:
        for divisor in range(2,N):
            if N % divisor == 0:
                return False
            elif N % divisor != 0 and divisor == N-1:
                return True
# PAR O IMPAR
def es_impar(X):
   X = int(X)
   if X % 2 == 0:
        return True
   else:
        return False
def es_par(X):
   X = int(X)
   if X % 2 == 0:
        return True
   else:
        return False
def impar_dfr(A):
    X = int(input(f"Digitar un número impar diferente de {A} :"))
    while X == A or (X % 2) == 0:
        X = int(input(f"Digitar un número impar diferente de {A} :"))
    return X
def par_dfr(A):
    X = int(input(f"Digitar un número par diferente de {A} :"))
    while X == A or (X % 2) != 0:
        X = int(input(f"Digitar un número par diferente de {A} :"))
    return X
# TERMINE EN:
def ter_en(N):
    X = int(input(f"Digite un número que termine en {N} :"))
    while X % (10**EJE01T02e2cmd(N)) != N:
        X = int(input(f"Digite un número que termine en {N} :"))
    return X
def myr_M_ter_N(M,N): # Devuelve un valor que es mayor que M y termina en N
    X = int(input(f"Digite un número mayor que {M} que termine en {N} :"))
    while X % (10**EJE01T02e2(N)) != N or X <= M:
        X = int(input(f"Digite un número mayor que {M} que termine en {N} :"))
    return X
# INCREMENTA
def incr_P_myr_Q(X,P,Q):# Devuelve un valor X incrementado en P hasta superar Q
    while X <= Q:
        X = X + P
    return X
def sqrt(X):
    return(X ** (1/2))



"""ED = "S"
regis = 0
while ED == "S" or ED == "s":""" # Inicio de un programa
"""regis = regis + 1""" # Cuenta los registros
""" """
"""ED = input("Digite 'S' si desea repetir el programa :")"""
# Final de un programa