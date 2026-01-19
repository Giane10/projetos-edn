
'''Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.'''


def verificar_senha():
    print("\n---  Verificador de Segurança de Senha ---")
    
    while True:
        senha = input("\nDigite uma nova senha (ou 'sair'): ").strip()

        if senha.lower() == 'sair':
            print("Encerrando verificador...")
            break

        # Regra 1: Verificar o tamanho
        tamanho_valido = len(senha) >= 8

        # Regra 2: Verificar se contém pelo menos um número
        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break 

        # Validação Final
        if tamanho_valido and tem_numero:
            print(" Senha validada com sucesso!")
            break 
        else:
            print(" Senha inválida! A senha deve ter:")
            if not tamanho_valido:
                print("   - Pelo menos 8 caracteres")
            if not tem_numero:
                print("   - Pelo menos um número")
            print("Tente novamente.")


verificar_senha()