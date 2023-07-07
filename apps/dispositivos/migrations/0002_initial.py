# Generated by Django 4.2.3 on 2023-07-07 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dispositivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefonos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rams',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.tiporam'),
        ),
        migrations.AddField(
            model_name='rams',
            name='velocidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dispositivos.ramsvelocidades'),
        ),
        migrations.AddField(
            model_name='historiales',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='graficas',
            name='gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dispositivos.graficasgb'),
        ),
        migrations.AddField(
            model_name='graficas',
            name='velocidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dispositivos.graficasvelocidades'),
        ),
        migrations.AddField(
            model_name='favoritos_urljuegos',
            name='favorito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.favoritos'),
        ),
        migrations.AddField(
            model_name='favoritos_urljuegos',
            name='urlJuego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.urljuegos'),
        ),
        migrations.AddField(
            model_name='favoritos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='grafica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.graficas'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='procesador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.procesadores'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.rams'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='sistemaOperativo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.sistemasoperativos'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
