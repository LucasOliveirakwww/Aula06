#Receber 10 notas e tirar a média usando while
n = 10
soma = 0
i = 1
while i <= 10:
    num = float(input("Digite um número: "))
    soma += num
    i+=1
media = soma/10
print(media)