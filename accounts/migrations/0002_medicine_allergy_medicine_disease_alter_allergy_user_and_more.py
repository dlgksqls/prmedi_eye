# Generated by Django 4.2.3 on 2023-08-11 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='allergy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allergy_medi', to='accounts.allergy'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='disease',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disease_medi', to='accounts.disease'),
        ),
        migrations.AlterField(
            model_name='allergy',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allergy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='disease',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disease', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine', to=settings.AUTH_USER_MODEL),
        ),
    ]