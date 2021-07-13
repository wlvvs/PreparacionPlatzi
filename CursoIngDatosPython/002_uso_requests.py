from icecream import ic
import requests as rq
import bs4

def run():
    
    # Se solicita una respuesta a cierta URL dada
    response = rq.get('https://www.platzi.com')
    response.encoding = 'utf-8'

    """
    Al realizar la impresión por medio de icecream, me regresa uno de los
    valores inmersos en las propiedades de get, que es el status code

    Con la opción dir, se imprimen todos los atributos que contiene
    el get de la URl, mismos que podemos consultar de manera individual

    En el header, se observan los valores iniciales de la web que consultamos
    y esta estructura esta planteada como un diccionario, por lo que
    podemos movernos a traves de las keys del mismo.

    El valor text muestra el archivo html de la web consultada, mismo que
    guardamos para verificar como luce

    """
    ic(response)
    ic(dir(response))
    ic(response.status_code)
    ic(response.headers)
    ic(response.headers['Date'])

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    with open('./files/example_requests.html', 'w', encoding = 'utf-8') as f:
                f.write(response.text)
    with open('./files/example_requests_soup.html', 'w', encoding = 'utf-8') as f:
                f.write(soup.text)


if __name__ == '__main__':
    run()