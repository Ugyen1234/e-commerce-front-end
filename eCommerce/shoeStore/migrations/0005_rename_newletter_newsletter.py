# Generated by Django 4.2.4 on 2023-10-30 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoeStore', '0004_rename_emails_newletter_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewLetter',
            new_name='NewsLetter',
        ),
    ]