import os, sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d_code.settings")
path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.abspath(path))
django.setup()
from test_d_code.models import DataSetModel
import csv
import json


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d_code.settings")
path = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.abspath(path))
django.setup()


def file_parser(input_file):
    if input_file.endswith('.json'):
        with open(os.path.abspath(input_file), 'r', encoding='utf-8') as json_file:
            json_file = json.load(json_file)
        for data in json_file['data']:
            DataSetModel.objects.create(
                group_region=data['Регион'],
                parameter_country=data['Страна'],
                value=data['Значение']
            )
        return 'OK'

    elif input_file.endswith('.csv'):
        with open(os.path.abspath(input_file), 'r', encoding='utf-8') as csv_file:
            csv_read_file = csv.reader(csv_file)
            for row in csv_read_file:
		if row[0] != 'Регион': 
                    DataSetModel.objects.create(
                        group_region=row[0],
                        parameter_country=row[1],
                        value=row[2]
                    )
		else:
		    pass
            return 'OK'
    else:
        return 'File not recognized'


if __name__ == '__main__':
    a = input('Введите имя файла!(файл должен находится в дерриктории  test_d_code): ')
    file_parser(a)
