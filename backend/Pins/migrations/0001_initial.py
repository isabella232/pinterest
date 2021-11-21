<<<<<<< HEAD
# Generated by Django 3.2.9 on 2021-11-20 15:43
=======
# Generated by Django 3.2.9 on 2021-11-21 14:48
>>>>>>> origin/dev

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
<<<<<<< HEAD
=======
        ('Boards', '0001_initial'),
        ('Categories', '0001_initial'),
>>>>>>> origin/dev
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('attachment', models.ImageField(upload_to='uploads/pins/')),
                ('boards', models.ManyToManyField(to='Boards.Board')),
                ('categories', models.ManyToManyField(to='Categories.Category')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('pin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pins.pin')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'pin_id')},
            },
        ),
    ]
