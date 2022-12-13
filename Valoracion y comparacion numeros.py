def EJE01T02e1(A):
    A = abs(A)
    if A < 10 : Z = 1
    elif A < 100 : Z = 2
    else: Z = 3
    return Z

def EJE01T02e2(A):
    A = abs(A)
    PC = 10
    CD = 1
    while A > PC :
                PC = PC * 10
                CD = CD + 1
    return CD

def EJE01T02e3(A):
    A = abs(A)
    CD=0
    while A > 0:
        A = A // 10    #    // <==   DIVIDIR con resultado entero
                       #    A = int ( A/10 )
        CD=CD + 1
    return CD

def EJE01T02e4(A):
    A = abs(A)
    CD=0
    while A > 0:
        UD = A % 10   # % <== OBTIENE RESIDUO DE una divisón EJEMPLO 34 % 7 = 6
        CD=CD + 1
        A = int(A / 10)
    return CD

def EJE01T02e5(A):
    ACAD = str(A)
    CD = len(ACAD)
    return CD

# PRUEBA DE LAS 5 FUNCIONES IMPLEMENTADAS CON DIFERENTES ESTRATEGIAS

VP  = 19865
re1 = EJE01T02e1(VP)
re2 = EJE01T02e2(VP)
re3 = EJE01T02e3(VP)
re4 = EJE01T02e4(VP)
re5 = EJE01T02e5(VP)
print(re1,re2,re3,re4,re5)

