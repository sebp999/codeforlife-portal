# Generated by Django 3.2.20 on 2023-11-06 18:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0046_alter_school_country"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="school",
            name="postcode",
        ),
    ]
