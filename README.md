# Análisis Geoespacial del Conflicto Ruso-Ucraniano

**Asignatura:** Metodología de Investigación para Ciencia de Datos

**Autor:** Diego Ernesto Silva Madariaga

**Institución:** Universidad Tecnológica Metropolitana (UTEM), Facultad de Ingeniería, Ingeniería Civil en Ciencia de Datos

**Semestre:** Primer Semestre 2026

## Descripción general

Este repositorio reúne los avances de un mismo proyecto de investigación, desarrollado de forma incremental a lo largo del curso. El hilo conductor es el uso de técnicas de Ciencia de Datos (clustering espacial no supervisado) para analizar la correspondencia entre la intensidad del combate y el daño documentado satelitalmente en el conflicto ruso-ucraniano (2022-presente).

Cada carpeta corresponde a una entrega del curso y construye sobre la anterior:

| Carpeta | Entrega | Contenido |
|---|---|---|
| [`Trabajo 1 Metodologia/`](./Trabajo%201%20Metodologia) | Planteamiento del problema | Define el área OCDE (Geografía), la motivación, la descripción del problema y la relevancia. Identifica el problema de sobrecarga de datos geoespaciales y propone clustering (K-Means/DBSCAN) sobre datos ACLED/UCDP como enfoque metodológico. Incluye notebook exploratorio y scripts de descarga de datos. |
| [`Trabajo 2 Metodologia/`](./Trabajo%202%20Metodologia) | Revisión bibliométrica | Revisión de alcance (scoping review) bajo PRISMA 2020 + protocolo ScoRBA sobre metodologías de teledetección aplicadas al conflicto (36 artículos, Scopus + WoS). Concluye identificando como brecha el uso de clustering espacial sobre registros ACLED, propuesto como trabajo futuro. |
| [`Trabajo 3 Metodologia/`](./Trabajo%203%20Metodologia) | Propuesta de investigación | Formaliza la brecha identificada en el Trabajo 2: pregunta de investigación, hipótesis correlacional y objetivos específicos (Datos → Método → Evaluación → Interpretación) para aplicar K-Means/DBSCAN sobre ACLED (2022-2026) y compararlo con el daño satelital documentado en la literatura. |
| `Trabajo 4 Metodologia/` *(próximamente)* | Aplicación del clustering | Implementación y evaluación del clustering propuesto en el Trabajo 3 (K-Means/DBSCAN, coeficiente de silueta, índice de Davies-Bouldin) y análisis de correspondencia espacial con el daño satelital. |

## Estructura de cada carpeta

Cada `Trabajo N Metodologia/` es un proyecto autocontenido: tiene su propia app de Streamlit (multipágina), su propio archivo de entorno (`environment.yml` y/o `requirements.txt`) y, cuando corresponde, sus datos, notebooks e informes.

**No es necesario clonar/descargar el repositorio completo para revisar un trabajo puntual.** Basta con esa carpeta: incluye su propio `environment.yml`/`requirements.txt` para instalarse y ejecutarse de forma independiente.

## Entornos de ejecución

Todos los trabajos comparten el mismo entorno conda, **`proyecto-ocde`** (Python 3.11 + Streamlit).

- **Para revisar un solo trabajo:** usa el `environment.yml`/`requirements.txt` de esa carpeta — son autosuficientes.
- **Para trabajar con todo el repo:** el `environment.yml`/`requirements.txt` de la raíz tiene la unión de todas las dependencias, así se crea el entorno una sola vez y sirve para los tres (futuro cuarto) trabajos:

```bash
conda env create -f environment.yml
conda activate proyecto-ocde
```

Alternativa con pip:

```bash
pip install -r requirements.txt
```

`Trabajo 1 Metodologia/` además requiere un archivo `.env` con credenciales ACLED/UCDP (ver `Trabajo 1 Metodologia/.env.example`).

### Ejecutar una app

Desde la carpeta del trabajo correspondiente:

```bash
streamlit run app.py        # Trabajo 1
streamlit run app.py         # Trabajo 2 (dentro de streamlit_app/)
streamlit run Portada.py     # Trabajo 3
```

La app se abre en `http://localhost:8501`.

## Notas

- Las credenciales (`.env`) nunca se incluyen en el repositorio (ver `.gitignore`).
- Los entornos virtuales (`.venv/`) y cachés de Python no se versionan; cada quien debe crear su propio entorno con los archivos indicados arriba.
