# Desafio
# Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

# Entrada
# Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

# Saída
# Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# Rodrigo
# (00) 90000-0000
# 10.00
# (33) 93333-3333
# 60
# Chamada para (33) 93333-3333 realizada com sucesso. Saldo: $4.00

# Yule
# (11) 91111-1111
# 30.00
# (00) 90000-0000
# 240	Chamada para (00) 90000-0000 realizada com sucesso. Saldo: $6.00

# Amelia
# (33) 93333-3333
# 10.00
# (11) 91111-1111
# 120
# Saldo insuficiente para fazer a chamada.




# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
    def custo_chamada(self, duracao_minutos):
        custo_por_minuto = 0.10
        return custo_por_minuto * duracao_minutos

    def deduzir_saldo(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False
        
# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao_minutos):
        custo = self.plano.custo_chamada(duracao_minutos)
        if self.plano.deduzir_saldo(custo):
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return f"Saldo insuficiente para fazer a chamada."

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Criando objeto de usuário pré-pago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

# Recebendo informações da chamada:
destinatario = input()
duracao = int(input())

# Realizando a chamada e exibindo o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))