# Generated by Django 3.2.9 on 2021-11-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_user_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
