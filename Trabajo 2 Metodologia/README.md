# Revisión Bibliométrica: Metodologías Geoespaciales en el Conflicto Ruso-Ucraniano

Trabajo 2 de Metodología de Investigación en Ciencia de Datos (UTEM). El entregable principal es el **informe de revisión bibliográfica** (scoping review bajo PRISMA 2020 + protocolo ScoRBA) sobre 36 artículos (Scopus + Web of Science) que aplican teledetección al conflicto ruso-ucraniano. La app de Streamlit es un complemento interactivo que resume ese mismo análisis.

## Estructura

- **`Trabajo_2_Metodologia.pdf`** — informe final (el entregable principal de este trabajo)
- **`Trabajo_2_Metodologia/`** — fuente LaTeX del informe (`main.tex`). Incluye copias propias de `Capturas/`, `Logo-UTEM-1.png` y `prisma.png` porque LaTeX necesita esos archivos junto al `.tex` para compilar; son las mismas imágenes que las de la raíz de esta carpeta, solo duplicadas para que el LaTeX sea autocontenido
- **`papers/`** — metadata y seguimiento de los 36 artículos revisados:
  - `savedrecs.bib` / `scopus_export_*.bib` — exports bibliográficos de Web of Science y Scopus
  - `mis_articulos.xlsx` / `articulos_finales_ucrania.xlsx` — planillas de seguimiento/selección de artículos
  - `sin papers.txt` — artículos descartados o no disponibles (de pago, sin acceso, etc.) durante la selección
  - Los PDF de los 36 artículos **no se incluyen en el repo** (varios son de editoriales de pago como Elsevier/Science y el repo es público); se mantienen solo localmente. El listado y referencias completas están en los `.bib` y en `articulos_finales_ucrania.xlsx`
- **`prisma/`** y **`prisma.png`** — diagrama de flujo PRISMA del proceso de selección (versiones html/pdf/png)
- **`Capturas/`** — capturas de pantalla de los análisis bibliométricos, usadas en el informe y la app
- **`Logo-UTEM-1.png`** — logo institucional
- **`streamlit_app/`** — versión interactiva (opcional), complementaria al informe:
  - `app.py` — portada / contexto y objetivo
  - `pages/1_Metodologia.py` — pregunta de investigación y protocolo (PRISMA/ScoRBA)
  - `pages/2_Bibliometria.py` — análisis bibliométrico (evolución temporal, autores, fuentes, etc.)
  - `pages/3_Resultados.py` — resultados (métodos de análisis geoespacial identificados)
  - `pages/4_Discusion.py` — discusión y patrones metodológicos transversales
  - `pages/5_Conclusiones.py` — conclusiones y hallazgos principales
  - `pages/6_Articulos.py` — listado de los 36 artículos incluidos en la revisión
  - `pages/8_Referencias_IA.py` — referencias y declaración de uso de IA

## Ejecutar la versión interactiva (opcional)

```bash
pip install -r streamlit_app/requirements.txt
cd streamlit_app
streamlit run app.py
```

La app se abre en `http://localhost:8501`.
