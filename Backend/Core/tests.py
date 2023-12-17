from django.test import TestCase
from django.test.client import Client
from django.http import FileResponse
from Core.models import Imagem, Categoria
from django.core.files.uploadedfile import SimpleUploadedFile

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.categoria_1 = Categoria.objects.create(nome='Categoria 1')
        imagem_file = SimpleUploadedFile("home-bg.png", b"file_content", content_type="image/png")
        self.desenho_1 = Imagem.objects.create(nome='desenho 1',categoria=self.categoria_1,arquivo=imagem_file,descricao='desscricao')

    def test_status_code_200(self):
        response = self.client.get(f"http://localhost:8000/api/imagens/")
        self.assertEqual(response.status_code,200)

    def teste_status_code_categoria_get(self):
        response = self.client.get(f"http://localhost:8000/api/categorias/{self.categoria_1.pk}/")
        self.assertEqual(response.status_code,200)

    def teste_status_code_categoria_404(self):
        response = self.client.get(f"http://localhost:8000/api/categorias/4/")
        self.assertEqual(response.status_code,404)
    
    def teste_status_code_desenho_get(self):
        response = self.client.get(f"http://localhost:8000/api/imagens/{self.desenho_1.pk}/")
        self.assertEqual(response.status_code,200)

    def teste_status_code_desenho_404(self):
        response = self.client.get(f"http://localhost:8000/api/imagens/600/")
        self.assertEqual(response.status_code,404)

    def test_status_code_200_imprimir(self):
        response = self.client.get(f"http://localhost:8000/imprimir/{self.desenho_1.pk}")
        self.assertEqual(response.status_code, 200)

    def test_status_code_404_imprimir(self):
        response = self.client.get(f"http://localhost:8000/imprimir/6")
        self.assertEqual(response.status_code,404)

    def tearDown(self):
        self.desenho_1.arquivo.delete()