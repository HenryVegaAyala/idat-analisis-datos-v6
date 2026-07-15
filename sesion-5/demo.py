import requests

url = "https://fs.datosabiertos.mef.gob.pe/datastorefiles/2021-Gasto.csv"
local_path = "2021-Gasto.csv"

with requests.get(url, stream=True) as r:
    r.raise_for_status()
    total = int(r.headers.get('content-length', 0))
    descargado = 0
    with open(local_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8 * 1024 * 1024):  # 8MB
            f.write(chunk)
            descargado += len(chunk)
            print(f"\r{descargado / 1e9:.2f} GB / {total / 1e9:.2f} GB", end="")

print(f"\n✅ Archivo CSV guardado en: {local_path}")
