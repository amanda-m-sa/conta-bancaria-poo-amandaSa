# Abstraindo Conta
class ContaBancaria:                          #identificador
    def __init__(self, titular):              #atributos
        self.titular = titular
        self.saldo = 0.0

    def exibir_saldo(self):                   #método 
        print(f"Nome do titular: {self.titular}. Saldo: {self.saldo}.")

#Criando objeto da classe contaBancaria
titular1 = ContaBancaria("Amanda")
titular2 = ContaBancaria("Raimundo")

#Exibição de saldo
titular1.exibir_saldo()
titular2.exibir_saldo() 

#Manipulação dos atributos
titular1.saldo = 22000
titular1.exibir_saldo()