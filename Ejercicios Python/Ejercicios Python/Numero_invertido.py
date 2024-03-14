numero= input("Ingrese un numero entero de tres digitos: " )
if len(numero) != 3:
   print("El numero ingresado no es valido, intentelo de nuevo")
else:
   digitos= list(numero)
   inversion= digitos[::-1]
   numerosinvertidos= int("".join(inversion))
print ("El digito con los numeros inversos es: ",{numerosinvertidos})