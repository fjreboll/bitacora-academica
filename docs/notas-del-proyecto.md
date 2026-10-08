# Notas del proyecto

Bitácora Académica es una guía no oficial sobre reglamentos, plazos, trámites y responsables de pregrado para la Escuela de Comunicaciones y Periodismo de la UAI. Está dirigida a estudiantes, docentes, equipos administrativos y autoridades.

- Sitio: https://fjreboll.github.io/bitacora-academica/
- Corte de la información: 7 de octubre de 2026. La sección de cohortes se agregó el 8 de octubre de 2026.

## Estructura del sitio

1. **Inicio:** título, la pregunta "¿En qué año ingresaste a la UAI?", el buscador y tres preguntas sugeridas.
2. **Asistente ("Pregúntale a la Bitácora"):** responde solo con la normativa recopilada y cita el documento y el artículo. En GitHub Pages funciona como búsqueda local. La versión con IA funciona dentro de Claude.
3. **Trámites y plazos:**
   - La cohorte elegida.
   - Los próximos 5 plazos del Calendario Académico 2026.
   - 15 trámites con sus requisitos, quién resuelve y la norma.
4. **Organigrama funcional:** construido a partir de los reglamentos; no reemplaza al organigrama oficial. Incluye las secretarias de pregrado según la inicial del apellido.
5. **Documentos:** el catálogo de 55 fuentes oficiales, con filtros por estado y por cohorte.

## Año de ingreso (cohorte)

El Reglamento de Pregrado 2026 aplica a todo el pregrado. El art. 70 establece que quienes ingresaron antes de 2026 conservan el reglamento de su cohorte en lo que les sea más favorable.

| Año de ingreso | Reglamentos que muestra el sitio |
|---|---|
| 2026 o después | Reglamento 2026 (UAI-REG-01) y Reglamento de Homologaciones (UAI-REG-03) |
| 2025 | Reglamento 2026 + Licenciaturas y Bachilleratos 2025, D.A. 16-2025 (UAI-REG-02) + Homologaciones |
| 2024 | Reglamento 2026 + Licenciaturas y Bachilleratos 2024, D.A. 6/2024 (folleto 2024, UAI-REG-07) + Homologaciones |
| 2023 o antes | Reglamento 2026 + folletos de reglamentos 2023, 2022 y 2021 (UAI-REG-08 a 10) |

La opción "Atiendo estudiantes" recuerda verificar el año de ingreso del estudiante antes de aplicar una regla. La elección se guarda solo en el navegador de cada persona.

## Decisiones de diseño

- **Referente:** el lenguaje editorial del MIT Media Lab.
  - Barra lateral fija con la navegación en negrita.
  - Tipografía grotesca (Inter Tight) con titulares de interlineado cerrado.
  - Sin bordes redondeados ni sombras; reglas negras de 2 px; tooltips negros.
- **Color:** blanco, el negro y los grises de la UAI, con el celeste institucional como único acento. No se usa rojo en fondos ni textos.
- **Redacción:** mayúscula solo al inicio de oración, trato de "tú" y botones con verbo.
- **Marca:**
  - Logo y favicon de la UAI en la esquina superior izquierda, con la etiqueta "Prototipo no oficial".
  - El sitio está marcado con `noindex` para que no aparezca en buscadores.

## Pendiente

- Revisar el contenido de los folletos 2021–2024 para detallar las diferencias por cohorte.
- Confirmar con la Escuela desde qué cohorte rige el plan de la Licenciatura en Comunicación con plan común de 3 años.
- Conseguir el protocolo de titulación de la Escuela, las reglas de práctica y los requisitos del Magíster en Comunicación e Innovación.
- Precisar las fechas del calendario por día, porque hoy se muestran por semana.
- Validar el uso de la marca con la Dirección de Marketing y Posicionamiento de la UAI.
- Implementar un asistente con IA en la versión web, lo que requiere un servicio propio.

## Cómo actualizar

1. Ejecuta `data/descargar_corpus.py` con el catálogo para descargar los documentos y detectar cambios.
2. Actualiza la base normativa y el catálogo en `data/`.
3. Vuelve a insertar ambos en `index.html`, en los bloques `<script id="kb">` y `<script id="catalog">`.
