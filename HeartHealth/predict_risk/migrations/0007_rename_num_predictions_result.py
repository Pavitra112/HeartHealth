# Generated by Django 4.2.4 on 2023-10-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("predict_risk", "0006_rename_sex_predictions_gender"),
    ]

    operations = [
        migrations.RenameField(
            model_name="predictions",
            old_name="num",
            new_name="result",
        ),
    ]
