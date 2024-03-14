nota1 =  int(input("Ingrese la nota del primer certamen: "))
nota2 = int(input("Ingrese la nota del segundo certamen: "))
nota_lab = int(input("Ingrese la nota de Laboratorio: "))

promedio = (nota1 + nota2) / 2

nota_objetivo = (60-(promedio*0.7 + nota_lab*0.3))/0.7

print(f"La nota necesaria es: {nota_objetivo}")