import util

from datetime import datetime

DOLAR_OFICIAL_URL = 'https://tiempofinanciero.com.ar/cotizaciones/dolar-oficial/'
DOLAR_BLUE_URL = 'https://tiempofinanciero.com.ar/cotizaciones/dolar-blue/'
DOLAR_TURISTA_URL = 'https://tiempofinanciero.com.ar/cotizaciones/dolar-turista/'
DOLAR_MEP_URL = 'https://tiempofinanciero.com.ar/cotizaciones/dolar-bolsa/'
DOLAR_CCL_URL = 'https://tiempofinanciero.com.ar/cotizaciones/contadoliqui/'
EURO_OFICIAL_URL = 'https://tiempofinanciero.com.ar/cotizaciones/euro/'
EURO_BLUE_URL = 'https://tiempofinanciero.com.ar/cotizaciones/euro-blue/'
EURO_TARJETA_URL = 'https://tiempofinanciero.com.ar/cotizaciones/euro-tarjeta/'
REAL_OFICIAL_URL = 'https://tiempofinanciero.com.ar/cotizaciones/real-oficial/'
REAL_BLUE_URL = 'https://tiempofinanciero.com.ar/cotizaciones/real-blue/'


def formatResponse(values):
    compra = values[0].replace('.', '').replace(',', '.')
    venta = values[1].replace('.', '').replace(',', '.')
    return {
        "fecha": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "compra": f"{util.convertToDecimal(compra):.2f}",
        "venta": f"{util.convertToDecimal(venta):.2f}",
    }


def getDolarOficial():
    return _getValues(DOLAR_OFICIAL_URL)


def getDolarBlue():
    return _getValues(DOLAR_BLUE_URL)


def getDolarTurista():
    return _getValues(DOLAR_TURISTA_URL)


def getDolarMep():
    return _getValues(DOLAR_MEP_URL)


def getDolarCcl():
    return _getValues(DOLAR_CCL_URL)


def getEuroOficial():
    return _getValues(EURO_OFICIAL_URL)


def getEuroBlue():
    return _getValues(EURO_BLUE_URL)


def getEuroTarjeta():
    return _getValues(EURO_TARJETA_URL)


def getRealOficial():
    return _getValues(REAL_OFICIAL_URL)


def getRealBlue():
    return _getValues(REAL_BLUE_URL)


def _getValues(url):
    import requests
    from bs4 import BeautifulSoup

    html_source = requests.get(url).text
    soup = BeautifulSoup(html_source, 'lxml')

    div = soup.find('div', id='price-content')
    tds = div.find('div', {'class', 'wp-block-table'}
                   ).find('table').tbody.find('tr').find_all('td')
    print(tds)
    compra = tds[1].text[1:]
    venta = tds[2].text[1:]
    return [compra, venta]
