from collections import Counter

#   conceptos   y    uso de   cadenas   -  string    -  textos    METODOS  y FUNCIONES de str


ciudad = "Manizales"                       # asignar  a una variable un valor  en "carcteres"
país = "Colombia"
tstr = len(ciudad)                         # len   obtiene  el tamaño de la cadena

ciud_país = ciudad + " " + país
print(type(ciudad))
print(ciudad,"    ",ciud_país)
print(tstr)


for i in range(tstr):
   print("%3c %s " % (ciudad[i], ciudad))

for i in range(tstr-1,-1,-1):
      print("%3c %30s " % (ciudad[i], ciudad))

print(ciudad.count('a'))               # cuenta
print(ciudad.find("z"))                #  busca     IZQ  a  Der  ;      rfind    DER  a Izq
print(ciudad[0:tstr].upper())          #  5:8:2
print(ciudad)
ciudad = ciudad[3:10].upper()    # lower   capitalize    title    split     islower      isupper
print(ciudad)                    # isalpha isalphanum    isdigit  isdecimal replace
                                 #


z = Counter("palabra")        #   cta veces c/caracter
print(z)
coches= "mercedes ferrari zbmw zbmw ferrari zbmw"
print( coches)
cochessp = coches.split(" ")      # CREA una estructura c/ que encuentre un espacio en el EJEMPLO)
print("     ", cochessp)
z= Counter(cochessp)
print("z ",z)

# Obtener el ( los )  más repetido
h = z.most_common(2)
print("h ", h)
print(h[0:1])


for ca in range(32,123):
    print( ca , chr(ca))
                                           #     A B    Z              a  b       z

txt = "LFMjdcwiFMONhuiuittYYYYggf"         #    65     90              97        122
lt = len(txt)                        #  se cambian las  MAYÚSCULAS por MINÚSCULAS
ntx = ""                             #   y   las minusculas  por
for i in range(lt):
        if ord(txt[i]) >= 65 and ord(txt[i]) <= 90 :
                                    ntx = ntx + chr(ord(txt[i]) + 32)
        else :
                 ntx = ntx + chr(ord(txt[i]) - 32)
print(txt,ntx)

txt = "LFMjdcwiFMONhuiuittYYYYggf"          # las 10  instrucciones   ANTERIORES
txt_chg = txt.swapcase()                    # las  reemplaza  el metódo   swapcase
print(txt, txt_chg)


def reversa(txtr):
    lt = len(txtr)                      # Crear una cadena que sea la opuesta a la recibida
    for k in range (lt-1,-1,-1):        #  si recibe "ana reconoce"
        txtrv= txtrv + txtr[k]          #  opuesta CREADA "econocer ana"
    return txtrv

nt = reversa("anitalavalatina")
print(nt)

cadena = "   hgkeu hioio   ffyyt  kkhh  geniabah   "
print (cadena.strip())         #lstrip     #  rstrip


def quitaespacios(txtr):                    # quitar los espacios (en este ejemplo) a un texto
    txtrse = txtr.replace(" ","")
    return txtrse
print(quitaespacios("ghh  uty  yyy iyu"))

cadena = "   hgkeu hioio   ffyyt  kkhh  geniabah   "
print(cadena)
print (cadena.strip())         #strip  quita espacios derecha y de la  izquierda del text
print (cadena.lstrip())        #lstrip quita espacios a la izquierda
print (cadena.rstrip())        #rstrip


    #    HACER UNA FUNCIÓN    QUE RECIBA  UN TEXTO   Y DETERMINE SI ES Ó NO UN PALINDROME
    #    palindrome :  texto que se lee lo mismo de IZQUIERDA a DERECHA   que de DERECHA  a IZQUIERDA
    #    palindrome = "Anita lava la tina"    "Dabale arroz a la zorra el ABAD"
    #                 "reconocer"     "ana"


   #   hacer   Función que reciba UNA CADENA y retorne una cadena ASI:
   #   cada caracter alfabetico lo cambie por el caracter alfabetico que SIGA en
   #   en el orden del ALFABETO.    EJEMPLO :   recibe "Hola"  retorna "Ipmb"
   #   Los caracteres que sean digitos los cambie así :
   #   0 : 9  , 1 : 8 ,  2 : 7 , 3 : 6 ; 4 : 5  ;  5 : 4 , 6 : 3 ;  7 : 2 , 8 : 1 ;  9 : 0
   #   los demas dejarlos  como estén.

   #   hacer   Función que reciba UNA CADENA y retorne una cadena ASI:
   #   cada caracter alfabetico lo cambie por el caracter alfabetico que le sigue en
   #   en el texto.    EJEMPLO :   recibe "Hola"  retorna "olaH"





inve













