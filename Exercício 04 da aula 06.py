#Código para ler senha e após 3 tentativas sair informando que a senha está bloqueada
senha_correta= 12345
cont = 1
senha = int(input("Digite sua senha: " ))
while senha != senha_correta and cont < 3:
    senha = int(input("Digite sua senha: " ))
    cont = cont+1
if senha == 12345:
    print("Senha correta")
else:
    print("Senha bloqueada")
