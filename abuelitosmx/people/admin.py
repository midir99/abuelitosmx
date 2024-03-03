from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from people.models import Location, Person


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = (
        "display_full_code",
        "agee_name",
        "agem_name",
        "loc_name",
    )
    ordering = (
        "agee_name",
        "agem_name",
        "loc_name",
    )
    search_fields = (
        "agee_name",
        "agem_name",
        "loc_name",
    )

    @admin.display(description=_("Full code"))
    def display_full_code(self, obj):
        return f"{obj.agee_code}/{obj.agem_code}/{obj.loc_code}"


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("full_name",),
    }
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    list_display = (
        "full_name",
        "alias",
        "date_of_birth",
        "date_of_death",
        "display_location",
    )
    ordering = (
        "full_name",
        "date_of_birth",
    )
    search_fields = (
        "full_name",
        "alias",
    )

    @admin.display(description=_("Location"))
    def display_location(self, obj):
        if obj.location is None:
            return
        return f"{obj.location.loc_name}, {obj.location.agem_name}, {obj.location.agee_name}"
