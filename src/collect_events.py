from textwrap import indent
from typing import Dict
import scraper as _scraper
import json as json

#Con esta funcion creamos el diccionario de noticias y utilizamos el scraper para  buscar esas noticias y meterlas dentro del diccionario
#Seccion:CIUDAD
def create_events_dict() -> Dict:
    noticias = dict()
    noticias = _scraper.events_of_the_day('ciudad')
    return noticias

#Pasamos la funcion que forma el diccionario como variable noticia y utilizamos la funcion dump para obtener una cadena de caracteres 
# en formato JSON.
if __name__ == '__main__':
    noticias = create_events_dict()
    with open('json/city.json', mode='w') as noticias_file:
        json.dump(noticias, noticias_file, ensure_ascii=False, indent=4)
    

#Seccion:DEPORTES
def create_deportes_dict() -> Dict:
    noticias = dict()
    noticias = _scraper.events_of_the_day('deportes')
    return noticias

if __name__ == '__main__':
    noticias = create_deportes_dict()
    with open('json/sports.json', mode='w') as noticias_file:
        json.dump(noticias, noticias_file, ensure_ascii=False, indent=4)

#Seccion:OCIO
def create_ocio_dict() -> Dict:
    noticias = dict()
    noticias = _scraper.events_of_the_day('ocio')
    return noticias

if __name__ == '__main__':
    noticias = create_ocio_dict()
    with open('json/leisure.json', mode='w') as noticias_file:
        json.dump(noticias, noticias_file, ensure_ascii=False, indent=4)


#Seccion:ULTIMAS NOTICIAS
def create_ultimas_dict() -> Dict:
    noticias = dict()
    noticias = _scraper.events_of_the_day('ultimas-noticias')
    return noticias

if __name__ == '__main__':
    noticias = create_ultimas_dict()
    with open('json/Breaking-news.json', mode='w') as noticias_file:
        json.dump(noticias, noticias_file, ensure_ascii=False, indent=4)


#Seccion:POLICIALES
def create_policiales_dict() -> Dict:
    noticias = dict()
    noticias = _scraper.events_of_the_day('policiales')
    return noticias

if __name__ == '__main__':
    noticias = create_policiales_dict()
    with open('json/police.json', mode='w') as noticias_file:
        json.dump(noticias, noticias_file, ensure_ascii=False, indent=4)

#Seccion:REGION
def create_region_dict() -> Dict:
    noticias = dict()
    noticias = _scraper.events_of_the_day('policiales')
    return noticias

if __name__ == '__main__':
    noticias = create_region_dict()
    with open('json/region.json', mode='w') as noticias_file:
        json.dump(noticias, noticias_file, ensure_ascii=False, indent=4)