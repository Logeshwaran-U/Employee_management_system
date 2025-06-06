# Generated by Django 5.1.1 on 2024-10-02 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_positionlist_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country_code', models.CharField(choices=[('IN', '+91'), ('US', '+1'), ('AU', '+61'), ('CA', '+1'), ('UK', '+44')], max_length=2)),
                ('contact_number', models.CharField(max_length=15)),
                ('date_hired', models.DateField()),
                ('monthly_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='base.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='base.positionlist')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
