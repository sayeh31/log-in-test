# Generated by Django 4.1.3 on 2022-12-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userlevels',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=45)),
                ('FormLevel', models.IntegerField(db_column='FormLevel')),
            ],
            options={
                'db_table': 'test',
                'managed': True,
            },
        ),
    ]
