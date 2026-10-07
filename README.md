# Bitácora Académica

Guía de consulta, **no oficial**, sobre reglamentos, plazos, trámites y responsables de pregrado para la Escuela de Comunicaciones y Periodismo de la Universidad Adolfo Ibáñez (UAI).

Este proyecto es independiente y no es un sitio oficial de la UAI. La información está actualizada al 7 de octubre de 2026. Si hay diferencias, prima el documento oficial y lo que indique la Secretaría Académica.

## Contenido

- `index.html`: el sitio. Es un solo archivo, sin dependencias de compilación.
  - Asistente: busca respuestas en la normativa recopilada. En GitHub Pages funciona como búsqueda local.
  - Trámites y plazos: los próximos plazos del Calendario Académico 2026 y 15 trámites con sus requisitos, quién resuelve y la norma.
  - Organigrama funcional, construido a partir de los reglamentos.
  - Documentos: catálogo de 51 fuentes oficiales con su estado de vigencia.
- `data/`: la base de datos del sitio.
  - `base_normativa_uai_fcom_2026-10-07.md`: la normativa resumida y citada por artículo.
  - `catalogo_documentos_uai_fcom.csv` / `.json`: el catálogo de fuentes, con URL, alcance, fecha de versión y estado.
  - `descargar_corpus.py`: descarga los PDF del catálogo y extrae su texto, para actualizar la base.
- `assets/`: favicon de la UAI.

## Fuentes principales

- [Reglamento de los Programas de Pregrado 2026](https://uai.cdn7pm.net/documentos/reglamento-programas-de-pregrado-2026.pdf)
- [Calendario Académico 2026](https://uai.cdn7pm.net/documentos/calendario-academico-uai-2026.pdf)
- [Reglamento de Homologaciones y Convalidaciones](https://uai.cdn7pm.net/documentos/reglamento-de-homologaciones-y-convalidaciones-2025.pdf)
- [Escuela de Comunicaciones y Periodismo](https://www.uai.cl/comunicaciones)
- [Portal de estudiantes UAI](https://alumno.uai.cl/)

## Cómo actualizar

1. Vuelve a ejecutar `data/descargar_corpus.py` con el catálogo para descargar y comparar las versiones de los documentos.
2. Actualiza la base normativa y el catálogo.
3. Vuelve a insertar ambos en `index.html`, en los bloques `<script id="kb">` y `<script id="catalog">`.

## Marca

El logotipo y el favicon son propiedad de la Universidad Adolfo Ibáñez. Su uso en este prototipo debe validarse con la Dirección de Marketing y Posicionamiento de la UAI según la [Guía de Identidad de Marca y Comunicación](https://uai.cdn7pm.net/documentos/manual-corporativo-uai.pdf). El diseño está inspirado en el lenguaje editorial del MIT Media Lab.
