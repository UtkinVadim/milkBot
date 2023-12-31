# Generated by Django 4.2.4 on 2023-08-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MilkBuyer',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
