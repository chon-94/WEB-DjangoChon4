# Generated by Django 3.2.6 on 2022-12-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221201_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cita_1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cita_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cita_3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cita_4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cita_5',
        ),
        migrations.AddField(
            model_name='post',
            name='cita_1_0',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_1_1',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_1_2',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_1_3',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_1_4',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_2_0',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_2_1',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_2_2',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_2_3',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_2_4',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_3_0',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_3_1',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_3_2',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_3_3',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_3_4',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_4_0',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_4_1',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_4_2',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_4_3',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_4_4',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_5_0',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_5_1',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_5_2',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_5_3',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='post',
            name='cita_5_4',
            field=models.CharField(blank=True, max_length=750),
        ),
    ]
