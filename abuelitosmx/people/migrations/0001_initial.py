# Generated by Django 5.0.2 on 2024-03-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("agee_code", models.CharField(max_length=2, verbose_name="AGEE code")),
                (
                    "agee_name",
                    models.CharField(max_length=30, verbose_name="AGEE name"),
                ),
                ("agem_code", models.CharField(max_length=3, verbose_name="AGEM code")),
                (
                    "agem_name",
                    models.CharField(max_length=50, verbose_name="AGEM name"),
                ),
                (
                    "loc_code",
                    models.CharField(max_length=4, verbose_name="location code"),
                ),
                (
                    "loc_name",
                    models.CharField(max_length=50, verbose_name="location name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                (
                    "slug",
                    models.SlugField(
                        help_text="Slug to identify this person.",
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        help_text="Full name of the person.",
                        max_length=200,
                        verbose_name="full name",
                    ),
                ),
                (
                    "alias",
                    models.CharField(
                        help_text="Alias of the person.",
                        max_length=50,
                        verbose_name="alias",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True,
                        help_text="Date of birth of the person.",
                        verbose_name="birth date",
                    ),
                ),
                (
                    "death_date",
                    models.DateField(
                        blank=True,
                        help_text="Date of death of the person.",
                        verbose_name="death date",
                    ),
                ),
                (
                    "biography",
                    models.TextField(
                        blank=True,
                        help_text="Biography of the person.",
                        verbose_name="biography",
                    ),
                ),
                (
                    "autobiography",
                    models.TextField(
                        blank=True,
                        help_text="Autobiography of the person.",
                        verbose_name="autobiography",
                    ),
                ),
                (
                    "see_more_at",
                    models.TextField(
                        blank=True,
                        help_text="Links or places where people can find more information about this person.",
                        verbose_name="see more at",
                    ),
                ),
                (
                    "interesting_facts",
                    models.TextField(
                        blank=True,
                        help_text="Interesting facts about the person.",
                        verbose_name="interesting facts",
                    ),
                ),
                (
                    "anecdotes",
                    models.TextField(
                        blank=True,
                        help_text="Anecdotes of the person.",
                        verbose_name="anecdotes",
                    ),
                ),
                (
                    "picture_ft",
                    models.ImageField(
                        blank=True,
                        help_text="Picture of this person that will be shown in the family tree.",
                        upload_to="persons/pictures_ft/",
                        verbose_name="picture for their family tree",
                    ),
                ),
                (
                    "picture_1",
                    models.ImageField(
                        blank=True,
                        help_text="First picture of this person that will be shown in their gallery.",
                        upload_to="persons/pictures/",
                        verbose_name="first picture",
                    ),
                ),
                (
                    "picture_1_caption",
                    models.CharField(
                        blank=True,
                        help_text="Caption for the first picture of this person.",
                        max_length=100,
                        verbose_name="first picture caption",
                    ),
                ),
                (
                    "picture_2",
                    models.ImageField(
                        blank=True,
                        help_text="Second picture of this person that will be shown in their gallery.",
                        upload_to="persons/pictures/",
                        verbose_name="second picture",
                    ),
                ),
                (
                    "picture_2_caption",
                    models.CharField(
                        blank=True,
                        help_text="Caption for the second picture of this person.",
                        max_length=100,
                        verbose_name="second picture caption",
                    ),
                ),
                (
                    "picture_3",
                    models.ImageField(
                        blank=True,
                        help_text="Third picture of this person that will be shown in their gallery.",
                        upload_to="persons/pictures/",
                        verbose_name="third picture",
                    ),
                ),
                (
                    "picture_3_caption",
                    models.CharField(
                        blank=True,
                        help_text="Caption for the third picture of this person.",
                        max_length=100,
                        verbose_name="third picture caption",
                    ),
                ),
                (
                    "picture_4",
                    models.ImageField(
                        blank=True,
                        help_text="Forth picture of this person that will be shown in their gallery.",
                        upload_to="persons/pictures/",
                        verbose_name="forth picture",
                    ),
                ),
                (
                    "picture_4_caption",
                    models.CharField(
                        blank=True,
                        help_text="Caption for the forth picture of this person.",
                        max_length=100,
                        verbose_name="forth picture caption",
                    ),
                ),
                (
                    "picture_5",
                    models.ImageField(
                        blank=True,
                        help_text="Fifth picture of this person that will be shown in their gallery.",
                        upload_to="persons/pictures/",
                        verbose_name="fifth picture",
                    ),
                ),
                (
                    "picture_5_caption",
                    models.CharField(
                        blank=True,
                        help_text="Caption for the fifth picture of this person.",
                        max_length=100,
                        verbose_name="fifth picture caption",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="location",
            constraint=models.UniqueConstraint(
                fields=("agee_code", "agem_code", "loc_code"), name="unique_location"
            ),
        ),
    ]
