# Generated by Django 3.2.6 on 2021-11-24 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElementosProteccionPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('nit', models.CharField(max_length=11)),
                ('certificado_arl', models.FileField(upload_to='SSGST/documentos')),
                ('autorizado', models.BooleanField()),
                ('seguridad_social', models.FileField(upload_to='SSGST/documentos')),
                ('telefono1', models.PositiveBigIntegerField()),
                ('telefono2', models.PositiveBigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('tipo_empresa', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElementosProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ficha_seguridad', models.FileField(upload_to='SSGST/documentos')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proveedores.elementosproteccionpersonal')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proveedores.proveedores')),
            ],
        ),
    ]
