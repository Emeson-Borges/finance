# Generated by Django 4.2.3 on 2023-07-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
                ('essencial', models.BooleanField(default=False)),
                ('valor_planejamento', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50)),
                ('banco', models.CharField(choices=[('BB', 'Banco do Brasil'), ('BR', 'Bradesco Bank'), ('NU', 'Nubank'), ('CX', 'Caixa Econômica'), ('INT', 'Inter'), ('SANT', 'Santander'), ('PIC', 'Picpay')], max_length=5)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=3)),
                ('valor', models.FloatField()),
                ('icone', models.ImageField(upload_to='icones')),
            ],
        ),
    ]
