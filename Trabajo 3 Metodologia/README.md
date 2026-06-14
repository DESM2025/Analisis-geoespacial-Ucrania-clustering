# Correspondencia Espacial entre Clústeres de Intensidad de Combate y Daño Satelital en el Conflicto Ruso-Ucraniano

App en Streamlit que acompaña el informe del Trabajo 3 (Metodología de Investigación en Ciencia de Datos, UTEM). Aplica K-Means y DBSCAN sobre datos georreferenciados de ACLED (2022-2026) para identificar clústeres de combate y compararlos con daño documentado satelitalmente en el conflicto ruso-ucraniano.

## Estructura

- `Portada.py` — Portada
- `pages/1_Estado_del_Arte.py` — Estado del arte
- `pages/2_Pregunta_e_Hipotesis.py` — Pregunta e hipótesis
- `pages/3_Objetivos.py` — Objetivo general y objetivos específicos
- `pages/4_Coherencia_y_Cierre.py` — Coherencia y cierre
- `Informe_Trabajo3_Silva.docx` — Informe escrito

## Instalación

**Opción A — conda (recomendada):**

```bash
conda env create -f environment.yml
conda activate proyecto-ocde
```

**Opción B — pip:**

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run Portada.py
```

La app se abre en `http://localhost:8501`.
