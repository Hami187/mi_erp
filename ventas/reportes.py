from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from django.http import HttpResponse
from .models import Venta


def generar_pdf_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    detalles = venta.detalles.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="venta_{venta.numero}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elementos = []
    styles = getSampleStyleSheet()

    # TITULO
    titulo = Paragraph(f'<b>FACTURA DE VENTA</b>', styles['Title'])
    elementos.append(titulo)
    elementos.append(Spacer(1, 0.2 * inch))

    # INFO EMPRESA
    empresa = Paragraph('<b>MI ERP</b> - Sistema de Gestión Empresarial', styles['Normal'])
    elementos.append(empresa)
    elementos.append(Spacer(1, 0.2 * inch))

    # INFO VENTA
    info_data = [
        ['Número:', venta.numero],
        ['Cliente:', str(venta.cliente)],
        ['Fecha:', str(venta.fecha.strftime('%d/%m/%Y'))],
        ['Estado:', venta.estado.upper()],
    ]

    info_table = Table(info_data, colWidths=[2 * inch, 4 * inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#003366')),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    elementos.append(info_table)
    elementos.append(Spacer(1, 0.3 * inch))

    # TABLA DETALLES
    detalle_data = [['Producto', 'Cantidad', 'Precio Unitario', 'Subtotal']]

    for detalle in detalles:
        detalle_data.append([
            str(detalle.producto),
            str(detalle.cantidad),
            f'$ {detalle.precio_unitario}',
            f'$ {detalle.subtotal}',
        ])

    detalle_data.append(['', '', 'TOTAL:', f'$ {venta.total}'])

    detalle_table = Table(detalle_data, colWidths=[3 * inch, 1 * inch, 1.5 * inch, 1.5 * inch])
    detalle_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f0f4ff')]),
        ('GRID', (0, 0), (-1, -2), 0.5, colors.HexColor('#cccccc')),
        ('FONTNAME', (2, -1), (-1, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (2, -1), (-1, -1), colors.HexColor('#003366')),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elementos.append(detalle_table)
    elementos.append(Spacer(1, 0.3 * inch))

    # PIE
    pie = Paragraph('Gracias por su preferencia.', styles['Normal'])
    elementos.append(pie)

    doc.build(elementos)
    return response