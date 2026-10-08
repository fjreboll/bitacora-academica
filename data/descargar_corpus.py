#!/usr/bin/env python3
"""Descarga los documentos del catálogo UAI/FCOM y extrae su texto.

Uso (en tu computador, con conexión a uai.cl):
    pip install requests pypdf
    python3 descargar_corpus.py catalogo_documentos_uai_fcom.json salida/

Genera: salida/pdf/<id>.pdf, salida/txt/<id>.txt y salida/manifest.csv
(con estado HTTP, Last-Modified, bytes y SHA-256 para detectar cambios en
futuras ejecuciones).
"""
import csv, hashlib, json, sys, pathlib, requests
from pypdf import PdfReader

cat, out = sys.argv[1], pathlib.Path(sys.argv[2])
(out / "pdf").mkdir(parents=True, exist_ok=True)
(out / "txt").mkdir(parents=True, exist_ok=True)
docs = json.load(open(cat, encoding="utf-8"))["documentos"]
rows = []
for d in docs:
    url, did = d["url"], d["id"]
    try:
        r = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        ctype = r.headers.get("content-type", "")
        row = {"id": did, "url": url, "status": r.status_code, "content_type": ctype,
               "last_modified": r.headers.get("last-modified", ""), "bytes": len(r.content),
               "sha256": hashlib.sha256(r.content).hexdigest()}
        if r.ok and "pdf" in ctype:
            p = out / "pdf" / f"{did}.pdf"; p.write_bytes(r.content)
            text = "\n\n".join((pg.extract_text() or "") for pg in PdfReader(p).pages)
            (out / "txt" / f"{did}.txt").write_text(text, encoding="utf-8")
        elif r.ok:
            (out / "txt" / f"{did}.html").write_text(r.text, encoding="utf-8")
    except Exception as e:
        row = {"id": did, "url": url, "status": f"error: {e}"}
    rows.append(row); print(did, row.get("status"))
with open(out / "manifest.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id", "url", "status", "content_type", "last_modified", "bytes", "sha256"])
    w.writeheader(); w.writerows(rows)
