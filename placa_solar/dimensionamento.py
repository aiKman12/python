import math
from proposta import GERAR_PROPOSTA
from constants.cidades import CIDADE_INCIDENCIA

def receber_dados_proprietario():
    nome = input("Informe o nome do proprietário: ")
    endereco = input("Informe o endereço: ")
    cpf = format_cpf(input("Informe o CPF: "))
    telefone = input("Informe o número do Telefone com o DDD: ")

    return {"nome": nome, "endereco": endereco, "cpf": cpf, "telefone": telefone}

def format_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def receber_lista(texto, total):
    return [float(input(f"{texto} {i+1}: ")) for i in range(total)]

def calcular_consumo_media(consumos):
    return sum(consumos) / len(consumos)

def calcular_producao_desejada(consumo_media, margem_seguranca):
    return consumo_media * (1 + margem_seguranca / 100)

def determinar_numero_modulos(producao_desejada, radiacao_dia, perdas_percentual, potencia_modulo):
    return math.ceil((((producao_desejada / 30) / radiacao_dia) / (1 - (perdas_percentual / 100))) / (potencia_modulo / 1000))

def dimensionar_sistema():
    proprietario = receber_dados_proprietario()
    tarifa = float(input("Informe a tarifa (R$/kWh): "))
    consumos = [float(input(f"Informe o consumo do mês {i+1} (kWh): ")) for i in range(12)]

    media_consumo_mes = calcular_consumo_media(consumos)
    margem_seguranca = float(input("Informe a margem de segurança (em %): "))
    cidade = input("Informe a cidade: ").lower()
    radiacao_dia = CIDADE_INCIDENCIA[cidade]
    perdas_percentual = float(input("Informe o percentual de perdas (em %): "))
    potencia_modulo = float(input("Informe a potência do módulo (em W): "))
    fator_simultaneidade = float(input("Informe o fator de simultaneidade (em %): "))
    producao_desejada = calcular_producao_desejada(media_consumo_mes, margem_seguranca)

    numero_modulos = determinar_numero_modulos(producao_desejada, radiacao_dia, perdas_percentual, potencia_modulo)
    potencial_total = potencia_modulo * numero_modulos
    area_ocupada = numero_modulos * 2.6
    geracao_estimada_mes = potencia_modulo * radiacao_dia * 30 * (1 - (perdas_percentual / 100)) * (numero_modulos / 1000)

    GERAR_PROPOSTA(proprietario, potencial_total, numero_modulos, area_ocupada, geracao_estimada_mes)
    print("Proposta gerada com sucesso.")

if __name__ == "__main__":
    dimensionar_sistema()