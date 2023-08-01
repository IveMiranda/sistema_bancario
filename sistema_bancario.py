import textwrap                                          
def menu():
    menu = '''\n
    Vou te passar o nosso menu de serviços:\n
    ========== MENU ==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair\n
    Digite a opção desejada:  
    => '''
    
    return input(textwrap.dedent(menu))               

def depositar(saldo, limite, valor_deposito, extrato,  /):                # Uma regra de negócio é que a função depósito deve receber os argumentos apenas por posição (position only). Assim, acrescenta-se / depois dos argumentos.
    if limite < 1000:
        limite += valor_deposito
        if limite > 1000:
            saldo += limite - 1000
            limite = 1000
        extrato += f"Depósito:             R$ {valor_deposito:.2f}\n"

        print(
        f'''
        Depósito efetuado com sucesso! 
        Seu saldo é de R$ {saldo:.2f}.
        Seu limite do cheque especial é de R$ {limite:.2f}.
        ''')  
    elif limite == 1000 or limite > 1000:
        saldo += valor_deposito
        extrato += f"Depósito:             R$ {valor_deposito:.2f}\n"
                 
        print(
            f'''
            Depósito efetuado com sucesso! 
            Seu saldo é de R$ {saldo:.2f}.
            Seu limite do cheque especial é de R$ {limite:.2f}.
            ''')    
    else:
        print("\n@@@ Operação falou! O valor informado é inválido. @@@")

    return saldo, limite, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saque): # Uma regra de negócio é que a função saque deve receber os argumentos apenas por nome (keywork only). Assim, acrescenta-se * antes dos argumentos.

    if numero_saques < limite_saque:  
            
            if valor_saque <= saldo:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque                 R$ {valor_saque:.2f}\n"
                    
                print(
                        f'''
                        Saque efetuado com sucesso! 
                        Seu saldo é de R$ {saldo:.2f}.
                        ''')    
            elif valor_saque > saldo and valor_saque <= limite:
                    limite = limite - valor_saque + saldo
                    saldo = 0 
                    numero_saques += 1
                    extrato += f"Saque                 R$ {valor_saque:.2f}\n"
                    print(
                        f'''
                        Saque efetuado com sucesso! 
                        Você entrou no cheque especial.
                        Seu limite é de R$ {limite:.2f}.
                        ''')
            else:
                limite -= valor_saque + saldo
                print("@@@ Saldo insuficiente. @@@")

    else:
            print("@@@ Limite de saque excedido. @@@")

    return saldo, limite, numero_saques, extrato

def exibir_extrato(saldo, limite, numero_saques, /, *,extrato):                # Uma regra de negócio é que a função extrato deve receber os argumentos por posição (positional only: saldo) e por nome (keywork only: extrato). Assim, acrescenta-se / depois do argumento saldo e acrescenta-se * antes do argumento extrato.
    print(f"\n{cliente}, segue seu extrato...")
    print("\n**************** EXTRATO ****************")                                  
    print("\nNão foram realizadas movimentações." if not extrato else extrato)   
    print(f'''\n
        Saldo                 R$ {saldo:.2f}
        Limite                R$ {limite:.2f}
        Nº saques realizados  {numero_saques}
        ''')                                          
    print("\n*****************************************")    

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("\nInforme seu nome completo: ")
    data_nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme o endereço (logadouro, nro - bairro - cidade/sigla estado): ")

    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}

    print("\n*** Usuário criado com sucesso! ***")

def filtrar_usuario(cpf, usuarios):
    
    return usuarios.get(cpf)


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n*** Conta criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
       
    print("\n@@@ Usuário não encontrado, fluxo de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
                Agência: \t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
        """
        print("*" * 50)
        print(textwrap.dedent(linha))
        print("*" * 50)

        

if __name__ == "__main__":
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    usuarios = dict()
    contas = []

    cliente = input(
    '''
    Seja bem-vindo ao DinDin Digital Bank
    Para começarmos o atendimento, digite seu nome:  
    => '''
    )

    print(
        f"""
        Olá, {cliente}.
        Já localizei seus dados.
        """
        )

    while True:
        opcao = menu()

        if opcao == 'd':
            valor_deposito = float(input(f"\n{cliente}, informe o valor do depósito: "))

            saldo, limite, extrato = depositar(saldo, limite, valor_deposito,  extrato)
        
        elif opcao == 's':
            valor_saque = float(input(f"\n{cliente}, informe o valor do saque: "))

            saldo, limite, numero_saques, extrato = sacar(
                saldo = saldo, 
                valor_saque = valor_saque, 
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saque = LIMITE_SAQUES
            )
        elif opcao == 'e':
            exibir_extrato(saldo, limite, numero_saques, extrato = extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)
            
        elif opcao == 'q': 
            print(
            f'''
            {cliente}, obrigada por acessar nosso sistema.
            Conte sempre com o DinDin Digital Bank.
            Volte sempre!!!
            '''
            )
            break

        else:
            print("Operação inválida. Por favor, selecione novamente a opção desejada.")
            
