from typing import List
import requests as _requests
import bs4 as _bs4

#Declaramos la ruta donde se van a buscar las noticias, en el parametro nombre(se refiere al nombre de la seccion)va la seccion de rosario3 
# q se quiere buscar ejemplo: f"https://www.rosario3.com/seccion/ultimas/"
def _generate_url(nombre:str) -> str:
    url = f"https://www.rosario3.com/seccion/{nombre}/"
    return url

#con la libreria BeautifulSoup vamos a extraer los titulos de las noticias en formato html.
def _get_page(url:str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

#Esta es la funcion para buscar las noticias ingresando el parametro nombre
def events_of_the_day(nombre:str) -> List[str]:
    url = _generate_url(nombre)
    page = _get_page(url)
    raw_noticia = page.find_all(class_="title")
    noticia = [noticia.text for noticia in raw_noticia]
    return  noticia


