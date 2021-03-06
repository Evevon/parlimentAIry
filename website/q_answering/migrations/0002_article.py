# Generated by Django 2.1.4 on 2019-01-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q_answering', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('article_document', models.CharField(max_length=200)),
                ('article_type', models.CharField(choices=[('SCI', 'onderzoek'), ('NEW', 'nieuws'), ('LAW', 'wet')], default='NEW', max_length=3)),
            ],
        ),
    ]
