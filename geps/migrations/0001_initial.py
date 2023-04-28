# Generated by Django 4.1.7 on 2023-04-28 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Regioes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regiao', models.CharField(max_length=50)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regiao', to='geps.cidade')),
            ],
            options={
                'ordering': ['regiao'],
            },
        ),
        migrations.CreateModel(
            name='DisponibilidadeRegiao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geps.docente')),
                ('regiao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geps.regioes')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cidades', to='geps.estado'),
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bairros', to='geps.cidade')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
