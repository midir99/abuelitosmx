import csv
import datetime
import json

from django.core.management import base
from django.utils import text


class Command(base.BaseCommand):
    help = (
        "This command transforms the CSV file downloaded from the "
        '"Single Catalog of Keys of State, Municipal and Local Geostatistical Areas" '
        "report into a JSON fixture, so you can load the locations easily into the "
        "database. Find the CSV here: https://www.inegi.org.mx/app/ageeml/"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "csvfile",
            type=str,
            help="The CSV file downloaded from the INEGI.",
        )
        parser.add_argument(
            "outputfile",
            type=str,
            help="The file to dump the fixture (i.e., people/fixtures/people/{state_name}_locations.json).",
        )
        parser.add_argument(
            "--quotechar",
            type=str,
            default='"',
        )
        parser.add_argument("--delimiter", type=str, default=",")
        parser.add_argument(
            "--encoding",
            type=str,
            default="utf-8",
        )

    def handle(self, *args, **options):
        with open(options["csvfile"], "rt", encoding=options["encoding"]) as csvfile:
            reader = csv.DictReader(
                csvfile,
                delimiter=options["delimiter"],
                quotechar=options["quotechar"],
            )
            inegi_locations = tuple(reader)
        locations = tuple(map(transform_inegi_loc_to_model_loc, inegi_locations))
        with open(options["outputfile"], "wt", encoding="utf-8") as outputfile:
            json.dump(locations, outputfile)


def transform_inegi_loc_to_model_loc(inegi_loc):
    return {
        "model": "people.Location",
        "fields": {
            "agee_code": inegi_loc["CVE_ENT"],
            "agee_name": inegi_loc["NOM_ENT"],
            "agem_code": inegi_loc["CVE_MUN"],
            "agem_name": inegi_loc["NOM_MUN"],
            "loc_code": inegi_loc["CVE_LOC"],
            "loc_name": inegi_loc["NOM_LOC"],
        },
    }
