from icecream import ic
import requests
from requests.models import Response
import lxml.html as html
import os
import datetime

"""
Se dan de alra como variables globales tanto url de la web donde se realizara
el scraping como las funciones xpath que se generaron para encontrar las ligas
de todas las notas que aparecene en el home de la web, los titulos, los resumenes
y el articulo completo

"""
HOME_URL = 'https://www.larepublica.co'

XPATH_LINK_TO_ARTICLE = '//text-fill[@class=contains(.,"V_")]/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/text-fill/span/text()'
XPATH_SUMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'

def parse_notice(link, today):
    
    """
    Función para realizar el analisis de titulo, resumen y noticia con
    el fin de guardar la información capturada del día
    
    """
    try:

        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:

                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"', '')
                title = title.replace(':', '')

                print(f'Creando noticia: "{title}"')
                
                sumary = parsed.xpath(XPATH_SUMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            
            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'w', encoding = 'utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(sumary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    
    except ValueError as ve:
        print(ve)


def parse_home():
    
    """
    Función para realizar el analisis de url para obtener la informacion
    de mi scraper. Toda la función se encierra dentro de un bloque try
    para tener en cuenta el manejo de excepciones
    
    """
    try:
        # Se valida si la url del sitio es accesible
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            # Se extrae el contenido completo de la url con un set de caracteres utf8
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            # Se extraen las urls de las noticias, usando la instruccion definida
            # previamente en xpath
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)

            today = datetime.date.today().strftime('%Y-%m-%d')
            if not os.path.isdir(today):
                os.mkdir(today)
            
            for link in links_to_notices:
                parse_notice(link, today)
            
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()