
#//////////////////////////////////////

#Funcion de palabra o frase polindrome

def PLPALINDROME(F):

	F = F.lower()
	F = F.replace("","")
	LGT = len(F)
	if LGT % 2 == 0:
		IZ = F[:LGT // 2 ]
		DR = F[LGT // 2:]
	else:
		IZ = F[:LGT // 2 ]
		DR = F[LGT // 2 + 1: ]

	return  IZ == DR[:: -1]   

	

print(PLPALINDROME("anitalavalatina"))



#/////////////////////////////////////////////77
# inverrir frase
def INVERTCAD (F):
	FIVT= "".join(reversed(F))
	return FIVT

print(INVERTCAD("Hola JUAN como te encuentras  xd "))




#/////////////////////////////////////////////////////////////



# caracteres ascii
def TRNSFACSSI(F):
	for X in F:
		ACSII = print("%s: %i" % (X, ord(X)))
	return ACSII


print(TRNSFACSSI("3dw4rd F4bi@n &oyene&he"))



