                # Dimensionamento do sistema fotovoltaico

import math

# Informação da tarifa
tarifa = float(input("Informe a tarifa (R$/kWh): "))

# Consumo dos últimos 12 meses em kWh
consumos = []
for i in range(12):
    consumo = float(input(f"Informe o consumo do mês {i+1} (kWh): "))
    consumos.append(consumo)
media_consumo_mes = sum(consumos)/12
print(f"A média do consumo por mês é: {media_consumo_mes:.2f} kWh/mês.")

# Margem de segurança em percentual
margem_seguranca = float(input("Informe a margem de segurança (em %): "))

# Calculo da prodrução desejada
produçao = media_consumo_mes * (margem_seguranca / 100)
produçao_desejada = media_consumo_mes + produçao
print(f"A produção desejada é: {produçao_desejada:.2f} kWh/mês.")

# Radiação por dia
cidades = {
    'acorizal': 5.64, 
    'chapada dos guimaraes': 5.63,
    'cuiaba': 5.12,
    'jangada': 5.60,
    'nobres': 5.67,
    'nova brasilandia': 5.70,
    'pocone': 5.56,
    'rosario oeste': 5.62,
    'santo antonio': 5.60,
    'varzea grande': 5.61
}
cidade = input("Informe a cidade: ")
radiacao_dia = cidades[cidade]

# Percentual de perdas
perdas_percentual = float(input("Informe o percentual de perdas (em %): "))

# Potência do módulo em W
potencia_modulo = float(input("Informe a potência do módulo (em W): "))

# Fator de simultaneidade
fator_simultaneidade = float(input("Informe o fator de simultaneidade (em %): "))

# Cálculo da placa solar
numero_modulos = math.ceil((((produçao_desejada/30)/radiacao_dia)/(1 -(perdas_percentual/100))) / (potencia_modulo/1000))
potencial_total = potencia_modulo * numero_modulos
area_ocupada = numero_modulos * 2.6 # considerando uma área ocupada de 2,6 m² por módulo
geracao_estimada_mes = potencia_modulo * radiacao_dia * 30 * (1-(perdas_percentual / 100)) * (numero_modulos/1000)

# Resumo dos resultados
print(f"Potencial total do arranjo FV: {potencial_total:.2f} Wp")
print(f"Número de módulos: {(numero_modulos)}")
print(f"Área ocupada: {area_ocupada:.2f} m²")
print(f"Geração estimada por mês: {geracao_estimada_mes:.2f} kWh/mês")

                # Final do dimensionamento

