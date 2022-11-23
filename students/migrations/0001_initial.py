# Generated by Django 4.1.3 on 2022-11-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=7)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]