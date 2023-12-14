def main():
    Faker.seed(0)
    fake = Faker()
    for _ in range(3):
        categorias = Categoria.objects.create(
            nome=fake.name()
        )
        print(f'Categoria criada {categorias.nome}')


    for _ in range(50):
        desenho = Imagem.objects.create(
            nome=fake.name(),
            categoria=Categoria.objects.get(id=1),
            arquivo="http://localhost:8000/media/Imagens/home-bg.png",
            descricao=fake.sentence(nb_words=15),
            afiliado=fake.sentence(nb_words=50),
        )
        print(f'Desenho criado {desenho.id}')

if __name__ == '__main__':
    import os
    import random
    from django.core.wsgi import get_wsgi_application
 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Word.settings')
    application = get_wsgi_application()
    from Core.models import Categoria, Imagem
    from faker import Faker
    import random

    main()