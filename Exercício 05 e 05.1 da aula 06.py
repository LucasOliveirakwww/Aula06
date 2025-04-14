#Receber primeira e segunda nota de um aluno, calcular e entregar (Válidos valores até 10, apenas)
resp = "s"
while resp == "s":
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Digite a segunda nota: " ))
    media = (nota1+nota2)/2
    print(f"Sua média é: {media}")
    resp = input("Você deseja repetiro cálculo? ")

