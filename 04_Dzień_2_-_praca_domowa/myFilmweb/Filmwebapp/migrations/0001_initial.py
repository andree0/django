# Generated by Django 3.1.5 on 2021-01-21 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField(choices=[(1.0, '1.0'), (1.1, '1.1'), (1.2, '1.2'), (1.3, '1.3'), (1.4, '1.4'), (1.5, '1.5'), (1.6, '1.6'), (1.7, '1.7'), (1.8, '1.8'), (1.9, '1.9'), (2.0, '2.0'), (2.1, '2.1'), (2.2, '2.2'), (2.3, '2.3'), (2.4, '2.4'), (2.5, '2.5'), (2.6, '2.6'), (2.7, '2.7'), (2.8, '2.8'), (2.9, '2.9'), (3.0, '3.0'), (3.1, '3.1'), (3.2, '3.2'), (3.3, '3.3'), (3.4, '3.4'), (3.5, '3.5'), (3.6, '3.6'), (3.7, '3.7'), (3.8, '3.8'), (3.9, '3.9'), (4.0, '4.0'), (4.1, '4.1'), (4.2, '4.2'), (4.3, '4.3'), (4.4, '4.4'), (4.5, '4.5'), (4.6, '4.6'), (4.7, '4.7'), (4.8, '4.8'), (4.9, '4.9'), (5.0, '5.0'), (5.1, '5.1'), (5.2, '5.2'), (5.3, '5.3'), (5.4, '5.4'), (5.5, '5.5'), (5.6, '5.6'), (5.7, '5.7'), (5.8, '5.8'), (5.9, '5.9'), (6.0, '6.0'), (6.1, '6.1'), (6.2, '6.2'), (6.3, '6.3'), (6.4, '6.4'), (6.5, '6.5'), (6.6, '6.6'), (6.7, '6.7'), (6.8, '6.8'), (6.9, '6.9'), (7.0, '7.0'), (7.1, '7.1'), (7.2, '7.2'), (7.3, '7.3'), (7.4, '7.4'), (7.5, '7.5'), (7.6, '7.6'), (7.7, '7.7'), (7.8, '7.8'), (7.9, '7.9'), (8.0, '8.0'), (8.1, '8.1'), (8.2, '8.2'), (8.3, '8.3'), (8.4, '8.4'), (8.5, '8.5'), (8.6, '8.6'), (8.7, '8.7'), (8.8, '8.8'), (8.9, '8.9'), (9.0, '9.0'), (9.1, '9.1'), (9.2, '9.2'), (9.3, '9.3'), (9.4, '9.4'), (9.5, '9.5'), (9.6, '9.6'), (9.7, '9.7'), (9.8, '9.8'), (9.9, '9.9'), (10.0, '10.0')], default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Filmwebapp.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Filmwebapp.person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='Filmwebapp.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='Filmwebapp.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenplay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenplay', to='Filmwebapp.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(through='Filmwebapp.PersonMovie', to='Filmwebapp.Person'),
        ),
    ]
