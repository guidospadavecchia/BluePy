import os
from flask import Flask, send_from_directory, jsonify
from flask_caching import Cache
from datetime import datetime
from decimal import Decimal

VERSION = "1.1"
CACHE_TIMEOUT_SECONDS = os.getenv('CACHE_TIMEOUT', 3600)
GIT_REPO_URL = 'https://github.com/guidospadavecchia/BluePy'
DOLAR_OFICIAL_URL = 'https://tiempofinanciero.com.ar/cotizaciones/dolar-oficial/'
DOLAR_BLUE_URL = 'https://tiempofinanciero.com.ar/cotizaciones/dolar-blue/'
EURO_OFICIAL_URL = 'https://tiempofinanciero.com.ar/cotizaciones/euro/'
EURO_BLUE_URL = 'https://tiempofinanciero.com.ar/cotizaciones/euro-blue/'
REAL_OFICIAL_URL = 'https://tiempofinanciero.com.ar/cotizaciones/real-oficial/'
REAL_BLUE_URL = 'https://tiempofinanciero.com.ar/cotizaciones/real-blue/'


def getValues(url):
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


def formatResponse(values):
    return {
        "fecha": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "compra": f"{Decimal(values[0].replace(',', '.')):.2f}",
        "venta": f"{Decimal(values[1].replace(',', '.')):.2f}",
    }


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@ app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@ app.route("/")
def getRoot():
    html = f"""<head>
                   <title>BluePy API v{VERSION}</title>
               <head>
               <body>
                   BluePy API <b>v{VERSION}</b> - <b><a href={GIT_REPO_URL} style="text-decoration: none;">GitHub</a></b>
               </body>"""
    return html


@ app.route("/api/ping")
def ping():
    return 'pong'


@ app.route("/api/dolar/oficial")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getDolarOficial():
    dolarValues = getValues(DOLAR_OFICIAL_URL)
    dolarOficial = formatResponse(dolarValues)
    return jsonify(dolarOficial)


@ app.route("/api/dolar/blue")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getDolarBlue():
    dolarValues = getValues(DOLAR_BLUE_URL)
    dolarBlue = formatResponse(dolarValues)
    return jsonify(dolarBlue)


@ app.route("/api/euro/oficial")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getEuroOficial():
    euroValues = getValues(EURO_OFICIAL_URL)
    euroOficial = formatResponse(euroValues)
    return jsonify(euroOficial)


@ app.route("/api/euro/blue")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getEuroBlue():
    euroValues = getValues(EURO_BLUE_URL)
    euroBlue = formatResponse(euroValues)
    return jsonify(euroBlue)


@ app.route("/api/real/oficial")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getRealOficial():
    realValues = getValues(REAL_OFICIAL_URL)
    realOficial = formatResponse(realValues)
    return jsonify(realOficial)


@ app.route("/api/real/blue")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getRealBlue():
    realValues = getValues(REAL_BLUE_URL)
    realBlue = formatResponse(realValues)
    return jsonify(realBlue)


if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
