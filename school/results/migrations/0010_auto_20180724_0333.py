# Generated by Django 2.1rc1 on 2018-07-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_marks_subject_gpa_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='subject_marks',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Please give proper number', max_digits=5, null=True),
        ),
    ]