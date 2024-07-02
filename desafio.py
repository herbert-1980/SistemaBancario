menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do Depósito: "))
        
        if valor > 0: # Evita os valores negativos
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n" # Formata os valores
            print("Depósito")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite diário.")
            
        elif excedeu_saques:
            print("Operação Falhou! Número de saques excedeu.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1 # incrementar o numero de saques
            
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "e":
        
        print("\n ==================== EXTRATO ====================\n")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
            
        print("\n====================================================\n")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
