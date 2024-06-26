# Generated by Django 4.2.2 on 2024-06-04 19:03

import comum.utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_concessionaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.endereco', verbose_name='endereco_id')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='carro',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='carro',
        ),
        migrations.AddField(
            model_name='carro',
            name='cor',
            field=models.CharField(default='azul', verbose_name='Cor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='disponivel',
            field=models.BooleanField(default=True, verbose_name='Disponivel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='final_placa',
            field=models.CharField(default='', verbose_name='Final da placa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='ipva_pago',
            field=models.BooleanField(default=True, verbose_name='IPVa pago'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='quilometragem',
            field=models.IntegerField(default=0, verbose_name='Quilometragem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='transmissao',
            field=models.CharField(default='', verbose_name='Transmissao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anexo',
            name='arquivo',
            field=models.FileField(upload_to='site_concessionaria/anexos', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'xlsx', 'png', 'jpeg']), comum.utils.validate_file_size], verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='valorBase',
            field=models.FloatField(verbose_name='Valor Base'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='preco',
            field=models.FloatField(verbose_name='Preco'),
        ),
        migrations.CreateModel(
            name='Simulacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Simulação')),
                ('precoFinal', models.FloatField(verbose_name='Preco Final')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Nome da Simulação')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Nome da Simulação')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(verbose_name='Nome Loja')),
                ('telefone', models.CharField(verbose_name='Telefone')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.endereco', verbose_name='endereco_id')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraAgendamento', models.DateTimeField(verbose_name='Data Hora Agendamento')),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.carro', verbose_name='Carro_id')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.cliente', verbose_name='Cliente_id')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.loja', verbose_name='Loja_id')),
            ],
        ),
        migrations.CreateModel(
            name='CarroRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.carro')),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.recurso')),
                ('simulacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_concessionaria.simulacao')),
            ],
            options={
                'unique_together': {('simulacao', 'carro', 'recurso')},
            },
        ),
    ]
