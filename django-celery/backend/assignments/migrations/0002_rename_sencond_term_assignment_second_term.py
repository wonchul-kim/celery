# Generated by Django 4.2 on 2023-04-21 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assignment", old_name="sencond_term", new_name="second_term",
        ),
    ]