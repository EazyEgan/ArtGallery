# Generated by Django 2.1 on 2019-04-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('forSale', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('portfolio', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pubDate', models.DateField()),
            ],
        ),
    ]
