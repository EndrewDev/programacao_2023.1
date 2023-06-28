from datetime import datetime

class Contabancaira:
    def __init__(self, titula, agencia, numero):
        """Conta Bancária"""

        self.titula = titula
        self.agencia = agencia
        self.numero = numero
        self.deposita = 0.0
        self.valor = []

    def depositar(self, valor):
        """Depositar"""

        self.valor = valor
        if self.valor > self.deposita:
            self.deposita += self.valor
        
    def sacar(self, valor):
        """SACAR"""

        self.valor = valor
        if self.valor <= self.deposita:
            self.valor -= self.deposita
        else:
            if self.valor > self.deposita:
                except AttributeError:

