# Generated by Django 4.2.16 on 2024-09-18 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("submission", "0076_submissionfavourite"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="submissionfavourite",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="submissionfavourite",
            name="talk_list",
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name="submissionfavourite",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="submission_favorites",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterModelTable(
            name="submissionfavourite",
            table='"submission_submission_favourites"',
        ),
        migrations.RemoveField(
            model_name="submissionfavourite",
            name="created",
        ),
        migrations.RemoveField(
            model_name="submissionfavourite",
            name="submission",
        ),
        migrations.RemoveField(
            model_name="submissionfavourite",
            name="updated",
        ),
    ]
