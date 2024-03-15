import math

M = 67
p = 1.038 
c = 3.7  
K = 5.4e-3  
Tw = 100  
Ty = 70

temp_original = float(input("Ingrese la temperatura original del huevo en grados Celsius: "))



tiempo = t = (M*(2/3) * c * p(1/3)) / (K * math.pi2 * (4 * math.pi / 3)*(2/3) * math.log(0.76 * (temp_original - Tw) / (Ty - Tw)))
print("El tiempo en segundos que le toma al centro de la yema alcanzar la temperatura máxima es:", tiempo,"segundos")