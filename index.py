import os
import tiempo_financiero
import monitor_dolar_venezuela
from flask import Flask, send_from_directory, jsonify
from flask_caching import Cache

VERSION = "1.1"
CACHE_TIMEOUT_SECONDS = os.getenv('CACHE_TIMEOUT', 3600)
GIT_REPO_URL = 'https://github.com/guidospadavecchia/BluePy'

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
    dolarValues = tiempo_financiero.getDolarOficial()
    dolarOficial = tiempo_financiero.formatResponse(dolarValues)
    return jsonify(dolarOficial)


@ app.route("/api/dolar/blue")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getDolarBlue():
    dolarValues = tiempo_financiero.getDolarBlue()
    dolarBlue = tiempo_financiero.formatResponse(dolarValues)
    return jsonify(dolarBlue)


@ app.route("/api/euro/oficial")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getEuroOficial():
    euroValues = tiempo_financiero.getEuroOficial()
    euroOficial = tiempo_financiero.formatResponse(euroValues)
    return jsonify(euroOficial)


@ app.route("/api/euro/blue")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getEuroBlue():
    euroValues = tiempo_financiero.getEuroBlue()
    euroBlue = tiempo_financiero.formatResponse(euroValues)
    return jsonify(euroBlue)


@ app.route("/api/real/oficial")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getRealOficial():
    realValues = tiempo_financiero.getRealOficial()
    realOficial = tiempo_financiero.formatResponse(realValues)
    return jsonify(realOficial)


@ app.route("/api/real/blue")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getRealBlue():
    realValues = tiempo_financiero.getRealBlue()
    realBlue = tiempo_financiero.formatResponse(realValues)
    return jsonify(realBlue)


@ app.route("/api/venezuela/dolar/oficial")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getVenezuelaOficialRate():
    valueOficial = monitor_dolar_venezuela.getOficial()
    response = monitor_dolar_venezuela.formatResponse(valueOficial)
    return jsonify(response)


@ app.route("/api/venezuela/dolar/paralelo")
@ cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getVenezuelaParaleloRate():
    valueParalelo = monitor_dolar_venezuela.getParalelo()
    response = monitor_dolar_venezuela.formatResponse(valueParalelo)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
