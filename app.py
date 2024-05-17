import os


def cadastro():
    nome = input("Digite seu nome: \n")
    idade = input("Digite sua idade: \n")
    profissao = input("Qual a sua profissão atual ? \n")
    print(f"Você cadastrou o usuário {nome}, o qual possui {
          idade} anos de idade e atua como {profissao}.")


def resposta(text):
    if (text.lower() == "sair"):
        print("Saindo da aplicação.")
    elif (text.lower() == "sim"):
        cadastro()


resposta(input("Se você deseja cadastrar um novo usuário digite sim, caso deseje sair da aplicação digite sair.\n"))
