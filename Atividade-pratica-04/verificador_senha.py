
'''Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.'''


def verificar_senha():
    senha = input("Digite sua senha: ")

    if len(senha) < 8:
        print("Por favor digite acima de 8(oito) caracteres. ")

verificar_senha()