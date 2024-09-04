import json


class ImportData:
    def map(self):
        with open('mapa.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def torres(self):
        with open('torres.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def partcileType(self, particletype):
        with open('particle.json', 'r', encoding='utf-8') as file:
            return json.load(file)[particletype]
        
    def setDifficult(self):
        with open('level.json','r', enconding='utf-8') as file:
            return json.load(file)