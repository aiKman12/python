# Criando uma lista para armazenar os empréstimos
emprestimos = []

# Definindo uma classe para representar um empréstimo
class Emprestimo:
    def __init__(self, valor, juros, data_vencimento):
        self.valor = valor
        self.juros = juros
        self.data_vencimento = data_vencimento
        self.pagamentos = []

    def adicionar_pagamento(self, valor_pago, data_pagamento):
        self.pagamentos.append((valor_pago, data_pagamento))

    def saldo_devedor(self):
        saldo = self.valor
        for valor_pago, data_pagamento in self.pagamentos:
            saldo -= valor_pago
        return saldo + (saldo * self.juros)

# Função para registrar um novo empréstimo
def registrar_emprestimo():
    valor = float(input("Digite o valor do empréstimo: "))
    juros = float(input("Digite a taxa de juros (em decimal): "))
    data_vencimento = input("Digite a data de vencimento (no formato dd/mm/aaaa): ")
    emprestimo = Emprestimo(valor, juros, data_vencimento)
    emprestimos.append(emprestimo)
    print("Empréstimo registrado com sucesso.")

# Função para registrar um pagamento
def registrar_pagamento():
    if not emprestimos:
        print("Não há empréstimos registrados.")
        return
    print("Selecione o empréstimo:")
    for i, emprestimo in enumerate(emprestimos):
        print(f"{i + 1}. Valor: R${emprestimo.valor:.2f} - Data de vencimento: {emprestimo.data_vencimento}")
    escolha = int(input("Digite o número correspondente: "))
    emprestimo = emprestimos[escolha - 1]
    valor_pago = float(input("Digite o valor pago: "))
    data_pagamento = input("Digite a data do pagamento (no formato dd/mm/aaaa): ")
    emprestimo.adicionar_pagamento(valor_pago, data_pagamento)
    print("Pagamento registrado com sucesso.")

# Função para exibir o saldo devedor
def exibir_saldo():
    if not emprestimos:
        print("Não há empréstimos registrados.")
        return
    for i, emprestimo in enumerate(emprestimos):
        saldo = emprestimo.saldo_devedor()
        print(f"{i + 1}. Valor: R${emprestimo.valor:.2f} - Saldo devedor: R${saldo:.2f}")

# Menu principal
while True:
    print("\nGerenciamento de Empréstimos\n")
    print("1. Registrar um novo empréstimo")
    print("2. Registrar um pagamento")
    print("3. Exibir saldo devedor")
    print("4. Sair")
    escolha = int(input("Digite o número correspondente: "))
    if escolha == 1:
        registrar_emprestimo()
    elif escolha == 2:
        registrar_pagamento()
    elif escolha == 3:
        exibir_saldo()
    elif escolha == 4:
        break
    else:
        print("Opção inválida.")
