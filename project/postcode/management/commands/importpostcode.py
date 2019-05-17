import csv
from django.core.management.base import BaseCommand, CommandError
from postcode.models import PLZO


class Command(BaseCommand):
    help = 'import new data from csv into database'

    def add_arguments(self, parser):
        parser.add_argument('filenames', nargs='+', type=str)

    def handle(self, *args, **options):
        for filename in options['filenames']:
            try:
                csvReader = csv.reader(open(filename, newline='', encoding='latin-1'), delimiter=';')
                headers = next(csvReader) 
                for row in csvReader:
                    try:
                        entry = PLZO(
                            city_name = row[0],
                            postcode = row[1],
                            additional_number = row[2],
                            community_name = row[3],
                            bfs_nr = row[4],
                            canton_abbrev = row[5],
                            wgs84_e = row[6],
                            wgs84_n = row[7],
                            lang = row[8],
                        )
                        entry.save()
                    except Exception as e:
                        print(e)
                        raise CommandError('Error while importing file "%s"' % filename)
            except Exception as e:
                print(e)
                raise CommandError('Error while importing file "%s"' % filename)

            self.stdout.write(self.style.SUCCESS('Successfully imported file "%s"' % filename))
