# Generated by Django 2.0.6 on 2018-06-25 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_auto_20180626_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('stdcommon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.StdCommon')),
                ('subject_marks', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('results.stdcommon',),
        ),
        migrations.AlterField(
            model_name='stdsubject',
            name='subject_full_marks',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=5, verbose_name='Full Marks'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='std_class',
            field=models.CharField(choices=[('6', 'SIX'), ('7', 'SEVEN')], default=6, help_text='Select a class', max_length=2, verbose_name='Student Class'),
        ),
        migrations.AddField(
            model_name='marks',
            name='std_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.StudentInfo'),
        ),
        migrations.AddField(
            model_name='marks',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.StdSubject'),
        ),
    ]
