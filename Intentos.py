#Función que me devuelve un número diferente de otro. Y que no exeda 3 intentos
def attemps(num):
    dig = int(input(f"Digite un número diferente de {num} :"))
    i = 1                    # Si queremos que sean 4 intentos ponemos <=
    while dig == num and i < 3 : # Si queremos que sean 3 intentos ponemos <
        X = int(input(f"Digite un número diferente de {num} :"))
        i = i + 1
    return X      #La función planteada tiene un problema al retornar X
                    # Cuando ejecutamos el programa, al exceder 3 intentos
                    #   este nos devuelve el valor X que es el número digitado.


print(dfo(50))  # En este caso el programa nos devuelve 50
                        #     después de exceder los 3 intentos
                        # Por favor verificar.


