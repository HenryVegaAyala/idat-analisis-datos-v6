#!/usr/bin/env python3
import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import pandas as pd

BASE = "https://api.datosabiertos.mef.gob.pe/DatosAbiertos/v1"
RESOURCE_ID = "c275fa9f-5c61-4313-828d-0827277bdd97"
BATCH = 200

COLUMNAS = [
    "CODIGO_UNICO", "NOMBRE_INVERSION", "ESTADO", "PRIMER_DEVENGADO", "ULTIMO_DEVENGADO",
    "DEVENGADO_ACUMULADO", "DEV_AÑO_ACTUAL", "PIM_AÑO_ACTUAL", "FECHA_ULT_ACT_F12B",
    "ULT_PERIODO_REG_F12B", "AVANCE_FISICO", "ULT_ESTADO_SITUACIONAL", "ULT_PROBLEMA",
    "ACC_PROBLEMA", "ULT_FEC_DECLA_ESTIM", "AVANCE_EJECUCION",
    "DEV_ENE_AÑO_VIG", "DEV_FEB_AÑO_VIG", "DEV_MAR_AÑO_VIG", "DEV_ABR_AÑO_VIG",
    "DEV_MAY_AÑO_VIG", "DEV_JUN_AÑO_VIG", "DEV_JUL_AÑO_VIG", "DEV_AGO_AÑO_VIG",
    "DEV_SET_AÑO_VIG", "DEV_OCT_AÑO_VIG", "DEV_NOV_AÑO_VIG", "DEV_DIC_AÑO_VIG",
    "MONTO_ACTUALIZADO_1", "MONTO_ACTUALIZADO_2", "MONTO_ACTUALIZADO_3", "MONTO_ACTUALIZADO_4",
    "MONTO_ACTUALIZADO_5", "MONTO_ACTUALIZADO_6", "MONTO_ACTUALIZADO_7", "MONTO_ACTUALIZADO_8",
    "MONTO_ACTUALIZADO_9", "MONTO_ACTUALIZADO_10", "MONTO_ACTUALIZADO_11", "MONTO_ACTUALIZADO_12",
    "MONTO_PROGRAMADO_1", "MONTO_PROGRAMADO_2", "MONTO_PROGRAMADO_3", "MONTO_PROGRAMADO_4",
    "MONTO_PROGRAMADO_5", "MONTO_PROGRAMADO_6", "MONTO_PROGRAMADO_7", "MONTO_PROGRAMADO_8",
    "MONTO_PROGRAMADO_9", "MONTO_PROGRAMADO_10", "MONTO_PROGRAMADO_11", "MONTO_PROGRAMADO_12",
    "INICIO_EJEC_FISICA", "CULMINA_EJEC_FISICA",
]


def _sql(query, retries=4, pause=1.5):
    url = f"{BASE}/datastore_search_sql?sql=" + urllib.parse.quote(
        query, safe="\"'=()*,", encoding="latin-1", errors="replace"
    )
    for i in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                data = json.loads(r.read().decode("utf-8"))
                return data.get("records") or data.get("result", {}).get("records") or []
        except urllib.error.HTTPError as e:
            if e.code not in (500, 502, 503, 504):
                raise
            time.sleep(pause * (2 ** i))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(pause * (2 ** i))
    raise RuntimeError(f"Fallo tras {retries} intentos")


def descargar(codigos):
    codigos = [str(c).strip() for c in codigos if str(c).strip()]
    filas = []
    for i in range(0, len(codigos), BATCH):
        lote = codigos[i:i + BATCH]
        in_list = ",".join("'" + c.replace("'", "''") + "'" for c in lote)
        filas.extend(_sql(f'SELECT * FROM "{RESOURCE_ID}" WHERE "CODIGO_UNICO" IN ({in_list})'))
        time.sleep(0.2)

    if not filas:
        return pd.DataFrame()

    df = pd.DataFrame(filas)
    df = df[[c for c in COLUMNAS if c in df.columns]]
    orden = {c: i for i, c in enumerate(codigos)}
    return df.iloc[df["CODIGO_UNICO"].map(orden).argsort()].reset_index(drop=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--codigos", required=True)
    p.add_argument("--salida", default="resultado")
    a = p.parse_args()

    salida = a.salida if a.salida.lower().endswith(".xlsx") else a.salida + ".xlsx"
    with open(a.codigos, encoding="utf-8") as fh:
        codigos = [ln.strip() for ln in fh if ln.strip()]

    descargar(codigos).to_excel(salida, index=False)
    print(f"ok -> {salida}")


if __name__ == "__main__":
    main()
