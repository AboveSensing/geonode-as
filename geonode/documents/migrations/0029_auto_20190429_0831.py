# Generated by Django 1.11.20 on 2019-04-29 08:31


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0028_auto_20170801_1228_squashed_0035_auto_20190404_0820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelManagers(
            name='document',
            managers=[
            ],
        ),
    ]
