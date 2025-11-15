class CadastroConta:
    
    def __init__(self):
        self.contas_cadastradas = [] # Se o programa inicialmente vai ser runtime, porque armazenar as contas cadastradas?
    
    def cadastrar (self, nome, numero_conta) # Dois pontos para declarar o escopo da funçao
        conta = { # Analisar o escopo de funcao da variavel conta
            'nome': nome
            'numero_conta': numero_conta,
            'saldo': 0.0
        }