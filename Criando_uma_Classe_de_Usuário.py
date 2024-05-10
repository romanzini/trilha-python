# Desafio
# Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

# Entrada
# Nome do usuário, número de telefone e plano.

# Saída
# Mensagem indicando que o usuário foi criado com sucesso.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# Ana
# (11) 91111-1111
# Plano Essencial Fibra

# Usuário Ana criado com sucesso.

# Sofia
# (22) 92222-2222
# Plano Prata Fibra	Usuário Sofia criado com sucesso.
# Pedro
# (33) 93333-3333
# Plano Premium Fibra

# Usuário Pedro criado com sucesso.


# TODO: Crie uma classe UsuarioTelefone.  
class UsuarioTelefone:
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    def nome(self, nome):
        self._nome = nome

    def numero(self, numero):
        self._numero = numero

    def plano(self, plano):
        self._plano = plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
plano_1 = "Plano Essencial Fibra"
plano_2 = "Plano Prata Fibra"
plano_3 = "Plano Premium Fibra"

if (plano == plano_1) or (plano == plano_2) or (plano == plano_3):
    usuario = UsuarioTelefone(nome, numero, plano)
    print(usuario)
else:
    print(f"Plano {plano} não pode ser informado.")