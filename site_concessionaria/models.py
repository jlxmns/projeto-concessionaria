from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User

from comum.utils import validate_file_size

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
        return f"{self.rua}, {self.numero}, {self.complemento}, {self.Bairro}, {self.cidade}, {self.estado}, {self.cep}"

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, verbose_name="endereco_id", on_delete=models.CASCADE, null=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Carro(models.Model):
    modelo = models.CharField(verbose_name="Modelo", max_length=50)
    ano = models.SmallIntegerField(verbose_name="Ano")
    combustivel = models.CharField(verbose_name="Combustível", max_length=50)
    # carroceria = models.CharField(verbose_name"Carroceria"max_length=50)
    marca = models.CharField(verbose_name="Marca", max_length=50)
    valorBase = models.FloatField(verbose_name="Valor Base")
    created_at = models.DateTimeField(verbose_name="Data de criacao", auto_now_add=True),
    updated_at = models.DateTimeField(verbose_name="Data de atualizacao", auto_now=True),
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
        upload_to='site_concessionaria/anexos',
        validators=[
            FileExtensionValidator(['pdf', 'docx', "xlsx", "png", "jpeg"]),
            validate_file_size
        ],
        verbose_name='Arquivo'
    )

    def __str__(self):
        return self.nome


class Recurso(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50)
    preco = models.FloatField(verbose_name="Preco")

    def __str__(self):
        return f"{self.nome} - {self.preco}"

class Loja (models.Model):
    nome = models.CharField(verbose_name="Nome Loja")
    telefone = models.CharField(verbose_name="Telefone")
    endereco = models.ForeignKey(Endereco, verbose_name="endereco_id", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nome} ({self.telefone})"
class Agendamentos(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente_id", on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, verbose_name="Loja_id", on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, verbose_name="Carro_id", on_delete=models.CASCADE)
    dataHoraAgendamento = models.DateTimeField(verbose_name="Data Hora Agendamento")
    def __str__(self):
        return f"Agendamento na loja {self.loja} às {self.dataHoraAgendamento}"

class Simulacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(verbose_name="Nome da Simulação", max_length=100)
    precoFinal = models.FloatField(verbose_name="Preco Final")
    created_at = models.DateTimeField(verbose_name="Data de Criacao", auto_now=True)
    updated_at = models.DateTimeField(verbose_name="Data de Atualização", auto_now_add=True)
    def __str__(self):
        return  f"{self.nome} {self.precoFinal}"

class CarroRecurso(models.Model):
    simulacao = models.ForeignKey(Simulacao, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['simulacao', 'carro', 'recurso']