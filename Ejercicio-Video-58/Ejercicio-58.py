#   Lista de comprension
import math

# numeros = [1, 4, 9, 16, 25]
# raices = [int(math.sqrt(x)) for x in numeros]

# raices = []
# for n in numeros:
#     raices.append(int(math.sqrt(n)))

# print(raices)

# numeros = [1, 4, 9, 16, 25]
# v = [x if (x > 10) else "*" for x in numeros]
# print(v)

# l = [c.upper() for c in "Peperoni"]
# print(l)

a = [l if l in "aeiou" else "*" for l in "murcielago"]
print(a)
