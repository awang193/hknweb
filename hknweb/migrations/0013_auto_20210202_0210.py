# Generated by Django 2.2.8 on 2021-02-02 10:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hknweb', '0012_delete_reviewsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be ten digits.', regex='^([^\\d]*\\d){10}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='candidate_semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hknweb.Semester'),
        ),
    ]