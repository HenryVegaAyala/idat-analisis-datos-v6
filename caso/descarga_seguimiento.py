#!/usr/bin/env python3
import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import pandas as pd

BASE = "https://api.datosabiertos.mef.gob.pe/DatosAbiertos/v1"
RESOURCE_ID = "49d960a8-54cf-4a45-8ebe-d8074ac88877"
PAGE = 32000

COLUMNAS = [
    "ANO_EJE", "NIVEL_GOBIERNO", "NIVEL_GOBIERNO_NOMBRE", "SECTOR", "SECTOR_NOMBRE",
    "PLIEGO", "PLIEGO_NOMBRE", "SEC_EJEC", "EJECUTORA", "EJECUTORA_NOMBRE",
    "DEPARTAMENTO_EJECUTORA", "DEPARTAMENTO_EJECUTORA_NOMBRE", "PROVINCIA_EJECUTORA",
    "PROVINCIA_EJECUTORA_NOMBRE", "DISTRITO_EJECUTORA", "DISTRITO_EJECUTORA_NOMBRE",
    "TIPO_ACT_PROY", "TIPO_ACT_PROY_NOMBRE", "PRODUCTO_PROYECTO", "PRODUCTO_PROYECTO_NOMBRE",
    "FUNCION", "FUNCION_NOMBRE", "DEPARTAMENTO_META", "DEPARTAMENTO_META_NOMBRE",
    "FUENTE_FINANCIAMIENTO", "FUENTE_FINANCIAMIENTO_NOMBRE", "RUBRO", "RUBRO_NOMBRE",
    "MONTO_EJECUCION_HASTA_HACE_2_ANOS", "MONTO_EJECUCION_ANO_ANTERIOR", "MONTO_PIA",
    "MONTO_PIM", "MONTO_DEVENGADO_ANO_EJE", "MONTO_EJECUCION_TOTAL", "PKBZfrKt", "COSTO_ACTUAL",
]


def _fetch(url, intentos=8, pausa=0.6):
    ultimo = None
    for i in range(intentos):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            ultimo = f"HTTP {e.code}"
            if e.code in (500, 502, 503, 504):
                time.sleep(pausa * (i + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            ultimo = str(e)
            time.sleep(pausa * (i + 1))
    raise RuntimeError(f"Fallo tras {intentos} intentos: {ultimo}")


def _buscar(columna, valor, offset):
    filtros = urllib.parse.quote(json.dumps({columna: valor}))
    d = _fetch(f"{BASE}/datastore_search?resource_id={RESOURCE_ID}"
               f"&filters={filtros}&limit={PAGE}&offset={offset}")
    return d.get("records") or d.get("result", {}).get("records") or []


def descargar(columna, valor):
    filas, offset = [], 0
    while True:
        recs = _buscar(columna, valor, offset)
        if not recs:
            break
        filas.extend(recs)
        offset += len(recs)
        if len(recs) < PAGE:
            break
        time.sleep(0.3)
    df = pd.DataFrame(filas)
    if df.empty:
        return df
    return df[[c for c in COLUMNAS if c in df.columns]].reset_index(drop=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--valor", default="MUNICIPALIDAD PROVINCIAL DEL CUZCO")
    p.add_argument("--salida", default="resultado")
    a = p.parse_args()

    salida = a.salida if a.salida.lower().endswith(".xlsx") else a.salida + ".xlsx"
    df = descargar("EJECUTORA_NOMBRE", a.valor)
    df.to_excel(salida, index=False)
    print(f"ok -> {salida}")


if __name__ == "__main__":
    main()
