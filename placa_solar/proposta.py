from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

import os

current_path = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_path, "logo_empresa.png")

def GERAR_PROPOSTA(proprietario, potencial_total, numero_modulos, area_ocupada, geracao_estimada_mes):
    styles = getSampleStyleSheet()
    styleN = styles['Heading1']
    styleN.alignment = TA_CENTER
    styleB = styles['BodyText']
    styleB.alignment = TA_JUSTIFY

    # Informações da empresa
    empresa = {"nome": "DOMÍNIO SOLAR",
               "endereco": "Rua 2, Resisencial JK",
               "telefone": "(65) 9 9960-4463",
               "email": "iuri_abdon@hotmail.com"
               }

    # Criação do PDF
    nome_arquivo = f"{proprietario['nome'].split()[0]}.pdf"
    pdf = SimpleDocTemplate(nome_arquivo, pagesize=A4)

    # Adicionar cabeçalho da proposta
    cabecalho = Paragraph("PROPOSTA DE SISTEMA FOTOVOLTAICO", styleN)

    # Informações da empresa
    empresa_info = Paragraph(f"{empresa['nome']}<br />"
                             f"{empresa['endereco']}<br />"
                             f"{empresa['telefone']}<br />"
                             f"{empresa['email']}",
                             styles["BodyText"])

    # Introdução
    introducao = Paragraph("Prezado(a),<br /><br />"
                           "Agradecemos o seu interesse em nosso sistema fotovoltaico. Estamos felizes em apresentar a nossa proposta personalizada para atender às suas necessidades de geração de energia limpa e sustentável. Por favor, encontre abaixo os detalhes importantes do sistema proposto.",
                           styleB)

    # Dados do cliente
    dados_cliente = Paragraph("<b>Dados do Cliente</b>", styles["BodyText"])
    data = [
        ["Nome:", f"{proprietario['nome']}"],
        ["CPF:", f"{proprietario['cpf']}"],
        ["Endereço:", f"{proprietario['endereco']}"]
    ]
    cliente_table = Table(data, colWidths=(100, 350))

    # Dados do sistema proposto
    dados_sistema = Paragraph("<b>Dados do Sistema Fotovoltaico Proposto</b>", styles["BodyText"])
    data = [
        ["Potência total do arranjo FV:", f"{potencial_total:.2f} Wp"],
        ["Número de módulos:", f"{numero_modulos}"],
        ["Área ocupada:", f"{area_ocupada:.2f} m²"],
        ["Geração estimada por mês:", f"{geracao_estimada_mes:.2f} kWh/mês"]
    ]
    sistema_table = Table(data, colWidths=(230, 220))

    # Conclusão
    conclusao = Paragraph("Este sistema foi projetado para maximizar o aproveitamento da luz solar e a geração de energia elétrica, levando em consideração a sua localização, consumo médio mensal e necessidades específicas. Nosso objetivo é fornecer uma solução rentável e ambientalmente responsável para sua propriedade.<br /><br />"
                          "Caso tenha alguma dúvida ou precise de informações adicionais, por favor, entre em contato conosco. Ficaremos felizes em ajudar.<br /><br />"
                          "Atenciosamente,<br />"
                          f"{empresa['nome']}",
                          styleB)

    # Adiciona a data no final da proposta
    now = datetime.now()
    data_atual = now.strftime("%d/%m/%Y")
    data_proposta = Paragraph(f"<b>Data:</b> {data_atual}", styles["BodyText"])
    data_proposta.alignment = TA_RIGHT

    # Agrupar os elementos da proposta em uma lista
    story = []
    story.append(Spacer(1, 20))
    story.append(cabecalho)
    story.append(Spacer(1, 20))
    story.append(empresa_info)
    story.append(Spacer(1, 20))
    story.append(introducao)
    story.append(Spacer(1, 20))
    story.append(dados_cliente)
    story.append(Spacer(1, 5))
    story.append(cliente_table)
    story.append(Spacer(1, 20))
    story.append(dados_sistema)
    story.append(Spacer(1, 5))
    story.append(sistema_table)
    story.append(Spacer(1, 20))
    story.append(conclusao)
    story.append(Spacer(1, 20))
    story.append(data_proposta)

    # Adicionar a proposta e construir o PDF
    pdf.build(story)

    print(f"PDF gerado: {nome_arquivo}")