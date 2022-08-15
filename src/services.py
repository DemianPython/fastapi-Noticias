from typing import Dict
import json as _json 


def get_ciudad_noticias() -> Dict:
    with open("json/city.json") as events_file:
        data = _json.load(events_file)
    return data


def get_deportes_noticias() -> Dict:
    with open("json/sports.json") as events_file:
        data = _json.load(events_file)
    return data

def get_ultimas_noticias() -> Dict:
    with open("json/Breaking-news.json") as events_file:
        data = _json.load(events_file)
    return data

def get_policia_noticias() -> Dict:
    with open("json/police.json") as events_file:
        data = _json.load(events_file)
    return data

def get_region_noticias() -> Dict:
    with open("json/region.json") as events_file:
        data = _json.load(events_file)
    return data

def get_ocio_noticias() -> Dict:
    with open("json/leisure.json") as events_file:
        data = _json.load(events_file)
    return data

    