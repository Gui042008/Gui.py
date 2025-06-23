class Conta:
# método construtor
    def __init__(self, agencia, numero, titular, saldo, senha):
        # criando os atributos da classe
        # atributo privado usa 2 underlines "_"
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha
   
    @property
    def numero(self):
        return self.__numero

    def extrato(self):
        return self.__saldo

    def saque(self, valor):
        if self.__saldo >= valor and valor > 0:
            self.__saldo -= valor
            return True
        else:
            return False

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        else:
            return False
       
    def pix(self, valor, conta):
        self.saque(valor)
        conta.deposito(valor)
