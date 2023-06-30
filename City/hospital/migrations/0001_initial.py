# Generated by Django 4.1.3 on 2023-06-30 01:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=25)),
                ('Lname', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=30)),
                ('role', models.CharField(choices=[('D', 'Doctor'), ('N', 'Nurse')], max_length=1)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('nationalID', models.CharField(max_length=14)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.department')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=25)),
                ('Lname', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('nationalID', models.CharField(max_length=14)),
                ('medicalHistory', models.TextField(blank=True, max_length=10000)),
                ('admission_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('staff', models.ManyToManyField(to='hospital.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=500)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.employee')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]
