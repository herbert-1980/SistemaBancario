import textwrap

def menu ():
    menu = """\n
    ======================MENU======================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    =>  """  # Define um menu de opções que será exibido para o usuário

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:  # Verifica se o valor do depósito é positivo
        saldo += valor  # Adiciona o valor ao saldo
        extrato += f"Depósito:\tR${valor:.2f}\n"  # Registra a operação de depósito no extrato
        print("\n===== Depósito realizado com sucesso! =====")  # Confirma o depósito para o usuário
    else:
        print("\n=== Operação falhou! O valor informado é inválido. ===")  # Informa que o valor é inválido
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n === Operação falhou! Você não tem saldo suficiente. ===")  # Informa que o saldo é insuficiente
    elif excedeu_limite:
        print("\n === Operação falhou! O valor do saque excede o limite. ===")  # Informa que o saque excede o limite
    elif excedeu_saques:
        print("\n === Operação falhou! Número máximo de saques excedido. ===")  # Informa que o limite de saques diários foi excedido
    elif valor > 0:
        saldo -= valor  # Deduz o valor do saldo
        extrato += f"Saque:\t\tR${valor:.2f}\n"  # Registra a operação de saque no extrato
        numero_saques += 1  # Incrementa o contador de saques diários
        print("\n ===== Saque realizado com sucesso! =====")  # Confirma o saque para o usuário
    else:
        print("\n === Operação falhou! O valor informado é inválido. ===")  # Informa que o valor é inválido
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ========== EXTRATO ========== ")  # Imprime o título do extrato
    print("Não foram realizadas movimentações.")  # Informa que não há movimentações se o extrato estiver vazio
    print(f"Saldo atual: R${saldo:.2f}\n")  # Imprime o saldo atual formatado
    print(" =============================== ")  # Imprime todas as operações registradas no extrato
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n === Já existe usuário com esse CPF! ===")
        return
    nome =  input("Informe o nome Completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigle do estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) #adicionando ao dicionario
    print(" ==== Usuário criado com sucesso! ==== ")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n ==== Conta criada com Sucesso! ====")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario": usuario}
    print ("\n === Usuário não encontrado, fluxo de criação de conta encerrado! === ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Títular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    limite_saques = 3  # Define o limite máximo de saques diários
    agencia = "0001"
    
    saldo = 0  # Inicializa o saldo da conta com zero
    limite = 500  # Define o limite máximo de saque por transação
    extrato = ""  # Inicializa o extrato como uma string vazia para armazenar as operações
    numero_saques = 0  # Inicializa o contador de saques diários com zero
    usuarios = []
    contas = []

    while True:  # Inicia um loop infinito para executar o menu até que o usuário decida sair
        opcao = menu()  # Exibe o menu e captura a opção escolhida pelo usuário
        
        if opcao == "d":  # Se a opção for "d" (Depositar)
            valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":  # Se a opção for "s" (Sacar)
            valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )
            
        elif opcao == "e":  # Se a opção for "e" (Extrato)
            exibir_extrato (saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao =="nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
                
        elif opcao == "q":
            break
            
        else:
            print("Operação inválida, por favor selecione novamente a opção desejada. ")
                   
                   
main()
