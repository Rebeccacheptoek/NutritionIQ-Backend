# Generated by Django 4.2.2 on 2023-06-29 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='usertype',
            new_name='user_type',
        ),
    ]