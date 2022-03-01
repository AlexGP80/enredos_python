import random
import numpy as np

# def sumar(x, y):
#     return x + y
#
# def restar(x, y):
#     return x - y
#
# cu = "cu"
# lo = "lo"
# print(cu + lo)
output = ""
resultados = []
tirada = random.randint(1,100)

while tirada >= 50:
    resultados.append(tirada)
    tirada = random.randint(1,100)

resultados.append(tirada)

for resultado in resultados:
    if not output:
        output += f"{resultado} "
    else:
        output += f"+ {resultado} "

resultados = np.array(resultados)
output += f"= {resultados.sum()}"

print(output)
