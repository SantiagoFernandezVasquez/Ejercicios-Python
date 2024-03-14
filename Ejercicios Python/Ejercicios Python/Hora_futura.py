hora = int(input("Ingrese la hora actual(Del 1 al 24): "))
adelantar = int(input("Ingrese el numero de horas que quiere avanzar(Del 1 al 24): "))

hora_nueva = (hora + adelantar) % 24

print(f"Despues de {hora}, el relog marcara las {hora_nueva}:00 horas")