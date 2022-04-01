total_tinta = float(input("Quantidade de tinta em ml da caneta:"))
qnt_tinta = total_tinta * 0.20
while (total_tinta != 0):
    print("Enquanto tem tinta a caneta escreve...")
    str(input("Escreva:"))
    total_tinta = total_tinta - qnt_tinta
if total_tinta == 0:
    print("Acabou a tinta...")