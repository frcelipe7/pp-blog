# Generated by Django 4.0.4 on 2022-07-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_createdevocional_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(default='Usuário', max_length=200)),
            ],
        ),
    ]