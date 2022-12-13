def EJE01T02e1(X):
    X = abs(X)
    if X < 10: RT = 1
    elif X < 100: RT = 2
    else: RT = 3
    return RT
def EJE01T02e2(X):
    X = abs(X)
    PC = 10
    CD = 1
    while X >= PC:
        PC = PC * 10
        CD = CD + 1
    return CD
def EJE01T02e3(X):
    X = abs(X)
    CD = 0
    if X == 0:
        CD = 1
    while X > 0:
        X = X // 10
        CD = CD + 1
    return CD
def EJE01T02e4(X):
    X = abs(X)
    CD = 0
    if X == 0:
        CD = 1
    while X > 0:
        X = X % 10
        CD = CD + 1
    return CD
    
def EJE01T02e5(X):
    X = abs (X)
    X = int(X)
    X = str(X)
    X = len(X)
    return X
def EJE02T02(X,Y):
    if(X >= Y): return Y
    else: return X
    """
    return min(X,Y)
    """
def EJE03T02(X,Y,Z):
    """return(max(X,Y,Z))
    """
    if(Z <= X >= Y): RT = X
    elif(Z <= Y >= X): RT = Y
    else: RT = Z
    return RT
######### def EJE03CT02(W,X,Y,Z):
def EJE04T02(X,Y):
    P = float(input(f"Digitar un número mayor que {X} ó menor que {Y}"))
    while (P <= X and P >= Y):
        P = float(input(f"Digitar un número mayor que {X} ó menor que {Y}"))
    return P
def EJE05T02(X):
    if X < 10: R = 1
    """
    elif X < 20: R = 2
    elif X < 30: R = 3
    elif X < 40: R = 4
    else: R = 5
    return R
    """
    C = 10
    R = 1
    while X >= C:
        C = C + 10
        R = R + 1
    return R
def EJE06T02(X):
    return(round(X/10)*10)
def EJE07T02(X):
    while X <= 50:
        X = X + 7
    return(X)