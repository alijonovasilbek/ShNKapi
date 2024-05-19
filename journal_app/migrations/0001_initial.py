# Generated by Django 5.0.6 on 2024-05-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TagsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name_uz", models.CharField(max_length=222)),
                ("tag_name_en", models.CharField(max_length=222)),
            ],
            options={
                "verbose_name": "Tags",
                "db_table": "Tags_table",
            },
        ),
        migrations.CreateModel(
            name="JournalModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("journal_logo", models.ImageField(upload_to="journal_logos/")),
                ("journal_desc_uz", models.TextField()),
                ("journal_desc_en", models.TextField()),
                ("journal_date", models.DateTimeField(auto_now_add=True)),
                ("journal_tags", models.ManyToManyField(to="journal_app.tagsmodel")),
            ],
            options={
                "verbose_name": "Journals",
                "db_table": "Journal_table",
            },
        ),
    ]