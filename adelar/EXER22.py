negativos = 0
for num in range(5):
    num = int(input("Número:"))
    if num < 0:
        negativos = negativos + 1
print("Os negativos são:",negativos)