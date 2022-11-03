import io
from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def informeGen(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)

    textob = p.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines = [
        "This is line 1",
        "This is line 2",
        "This is line 3",
    ]

    for line in lines:
        textob.textLine(line)

    p.drawText(textob)

    p.showPage()
    p.save()

    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def informe(request):
    return render(request, "informeEstadistica/informes.html")

