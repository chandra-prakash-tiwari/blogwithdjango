# Generated by Django 4.0.1 on 2022-01-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_token_authentication_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authentication',
            name='user',
        ),
        migrations.AddField(
            model_name='authentication',
            name='username',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterModelTable(
            name='authentication',
            table=None,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
