from icecream import ic
import requests as rq
import bs4

def run():
    
    response = rq.get('https://www.platzi.com')
    response.encoding = 'utf-8'

    """
    Esta libreria toma la entrada de texto del la web elegida y la parsea por
    medio de formato html. Es importante mencionar que se puede realizar
    el parseo por diferentes formatos.

    Teniendola así, se pueden usar funciones propias de soup para seleccionar
    ciertos nodos del html de la web.
    En el ejemplo, se listan las escuelas correspondientes a platzi por medio
    del nodo al cual se cuelgan en la estructura del html
    
    """
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    ic(soup.title.text)
    ic(soup.select('meta[name = description]'))
    ic(soup.select('meta[name = description]')[0]['content'])
    courses_links = soup.select('.SchoolsList-school')
    courses = [course['href'] for course in courses_links]

    print('Escuelas disponibles por medio de la web al 13/07/2021\n')
    for course in courses:
        print(course)


if __name__ == '__main__':
    run()