# Generated by Django 3.1.2 on 2021-09-24 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cnab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[(1, 'Débito'), (2, 'Boleto'), (3, 'Financiamento'), (4, 'Crédito'), (5, 'Recebimento Empréstimo'), (6, 'Vendas'), (7, 'Recebimento DOC'), (8, 'Recebimento TED'), (9, 'Aluguel')], max_length=1, verbose_name='Tipo de Transação')),
                ('data', models.DateField(verbose_name='Data da ocorrência')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor de Movimentação')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF do Beneficiário')),
                ('cartao', models.CharField(max_length=11, verbose_name='Cartão')),
                ('hora', models.CharField(max_length=6, verbose_name='Hora (UTC-3)')),
                ('dono_loja', models.CharField(max_length=14, verbose_name='Dono da Loja')),
                ('nome_loja', models.CharField(max_length=19, verbose_name='Nome da Loja')),
            ],
        ),
    ]
