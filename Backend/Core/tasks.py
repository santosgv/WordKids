from celery import shared_task
from .models import Imagem
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os
from django.conf import settings
from PIL import Image
from django.http import FileResponse
from django.http import JsonResponse


@shared_task
def imprimir(request,id):
        try:
            image = Imagem.objects.get(id=id)
            buffer = io.BytesIO()
            PDF = canvas.Canvas(buffer, pagesize=letter)

            # Abre a imagem usando PIL
            img_path = os.path.join(settings.BASE_DIR, 'media', f'{image.arquivo}')
            img = Image.open(img_path)

            # Converte a imagem para preto e branco
            img = img.convert("L")

            # Obtém as dimensões da folha A4
            a4_width, a4_height = letter

            # Calcula as proporções para manter a escala
            width_ratio = a4_width / img.width
            height_ratio = a4_height / img.height
            min_ratio = min(width_ratio, height_ratio)

            # Calcula as novas dimensões da imagem mantendo a escala
            new_width = int(img.width * min_ratio)
            new_height = int(img.height * min_ratio)

            # Calcula as coordenadas para centralizar a imagem na folha
            x_offset = (a4_width - new_width) / 2
            y_offset = (a4_height - new_height) / 2

            # Desenha a imagem na folha A4 mantendo a escala
            PDF.drawInlineImage(img, x_offset, y_offset, width=new_width, height=new_height)
            PDF.drawString(120,2,'Visite https://mundocoloridokids.com.br para mais desenhos')

            PDF.showPage()
            PDF.save()

            buffer.seek(0)
            response = FileResponse(buffer, as_attachment=True, filename='Mundo Colorido Kids - Desenho.pdf')
            response.status_code = 200
            return response
        except Exception as msg:
            response = msg
            response.status_code = 404
            return JsonResponse({"error": str(msg)}, status=response.status_code)