# Generated by Django 4.1.3 on 2022-11-10 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_alter_agentname_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentname',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedlgaresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedpuresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedstateresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedwardresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lga',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='pollingunit',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ward',
            options={'managed': False},
        ),
    ]