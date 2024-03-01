from django.contrib import admin
from people.models import Location

from django.utils.translation import gettext_lazy as _


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "full_code",
        "agee_name",
        "agem_name",
        "loc_name",
    )

    ordering = ("agee_name", "agem_name", "loc_name")

    @admin.display(description=_("Full code"), empty_value="???")
    def full_code(self, obj):
        return f"{obj.agee_code}/{obj.agem_code}/{obj.loc_code}"

