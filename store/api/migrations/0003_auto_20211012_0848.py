# Generated by Django 3.2.8 on 2021-10-12 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_productcategory_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='title',
            new_name='name',
        ),
    ]
