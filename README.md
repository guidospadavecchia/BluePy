<p align="center">
  <img src="https://github.com/guidospadavecchia/BluePy/blob/main/static/icon.png">
</p>

---

<p align="center">
  <i>Cotizaciones blue de Dólar, Euro y Real</i>
</p>

## Endpoints

### Dólar

| Método | Endpoint           | Descripción                                    |
| ------ | ------------------ | ---------------------------------------------- |
| GET    | /api/dolar/oficial | Cotización del dólar oficial                   |
| GET    | /api/dolar/blue    | Cotización dólar blue                          |
| GET    | /api/dolar/turista | Cotización del dólar turista                   |
| GET    | /api/dolar/mep     | Cotización dólar MEP (Bolsa)                   |
| GET    | /api/dolar/ccl     | Cotización dólar CCL (Contado con Liquidación) |

### Euro

| Método | Endpoint          | Descripción                 |
| ------ | ----------------- | --------------------------- |
| GET    | /api/euro/oficial | Cotización del Euro oficial |
| GET    | /api/euro/blue    | Cotización Euro blue        |
| GET    | /api/euro/tarjeta | Cotización Euro tarjeta     |

### Real

| Método | Endpoint          | Descripción                 |
| ------ | ----------------- | --------------------------- |
| GET    | /api/real/oficial | Cotización del Real oficial |
| GET    | /api/real/blue    | Cotización Real blue        |

#### Respuesta

```javascript
{
    fecha: "2021/06/30 23:26:42",
    compra: "165.41",
    venta: "172.63"
}
```

### Venezuela

| Método | Endpoint                | Descripción                               |
| ------ | ----------------------- | ----------------------------------------- |
| GET    | /api/venezuela/oficial  | Cotización del par bolivar-dólar oficial  |
| GET    | /api/venezuela/paralelo | Cotización del par bolivar-dólar paralelo |

#### Respuesta

```javascript
{
    fecha: "2021/06/30 23:26:42",
    oficial: "32.15",
    paralelo: "33.10"
}
```

### Otros

| Método | Endpoint  | Descripción                               |
| ------ | --------- | ----------------------------------------- |
| GET    | /api/ping | Devuelve '_pong_' si el sitio está activo |

## Licencia

Este proyecto es **_100% libre y open-source_**. Está licenciado bajo la [MIT License](https://github.com/guidospadavecchia/BluePy/blob/main/LICENSE).

---

\*_Datos recopilados de https://tiempofinanciero.com.ar/cotizaciones_
