from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    """
    The fields in this model are taken from the
    "Single Catalog of Keys of State, Municipal and Local Geostatistical Areas" report
    provided by the INEGI.

    https://www.inegi.org.mx/app/ageeml/
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    agee_code = models.CharField(
        _("AGEE code"),
        max_length=2,
    )
    agee_name = models.CharField(
        _("AGEE name"),
        max_length=30,
    )
    agem_code = models.CharField(
        _("AGEM code"),
        max_length=3,
    )
    agem_name = models.CharField(
        _("AGEM name"),
        max_length=50,
    )
    loc_code = models.CharField(
        _("location code"),
        max_length=4,
    )
    loc_name = models.CharField(
        _("location name"),
        max_length=50,
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_(
            "This timestamp shows when this record was created. This field is "
            "populated automatically."
        ),
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_(
            "This timestamp shows when this record was last updated. This field is "
            "populated automatically."
        ),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_location",
                fields=["agee_code", "agem_code", "loc_code"],
            )
        ]

    def __str__(self):
        return f"{self.loc_name}, {self.agem_name}, {self.agee_name}"


class Person(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        max_length=50,
        help_text=_("Slug to identify this person."),
    )
    full_name = models.CharField(
        _("full name"),
        max_length=200,
        help_text=_("Full name of the person."),
    )
    alias = models.CharField(
        _("alias"),
        max_length=50,
        blank=True,
        help_text=_("Alias of the person."),
    )
    date_of_birth = models.DateField(
        _("date of birth"),
        blank=True,
        null=True,
        help_text=_("Date of birth of the person."),
    )
    date_of_death = models.DateField(
        _("date of death"),
        blank=True,
        null=True,
        help_text=_("Date of death of the person."),
    )
    biography = models.TextField(
        _("biography"), blank=True, help_text=_("Biography of the person.")
    )
    autobiography = models.TextField(
        _("autobiography"),
        blank=True,
        help_text=_("Autobiography of the person."),
    )
    see_more_at = models.TextField(
        _("see more at"),
        blank=True,
        help_text=_(
            "Links or places where people can find more information about this person."
        ),
    )
    interesting_facts = models.TextField(
        _("interesting facts"),
        blank=True,
        help_text=_("Interesting facts about the person."),
    )
    anecdotes = models.TextField(
        _("anecdotes"),
        blank=True,
        help_text=_("Anecdotes of the person."),
    )
    picture_ft = models.ImageField(
        _("family tree picture"),
        upload_to="persons/pictures_ft/",
        blank=True,
        help_text=_("Picture of this person that will be shown in the family tree."),
    )
    picture_1 = models.ImageField(
        _("first picture"),
        upload_to="persons/pictures/",
        blank=True,
        help_text=_(
            "First picture of this person that will be shown in their gallery."
        ),
    )
    picture_1_caption = models.CharField(
        _("first picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the first picture of this person."),
    )
    picture_2 = models.ImageField(
        _("second picture"),
        upload_to="persons/pictures/",
        blank=True,
        help_text=_(
            "Second picture of this person that will be shown in their gallery."
        ),
    )
    picture_2_caption = models.CharField(
        _("second picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the second picture of this person."),
    )
    picture_3 = models.ImageField(
        _("third picture"),
        upload_to="persons/pictures/",
        blank=True,
        help_text=_(
            "Third picture of this person that will be shown in their gallery."
        ),
    )
    picture_3_caption = models.CharField(
        _("third picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the third picture of this person."),
    )
    picture_4 = models.ImageField(
        _("forth picture"),
        upload_to="persons/pictures/",
        blank=True,
        help_text=_(
            "Forth picture of this person that will be shown in their gallery."
        ),
    )
    picture_4_caption = models.CharField(
        _("forth picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the forth picture of this person."),
    )
    picture_5 = models.ImageField(
        _("fifth picture"),
        upload_to="persons/pictures/",
        blank=True,
        help_text=_(
            "Fifth picture of this person that will be shown in their gallery."
        ),
    )
    picture_5_caption = models.CharField(
        _("fifth picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the fifth picture of this person."),
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("Location where this person lived most of their life."),
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_(
            "This timestamp shows when this record was created. This field is "
            "populated automatically."
        ),
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_(
            "This timestamp shows when this record was last updated. This field is "
            "populated automatically."
        ),
    )

    def __str__(self):
        return f"{self.full_name}"
