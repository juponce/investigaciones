import io
from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from denuncias.models import *

# Create your views here.

def informeGen(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)

    textob = p.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line 3",
    # ]

    denuncias = Denuncia.objects.all()

    lines = []

    for denuncia in denuncias:
        lines.append('Número denuncia: ' + str(denuncia.id_denuncia))
        lines.append('Fecha realizada la denuncia: ' + str(denuncia.fecha_creacion))
        lines.append('Motivo denuncia: ' + denuncia.situacion)
        lines.append('Fecha de ocurrido el incidente: ' + str(denuncia.fecha_delito))
        lines.append('Ubicación del incidente ' + denuncia.direccion)
        lines.append('Descripción sospechoso (si hay) ' + denuncia.descrpción_sospechoso)
        lines.append('Nombre denunciante ' + denuncia.nombre_denunciante + ' ' +denuncia.apellido_denunciante)
        lines.append('RUT denunciante ' + denuncia.rut_denunciante)
        lines.append('')

    for line in lines:
        textob.textLine(line)

    p.drawText(textob)

    p.showPage()
    p.save()

    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def informe(request):
    return render(request, "informeEstadistica/informes.html")

