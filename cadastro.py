class CadastroConta:
    
    @staticmethod
    def cadastrar(nome, numero_conta): # Dois pontos para declarar o escopo da funçao
        conta = { # Analisar o escopo de funcao da variavel conta
            'nome': nome,
            'numero_conta': numero_conta,
            'saldo': 0.0
        }
        return conta