import util
import pyDolarVenezuela as pdv
from datetime import datetime


def getValues():
    monitor = pdv.Monitor()
    values = monitor.get_value_monitors()
    return values


def getOficial():
    monitor = pdv.Monitor()
    value_bancamiga = monitor.get_value_monitors(
        monitor_code='bancamiga', name_property='price'
    )
    value_banco_de_venezuela = monitor.get_value_monitors(
        monitor_code='banco_de_venezuela', name_property='price'
    )
    value_banco_exterior = monitor.get_value_monitors(
        monitor_code='banco_exterior', name_property='price'
    )
    value_banesco = monitor.get_value_monitors(
        monitor_code='banesco', name_property='price'
    )
    value_bbva_provincial = monitor.get_value_monitors(
        monitor_code='bbva_provincial', name_property='price'
    )
    value_bcv = monitor.get_value_monitors(
        monitor_code='bcv', name_property='price'
    )
    value_bnc = monitor.get_value_monitors(
        monitor_code='bnc', name_property='price'
    )

    prices = [
        util.convertToDecimal(value_bancamiga),
        util.convertToDecimal(value_banco_de_venezuela),
        util.convertToDecimal(value_banco_exterior),
        util.convertToDecimal(value_banesco),
        util.convertToDecimal(value_bbva_provincial),
        util.convertToDecimal(value_bcv),
        util.convertToDecimal(value_bnc),
    ]
    valores = [n for n in prices if n > 0]
    return sum(valores) / len(valores)


def getParalelo():
    monitor = pdv.Monitor()
    value_enparalelovzla = monitor.get_value_monitors(
        monitor_code='enparalelovzla', name_property='price'
    )
    value_dolartoday = monitor.get_value_monitors(
        monitor_code='dolartoday', name_property='price'
    )
    value_monitor = monitor.get_value_monitors(
        monitor_code='monitor_dolar_venezuela', name_property='price'
    )

    prices = [
        util.convertToDecimal(value_enparalelovzla),
        util.convertToDecimal(value_dolartoday),
        util.convertToDecimal(value_monitor),
    ]
    valores = [n for n in prices if n > 0]
    return sum(valores) / len(valores)


def formatResponse(value):
    return {
        "fecha": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "valor": '{:.2f}'.format(value)
    }
