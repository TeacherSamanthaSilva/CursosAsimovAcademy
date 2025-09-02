nomedeusuario = "Samantha"
senhausuario = "s086a984m41998"

usuario = str(input("Digite o seu nome de usuário "))
senha = str(input("Digite a sua senha ")) 

if(usuario != nomedeusuario and  senha != senhausuario):
    print("O nome de usuário ou senha está incorretos")
else:
    print("Usuário logado com sucesso")
