# Generated by Django 2.2.3 on 2019-08-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190603_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='githuburl',
            field=models.CharField(default='http://google.com/', max_length=100),
            preserve_default=False,
        ),
    ]
