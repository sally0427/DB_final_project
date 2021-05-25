# Generated by Django 3.2.2 on 2021-05-25 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('Did', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=20, null=True)),
                ('Dphone', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]