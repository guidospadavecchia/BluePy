from decimal import Decimal


def convertToDecimal(value):
    try:
        return Decimal(value)
    except ValueError:
        return Decimal(0)
    except Exception:
        return Decimal(0)
