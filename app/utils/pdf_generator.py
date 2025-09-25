import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def gerar_comprovante_bytes(consulta):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    # Estilos de texto
    styles = getSampleStyleSheet()
    estilo_titulo = styles["Title"]
    estilo_normal = styles["Normal"]

    elementos = []

    # Logo (se você tiver um arquivo logo.png na pasta)
    try:
        logo = Image("logo.png", width=80, height=80)  
        elementos.append(logo)
    except:
        pass  # Se não tiver logo, só ignora

    # Espaço
    elementos.append(Spacer(1, 20))

    # Título
    elementos.append(Paragraph("Comprovante de Consulta - Clínica Vida+", estilo_titulo))
    elementos.append(Spacer(1, 20))

    # Tabela com dados da consulta
    data = [
        ["Paciente:", consulta.patient_name],
        ["Médico:", consulta.doctor_name],
        ["Data/Hora:", str(consulta.start_datetime)],
        ["Preço:", f"R$ {consulta.price:.2f}"],
    ]

    tabela = Table(data, colWidths=[100, 350])
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (0, -1), "RIGHT"),
    ]))

    elementos.append(tabela)
    elementos.append(Spacer(1, 40))

    # Rodapé
    elementos.append(Paragraph("Clínica Vida+ - Sua saúde em primeiro lugar", estilo_normal))
    elementos.append(Paragraph("Telefone: (11) 99999-9999 | Endereço: Av. Saúde, 123 - São Paulo/SP", estilo_normal))

    # Gera PDF
    doc.build(elementos)
    buffer.seek(0)
    return buffer
