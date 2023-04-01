# Generated by Django 4.1.7 on 2023-04-01 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('costo_por_hora', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora_fin', models.DateTimeField(default=django.utils.timezone.now)),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cancha', to='Reserva.cancha')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=10)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('esta_anulada', models.BooleanField(default=False)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='horario', to='Reserva.horario')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='persona', to='Reserva.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.FloatField()),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reserva', to='Reserva.reserva')),
            ],
        ),
    ]
