#Fazer código para ler 2 valores, fazer divisão do 1º pelo 2º e caso o segundo for 0, solicitar novamente informando que só aceitamos valores diferentes de 0
t=3
quant1 = int(input("Digite um valor: " ))
quant2 = int(input("Digite um valor: "))
while quant2 == 0:
    quant2 = int(input("Digite um valor(0 = inválido): "))
divis = quant1 / quant2
print(divis)


