import F_IIS
ED = "Y"
while ED =="Y":
    A = F_IIS.myr(0)
    B = F_IIS.dfr_myc(A)
    C = F_IIS.dfrs_myc(A,B)
    print("Número insertado --> cantidad de dígitos")
    Dig_A = F_IIS.EJE01T02e2(A)
    Dig_B = F_IIS.EJE01T02e2(B)
    Dig_C = F_IIS.EJE01T02e2(C)
    print(f"{A} --> {Dig_A}")
    print(f"{B} --> {Dig_B}")
    print(f"{C} --> {Dig_C}")
    print("Número insertado --> Redondeado a decena más próxima")
    round_A = F_IIS.EJE06T02(A)
    round_B = F_IIS.EJE06T02(B)
    round_C = F_IIS.EJE06T02(C)
    print(f"{A} --> {round_A}")
    print(f"{B} --> {round_B}")
    print(f"{C} --> {round_C}")
    print("Número insertado --> Aumentado en 7")
    aumen_A = F_IIS.EJE07T02(A)
    aumen_B = F_IIS.EJE07T02(B)
    aumen_C = F_IIS.EJE07T02(C)
    print(f"{A} --> {aumen_A}")
    print(f"{B} --> {aumen_B}")
    print(f"{C} --> {aumen_C}")
    ED = input("Digite 'Y' si desea reiniciar el programa :")