from django.db import models

class Carro():
    modelo = models.CharField(verbose_name="Modelo",max_length=50)
    ano = models.SmallIntegerField(verbose_name="Ano")
    combustivel = models.CharField(verbose_name="Combustível",max_length=50)
    #carroceria = models.CharField(verbose_name"Carroceria"max_length=50)
    marca = models.CharField(verbose_name="Marca",max_length=50)
    valorBase = models.DecimalField(verbose_name="Valor Base",max_digits=9,decimal_places=2)
    created_at = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Data de atualização", auto_now=True)
    ativo = models.BooleanField(verbose_name="Ativo/Inativo", default=True)

class Anexo():
    nome = models.CharField(max_length=255, verbose_name="Nome")
    descricao = models.TextField(verbose_name="Descrição")
    carro = models.ForeignKey(
        Carro, on_delete=models.SET_NULL, verbose_name='Carro', null=True
    )

    arquivo = models.FileField(
        upload_to='site_concessionaria/',
        validators=[
            FileExstencionValidator(['pdf', 'docx', "xlsx", "png", "jpeg"]),
            validate_file_size
        ],
        verbose_name='Arquivo'
    )

class Recurso():
    carro = models.ForeignKey(Carro,verbose_name="Carro_id", on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=)

class Endereco(models.Model):
    rua = models.CharField(verbose_name="Rua", max_length=255)
    numero = models.CharField(verbose_name="Número", max_length=255)
    complemento = models.CharField(verbose_name="Complemento", max_length=255, blank=True, default='')
    Bairro = models.CharField(verbose_name="Bairro", max_length=255)
    cidade = models.CharField(verbose_name="Cidade", max_length=255)
    estado = models.CharField(verbose_name="estado", max_length=255)
    cep = models.CharField(verbose_name="CEP", max_length=255)
    latitude = models.FloatField(verbose_name="latitude")
    longitude = models.FloatField(verbose_name="longitude")
    created_at = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Data de atualização", auto_now=True)
    ativo = models.BooleanField(verbose_name="Ativo/Inativo", default=True)