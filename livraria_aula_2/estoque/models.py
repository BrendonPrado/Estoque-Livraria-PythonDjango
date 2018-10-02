from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField("Idade")

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=255)
    avaliacao = models.IntegerField("Avaliação")

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=255)
    paginas = models.IntegerField("Páginas")
    preco = models.DecimalField("Preço",max_digits=10, decimal_places=2)
    avaliacao = models.FloatField("Avaliação")
    autores = models.ManyToManyField(Autor)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    data_pub = models.DateField("Data da Publicação")

    def __str__(self):
        return self.nome


class Loja(models.Model):
    nome = models.CharField(max_length=255)
    quantidade_de_clientes = models.PositiveIntegerField("QTD de clientes")

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)