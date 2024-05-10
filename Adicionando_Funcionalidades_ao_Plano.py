# Desafio
# Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

# Condições da verificação do saldo:
# - Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
# - Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
# - Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Entrada
# Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

# Saída
# Mensagem personalizada de acordo o saldo do cliente.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# João     
# Essencial      
# 9

# Seu saldo está baixo. Recarregue e use os serviços do seu plano.

# Debora
# Prata
# 11
#  	Seu saldo está razoável. Aproveite o uso moderado do seu plano.
# Catarina
# Premium
# 50

# Parabéns! Continue aproveitando seu plano sem preocupações.


# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo

# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:  
    def verificar_saldo(self):
        return self._saldo

# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 
    def mensagem_personalizada(self):
        if self._saldo < 10:
            return f"Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self._saldo >= 50:
            return f"Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return f"Seu saldo está razoável. Aproveite o uso moderado do seu plano."

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def verificar_saldo(self):
        saldo = self.plano.verificar_saldo()
        if saldo < 10:
            mensagem = f"Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            mensagem = f"Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            mensagem = f"Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        return saldo, mensagem

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)