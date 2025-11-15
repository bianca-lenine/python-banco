
def main():

    # #
    # Python Banco Menu 
    # 1. Criar uma conta
    # 2. Consultar saldo
    # 3. Deposito
    # 4. Saque
    # 5. Sair
    # #

    cadastro_contas = CadastroConta()
    
    nome = input('Informe seu nome: ')
    print('Bem vindo ao Python Banco ' + nome) 
   
   numero_conta = input ('Informe o número da conta: ')
   
   conta= cadastro_contas.cadastrar(nome, numero_conta)

    """
    TODO: 
    - Enriquecer o Onboarding do Cliente (cadastro) via etapas com validações basicas
    - Separar o cadastro de uma conta em uma classe separada
    - Salvar o cadastro do usuário para futuras sessoes (arquivo JSON em uma pasta chamada `data`)
    - Chamar LLM para dar dicas personalizadas para o cliente com base nos dados dele
    """
def cadastro(nome, conta):

main()
 