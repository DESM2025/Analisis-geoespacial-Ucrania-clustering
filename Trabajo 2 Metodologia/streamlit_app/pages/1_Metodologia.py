import streamlit as st
from pages.utils.ui_theme import setup_page, stat, hr, badge, highlight, show_img, PROJECT_DIR, PRISMA_IMG

setup_page("Metodología · ScoRBA + PRISMA 2020")

st.markdown("# Metodología")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:1.5rem'>"
    "PRISMA 2020</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

# ── Pregunta de investigación ─────────────────────────────────────────────────
st.markdown("## Pregunta de investigación")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div style='border-left:4px solid #00BCD4;padding:20px 26px;"
    "background:rgba(0,188,212,0.06);border-radius:0 10px 10px 0'>"
    "<p style='color:#00BCD4;font-weight:700;font-size:1rem;margin:0 0 10px 0'>"
    "Pregunta orientadora del estudio</p>"
    "<p style='color:#d0e8f5;font-size:1.05rem;margin:0;line-height:1.7;font-style:italic'>"
    "¿Qué metodologías de análisis geoespacial han sido aplicadas para estudiar los impactos "
    "del conflicto ruso-ucraniano, y cuáles son sus principales hallazgos, limitaciones "
    "y proyecciones futuras?"
    "</p></div>",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

col_obj1, col_obj2 = st.columns(2, gap="large")
with col_obj1:
    st.markdown("**Objetivo general**")
    st.markdown(
        "Sistematizar el estado del arte de las metodologías de análisis geoespacial "
        "aplicadas al conflicto Rusia-Ucrania mediante una revisión de alcance bibliométrica."
    )
with col_obj2:
    st.markdown("**Objetivos específicos**")
    for oe in [
        "Identificar los métodos y tecnologías satelitales más utilizados.",
        "Determinar las regiones con mayor cobertura científica y tipos de impacto documentados.",
        "Identificar limitaciones metodológicas y líneas de investigación futura.",
    ]:
        st.markdown(
            f"<div style='border-left:2px solid rgba(0,188,212,0.4);padding:7px 14px;margin:6px 0;"
            f"background:rgba(0,188,212,0.03);border-radius:0 4px 4px 0'>"
            f"<span style='color:#c0d8ef;font-size:0.93rem'>{oe}</span></div>",
            unsafe_allow_html=True,
        )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Diseño del estudio ────────────────────────────────────────────────────────
st.markdown("## Metodología de revisión bibliométrica")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "Se usó una revisión sistemática de literatura con análisis cuantitativo de la producción científica. "
    "El reporte sigue las directrices **PRISMA 2020** para garantizar transparencia y reproducibilidad."
)
st.markdown("<br>", unsafe_allow_html=True)

col_a, col_b = st.columns(2, gap="large")
with col_a:
    st.markdown("#### Parámetros de búsqueda")
    st.markdown(
        "| Campo | Criterio |\n"
        "|---|---|\n"
        "| Bases de datos | Web of Science · Scopus |\n"
        "| Fecha de búsqueda | 1 de mayo de 2026 |\n"
        "| Período | 2022 – 2026 |\n"
        "| Idioma | Inglés |\n"
        "| Documentos | Artículos · Revisiones · Conferencias |\n"
        "| Herramientas | pybibx · NotebookLM |"
    )

with col_b:
    st.markdown("#### Criterios de inclusión")
    incluidos = [
        "Aplica al menos una técnica de análisis geoespacial o teledetección.",
        "Contexto de aplicación: conflicto Rusia-Ucrania o sus impactos directos.",
        "Publicado en inglés entre 2022 y 2026.",
        "Disponible en texto completo.",
    ]
    for item in incluidos:
        st.markdown(
            f"<div style='border-left:2px solid #00BCD4;padding:8px 14px;margin:6px 0;"
            f"background:rgba(0,188,212,0.04);border-radius:0 4px 4px 0'>"
            f"<span style='color:#c0d8ef;font-size:0.95rem'>{item}</span></div>",
            unsafe_allow_html=True,
        )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Criterios de exclusión")
    excluidos = [
        "Artículos de opinión, editoriales o comentarios sin datos empíricos.",
        "Técnicas geoespaciales mencionadas solo de forma tangencial.",
        "Sin acceso a texto completo.",
        "Estudios duplicados entre bases de datos.",
    ]
    for item in excluidos:
        st.markdown(
            f"<div style='border-left:2px solid #E65100;padding:8px 14px;margin:6px 0;"
            f"background:rgba(230,81,0,0.04);border-radius:0 4px 4px 0'>"
            f"<span style='color:#c0d8ef;font-size:0.95rem'>{item}</span></div>",
            unsafe_allow_html=True,
        )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Cadenas de búsqueda ───────────────────────────────────────────────────────
