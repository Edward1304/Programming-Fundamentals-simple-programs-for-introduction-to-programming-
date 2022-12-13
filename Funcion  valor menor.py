def valormenor1(A,B,C,D,E,F,G):
    R = 1
    while A>B or A > C or A>D or A>E or A>F or A>G:
        R = R+1
        A,B,C,D,E,F,G = B,C,D,E,F,G,A                   # hacer esta rotación, asumiendo su lenguaje
    rt = f"El valor menor es {A} y es el  {R} valor"    # no permite esta propiedad de  PYTHON
    return rt

mn  = valormenor1( 12,45, 6, 3,  33, 53, 34)
print ( mn)
s = mn - 3              #    al ejecutar la prueba muestra bien cual es el menor  de los 7
print(s)                #    y a que valor corresponde.  Pero MUESTRA error  al calcular s

#               ===============================================================

#  Después de Corregir  el problema al calcular   " s ", basado en ese mismo ejercicio hacer una
#  función que reciba 7  valores y  obtenga  el promedio de los 3 valores mayores del grupo de 7.
#  Recuerde   NO debe utilizar  if - listas - tuplas - archivos, seguir estrategia del  ejercicio



mn = valormenor1(23,56,78,90,12,54,12)
print(mn)
sd= mn-3
print(sd)