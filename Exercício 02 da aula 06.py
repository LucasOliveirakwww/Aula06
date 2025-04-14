#Receber a quantidade de alunos, notas e tirar a média da turma
quant = int(input("Quantos alunos tem na sala: " ))
i = 1
soma=0
while i <= quant:
    nota = float(input("Digite um número: "))
    soma+=nota
    i+=1
media = soma/quant
print(media)