st.markdown("## Cadenas de búsqueda")
st.markdown(
    "Las palabras clave se organizaron en dos bloques temáticos combinados con AND. "
    "Se ejecutaron dos cadenas: la **Cadena A** en Scopus y WoS, "
    "y la **Cadena B** (variante simplificada) únicamente en WoS."
)
st.markdown("<br>", unsafe_allow_html=True)

tab_ca, tab_cb = st.tabs(["Cadena A — Scopus y WoS", "Cadena B — solo WoS"])

with tab_ca:
    st.markdown("<br>", unsafe_allow_html=True)
    st.code(
        '("Ukraine war" OR "Ukraine conflict" OR\n'
        ' "Russo-Ukrainian war" OR "Russia-Ukraine")\n'
        'AND\n'
        '("spatial analysis" OR "geospatial" OR "GIS" OR\n'
        ' "remote sensing" OR "satellite imagery" OR\n'
        ' "spatial pattern*" OR "geographic information")',
        language="text",
    )

with tab_cb:
    st.markdown("<br>", unsafe_allow_html=True)
    st.code(
        '"Ukraine war" OR "Ukraine conflict" OR "Russo-Ukrainian war"\n'
        'AND\n'
        '"Spatial analysis" OR "Geospatial" OR "GIS" OR "Spatial pattern*"',
        language="text",
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Resultados de la selección ────────────────────────────────────────────────
st.markdown("## Resultados de la selección")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    highlight(
        "La selección se hizo en dos etapas: primero se revisaron <strong>título y abstract</strong>, "
        "y se descartaron estudios sin uso de datos espaciales o centrados solo en política, economia o estrategia militar."
    ),
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4, gap="medium")
with c1: st.markdown(stat("114", "Registros iniciales · Scopus + WoS"),      unsafe_allow_html=True)
with c2: st.markdown(stat("73",  "Tras eliminar 41 duplicados"),              unsafe_allow_html=True)
with c3: st.markdown(stat("39",  "Revisados"),               unsafe_allow_html=True)
with c4: st.markdown(stat("36",  "Estudios incluidos · −3 no disponibles"),   unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Diagrama PRISMA ───────────────────────────────────────────────────────────
st.markdown("## Diagrama PRISMA 2020")
st.markdown("<br>", unsafe_allow_html=True)

if PRISMA_IMG.exists():
    _, col_prisma, _ = st.columns([0.5, 3, 0.5])
    with col_prisma:
        st.image(str(PRISMA_IMG), caption="Diagrama PRISMA 2020 — flujo completo de selección de estudios", use_container_width=True)
else:
    st.markdown(
        highlight(
            "<strong>Identificación</strong> → 114 registros (Scopus 57 + WoS 57)<br><br>"
            "<strong>Eliminación de duplicados</strong> → 73 registros únicos (−41)<br><br>"
            "<strong>Revisión a texto completo</strong> → 39 elegibles (−34 descartados por relevancia)<br><br>"
            "<strong>Incluidos</strong> → 36 estudios (−3 no disponibles en acceso abierto)"
        ),
        unsafe_allow_html=True,
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Análisis bibliométrico ────────────────────────────────────────────────────
st.markdown("## Análisis bibliométrico")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "Con los 36 estudios incluidos se realizó un análisis usando **pybibx** "
    "sobre los archivos exportados en formato BibTeX desde Scopus y WoS: "
    "producción anual, citas acumuladas, redes de co-autoría, palabras clave más frecuentes "
    "y distribución geográfica de las instituciones de los autores."
)
st.markdown("<br>", unsafe_allow_html=True)
herramientas = ["pybibx", "NotebookLM", "Web of Science", "Scopus", "PRISMA 2020", "ScoRBA", "Google Collab"]
st.markdown(" ".join(badge(h) for h in herramientas), unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Diagrama Sankey ───────────────────────────────────────────────────────────
st.markdown("## Relaciones entre autores, países e idiomas")
st.markdown(
    "El diagrama Sankey generado con pybibx muestra las relaciones entre los autores más productivos "
    "del corpus, los países de afiliación y el idioma de publicación de los estudios seleccionados."
)
st.markdown("<br>", unsafe_allow_html=True)
show_img("sankey.png", "Diagrama Sankey — autores · países · idiomas del corpus")
