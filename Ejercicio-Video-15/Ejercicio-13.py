#   Operadores Logicos

#   AND

distancia = 400
numeroHermanos = 3
salariosPadres = 3000
tieneBeneficio = False
if (distancia > 1000 and numeroHermanos > 2) or salariosPadres < 2000:
    tieneBeneficio = True

print(not tieneBeneficio)
#   OR
#   NOT

if (5 > 3) and (8 < 6):
    print("Verdad")
else:
    print("Es mentira...")


if (5 > 3) or (8 < 6):
    print("Verdad")
else:
    print("Es mentira...")
