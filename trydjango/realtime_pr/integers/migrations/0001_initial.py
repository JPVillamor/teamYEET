# Generated by Django 3.2.9 on 2022-01-21 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bar_mat', models.CharField(max_length=200)),
                ('tool_selected', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unit_name', models.CharField(max_length=200)),
                ('threshold_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timestamps', models.JSONField()),
                ('data_values', models.JSONField()),
                ('tool_used', models.JSONField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integers.user')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
