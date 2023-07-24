saldo = 0
limite = 1000.00
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

cliente = input(
    '''
    Seja bem-vindo ao DinDin Digital Bank
    Para começarmos o atendimento, digite seu nome:  
    '''
    )

print(
    f"""
      Olá, {cliente}.
      Já localizei seus dados.
      """
      )
    
while True:

    operacao = int(input(
    '''
    Vou te passar o nosso menu de serviços
    [1] Saque
    [2] Depósito
    [3] Extrato
    [4] Sair
    Digite o número da opção desejada:  '''
    ))
    if operacao == 1:
       if numero_saque < LIMITE_SAQUE:  
            valor_saque =  float(input(
                f'''
                \n{cliente}, informe o valor que deseja sacar: R$  '''
                ))
            
            if valor_saque <= saldo:
                saldo -= valor_saque
                numero_saque += 1
                extrato += f"Saque                 R$ {valor_saque:.2f}\n"
                    
                print(
                        f'''
                        Saque efetuado com sucesso! 
                        Seu saldo é de R$ {saldo:.2f}.
                        ''')    
            elif valor_saque > saldo and valor_saque <= limite:
                    limite = limite - valor_saque + saldo
                    saldo = 0 
                    numero_saque += 1
                    extrato += f"Saque                 R$ {valor_saque:.2f}\n"
                    print(
                        f'''
                        Saque efetuado com sucesso! 
                        Você entrou no cheque especial
                        Seu limite é de R$ {limite:.2f}.
                        ''')
            else:
                limite -= valor_saque + saldo
                print("Saldo insuficiente.")

       else:
            print("Limite de saque excedido.")
    
        
    elif operacao == 2:
        valor_deposito = float(input(
        f'''
        \n{cliente}, informe o valor que deseja depositar: R$  '''
        ))
        if limite < 1000:
            limite += valor_deposito
            if limite > 1000:
                saldo += limite - 1000
                limite = 1000
            extrato += f"Depósito:             R$ {valor_deposito:.2f}\n"
        else:
            saldo += valor_deposito
            extrato += f"Depósito:             R$ {valor_deposito:.2f}\n"
                 
        print(
            f'''
            Depósito efetuado com sucesso! 
            Seu saldo é de R$ {saldo:.2f}.
            Seu limite do cheque especial é de R$ {limite:.2f}.
            ''')
        
    elif operacao == 3:
        print(f"\n{cliente}, segue seu extrato...")
        print("\n*********** EXTRATO **********")                                  
        print("Não foram realizadas movimentações." if not extrato else extrato)   
        print(f'''
        Saldo                 R$ {saldo:.2f}
        Limite                R$ {limite:.2f}
        Nº saques realizados  {numero_saque}
        ''')                                          
        print("******************************")                                   

        
    elif operacao == 4:
        confirmar = int(input(
        f'''
        \n{cliente}, tem certeza que deseja sair?
        [1] Sim
        [2] Não
        Digite a opção desejada:   '''
        ))
        
        if confirmar == 1:
            print(
            f'''
            {cliente}, obrigada por acessar nosso sistema.
            Conte sempre com o DinDin Digital Bank.
            Volte sempre!!!
            '''
            )
            break
        elif confirmar == 2:
             print(f"\n{cliente}, você resolveu ficar mais um pouquinho. Show!")
                      
    else:
        print(input(
        f'''
        \n{cliente}, você digitou uma opção inválida.
        Mas não se preocupe...
       
        Vou te passar o nosso menu de serviços
        [1] Saque
        [2] Depósito
        [3] Extrato
        [4] Sair
        Digite o número da opção desejada:  '''
        ))