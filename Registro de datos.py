def EJP01T03(E):
    E = abs(E)
    CD = 0
    PD = 1
    if E == 0:
        CD = 1
        PD = 0
    SD = 0
    UD = 1
    while E > 0:
        UD = E % 10
        CD = CD + 1
        SD = SD + UD
        PD = PD * UD
        E = E // 10
    return CD, SD, PD




STP = 0
PTS = 1
MNT = 999999999
ED = "S"
regis = 0
while ED == "S" or ED == "s":
    regis = regis + 1
    print(f"REGISTRO {regis}")
    PV = int(input("Digite el primer número : "))
    SV = int(input("Digite el segundo número : "))
    TV = int(input("Digite el tercer número : "))
    CD_PV, SD_PV, PD_PV = EJP01T03(PV)
    CD_SV, SD_SV, PD_SV = EJP01T03(SV)
    CD_TV, SD_TV, PD_TV = EJP01T03(TV)
    STP = STP + PV
    if PV != 0:
        PTS = PTS * SV
    if TV < MNT:
        MNT = TV
        pos_M = regis
    print(PV,CD_PV, SD_PV, PD_PV)
    print(SV,CD_SV, SD_SV, PD_SV)
    print(TV,CD_TV, SD_TV, PD_TV)
    ED = input("Digite 'S' si desea continuar : ")
PromePV = STP / regis
print(STP,PromePV,PTS,MNT,pos_M)