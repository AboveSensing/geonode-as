# Generated by Django 2.2.16 on 2020-11-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_merge_20201016_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='attribution',
            field=models.CharField(blank=True, help_text='authority or function assigned, as to a ruler, legislative assembly, delegate, or the like.', max_length=2048, null=True, verbose_name='Attribution'),
        ),
    ]
