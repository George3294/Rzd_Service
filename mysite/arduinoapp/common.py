from csv import DictReader
from io import TextIOWrapper
from arduinoapp.models import Station


def save_csv_stations(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)
    stations = [
        Station(**row)
        for row in reader
    ]
    Station.objects.bulk_create(stations)
    return Station