# Generated by Django 4.2.2 on 2024-06-05 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_concessionaria', '0003_alter_agendamentos_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamentos',
            name='carro',
        ),
        migrations.RemoveField(
            model_name='agendamentos',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='agendamentos',
            name='loja',
        ),
        migrations.AddField(
            model_name='agendamentos',
            name='contato',
            field=models.CharField(default='', max_length=100, verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='agendamentos',
            name='info_adicional',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='agendamentos',
            name='nome',
            field=models.CharField(default='', max_length=100, verbose_name='Nome Completo'),
        ),
        migrations.AddField(
            model_name='agendamentos',
            name='servico',
            field=models.CharField(choices=[('TestDrive', 'Test-drive'), ('TrocaOleo', 'Troca de Óleo')], default='TestDrive', verbose_name='Serviço'),
        ),
        migrations.AlterField(
            model_name='agendamentos',
            name='dataHoraAgendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 17, 57, 15, 853956, tzinfo=datetime.timezone.utc), verbose_name='Data Hora Agendamento'),
        ),
    ]
