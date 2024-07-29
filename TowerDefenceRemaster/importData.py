import json


class ImportData:
    def map(self):
        with open('mapa.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def torres(self):
        with open('torres.json', 'r', encoding='utf-8') as file:
            return json.load(file)
