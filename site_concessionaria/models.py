from django.core.validators import FileExtensionValidator
from django.db import models

from comum.utils import validate_file_size

class Carro(models.Model):
    modelo = models.CharField(verbose_name="Modelo", max_length=50)
    ano = models.SmallIntegerField(verbose_name="Ano")
    combustivel = models.CharField(verbose_name="Combustível", max_length=50)
    # carroceria = models.CharField(verbose_name"Carroceria"max_length=50)
    marca = models.CharField(verbose_name="Marca", max_length=50)
    valorBase = models.DecimalField(verbose_name="Valor Base", max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(verbose_name="Data de criacao", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Data de atualizacao", auto_now=True)
    ativo = models.BooleanField(verbose_name="Ativo/Inativo", default=True)

    def __str__(self):
        return self.modelo


class Anexo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    descricao = models.TextField(verbose_name="Descricao")
    carro = models.ForeignKey(
        Carro, on_delete=models.SET_NULL, verbose_name='Carro', null=True
    )

    arquivo = models.FileField(
        upload_to='site_concessionaria/',
        validators=[
            FileExtensionValidator(['pdf', 'docx', "xlsx", "png", "jpeg"]),
            validate_file_size
        ],
        verbose_name='Arquivo'
    )

    def __str__(self):
        return self.nome


class Recurso(models.Model):
    carro = models.ForeignKey(Carro, verbose_name="Carro_id", on_delete=models.CASCADE)
    nome = models.CharField(verbose_name="Nome", max_length=50)
    preco = models.DecimalField(verbose_name="Preco", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.preco}"


class Endereco(models.Model):
    rua = models.CharField(verbose_name="Rua", max_length=255)
    numero = models.CharField(verbose_name="Numero", max_length=255)
    complemento = models.CharField(verbose_name="Complemento", max_length=255, blank=True, default='')
    Bairro = models.CharField(verbose_name="Bairro", max_length=255)
    cidade = models.CharField(verbose_name="Cidade", max_length=255)
    estado = models.CharField(verbose_name="estado", max_length=255)
    cep = models.CharField(verbose_name="CEP", max_length=255)
    latitude = models.FloatField(verbose_name="latitude")
    longitude = models.FloatField(verbose_name="longitude")
    created_at = models.DateTimeField(verbose_name="Data de criacao", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Data de atualizacao", auto_now=True)
    ativo = models.BooleanField(verbose_name="Ativo/Inativo", default=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.complemento}, {self.Bairro}, {self.cidade}, {self.estado}, {self.cep}"  # Uma representação mais detalhada do endereço