import streamlit as st
from pages.utils.ui_theme import setup_page, stat, hr, badge, highlight

setup_page("Conclusiones · Síntesis y trabajo futuro")

st.markdown("# Conclusiones")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:1.5rem'>"
    "Síntesis · Aportes · Trabajo futuro propuesto</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

# ── Hallazgos ─────────────────────────────────────────────────────────────────
st.markdown("## Hallazgos principales")
st.markdown(
    "La revisión de 36 artículos publicados entre 2022 y 2026 permite establecer "
    "cuatro conclusiones centrales sobre el uso del análisis geoespacial en el conflicto."
)
st.markdown("<br>", unsafe_allow_html=True)

conclusiones = [
    ("#00BCD4",
     "Sentinel y VIIRS como base de casi todo",
     "En los 36 estudios, Sentinel (ESA) y VIIRS (NASA) aparecen en casi todos. "
     "No porque sean los únicos disponibles, sino porque su combinación cubre lo que "
     "ninguno logra solo: el SAR pasa nubes, el óptico da detalle espectral, "
     "el VIIRS captura lo que pasa de noche."),
    ("#0288D5",
     "Los impactos agrícolas y ambientales, los más medidos",
     "El abandono de tierras (~2.4 M ha), la caída en rendimientos de girasol y trigo, "
     "los incendios y la destrucción de la presa Kajovka son los efectos con más evidencia "
     "satelital. Ucrania produce el 10% del trigo mundial, lo que le da escala global "
     "a ese daño agrícola."),
    ("#4527A0",
     "Lo que se desarrolló en Ucrania funciona en otros conflictos",
     "CCD, modelado contrafactual, fusión multisensor: son marcos que no dependen del contexto "
     "ucraniano. Ya se están discutiendo aplicaciones en Sudán, Gaza y Myanmar. "
     "Ucrania se convirtió en el caso de prueba metodológica para la ciencia de crisis."),
]

for color, titulo, desc in conclusiones:
    st.markdown(
        f"<div style='"
        f"border-left:4px solid {color};"
        f"background:rgba(255,255,255,0.025);"
        f"border-radius:0 10px 10px 0;"
        f"padding:22px 26px;margin:14px 0'>"
        f"<p style='color:{color};font-weight:700;font-size:1.05rem;margin:0 0 8px 0'>{titulo}</p>"
        f"<p style='color:#9bbdd4;font-size:0.95rem;margin:0;line-height:1.65'>{desc}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Cifras de cierre ──────────────────────────────────────────────────────────
st.markdown("## Cifras del estudio")
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4, gap="medium")
with c1: st.markdown(stat("36",             "artículos analizados en total"),      unsafe_allow_html=True)
with c2: st.markdown(stat("2022–2026",       "período analizado (post-invasión)"), unsafe_allow_html=True)
with c3: st.markdown(stat("5 sensores",      "plataformas satelitales dominantes"),unsafe_allow_html=True)
with c4: st.markdown(stat("PRISMA",   "protocolo metodológico aplicado"),   unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Brecha identificada ───────────────────────────────────────────────────────
st.markdown("## Brecha identificada en la literatura")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "A pesar del volumen y la calidad de los estudios revisados, el análisis sistemático "
    "reveló una ausencia dentro de los papers revisados: **ninguno de los 36 aplica "
    "técnicas de agrupamiento espacial sobre los propios eventos de combate**."
)
st.markdown("<br>", unsafe_allow_html=True)

b1, b2 = st.columns(2, gap="large")
with b1:
    st.markdown(
        "<div style='border-left:4px solid rgba(0,188,212,0.5);padding:18px 20px;"
        "background:rgba(0,188,212,0.03);border-radius:0 8px 8px 0'>"
        "<p style='color:#00BCD4;font-weight:600;margin:0 0 8px 0'>Lo que los papers SÍ hacen</p>"
        "<p style='color:#9bbdd4;font-size:0.93rem;margin:0;line-height:1.6'>"
        "Detectar daño satelitalmente: edificios destruidos, tierras abandonadas, "
        "cortes de luz, contaminación. Todos los estudios parten del satélite "
        "hacia el terreno."
        "</p></div>",
        unsafe_allow_html=True,
    )

with b2:
    st.markdown(
        "<div style='border-left:4px solid rgba(206,147,216,0.6);padding:18px 20px;"
        "background:rgba(123,31,162,0.04);border-radius:0 8px 8px 0'>"
        "<p style='color:#CE93D8;font-weight:600;margin:0 0 8px 0'>No encontrado en los papers revisados</p>"
        "<p style='color:#9bbdd4;font-size:0.93rem;margin:0;line-height:1.6'>"
        "Ningún paper del corpus agrupa los eventos de combate en tierra para "
        "identificar zonas de concentración de ataques ni construye un índice "
        "de peligro para la población civil."
        "</p></div>",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    highlight(
        "Esta brecha es la que motiva el análisis propio propuesto: usar datos de "
        "<strong>ACLED</strong> con técnicas de <strong>clustering espacial (K-Means, DBSCAN)</strong> "
        "para mapear la intensidad del conflicto desde los eventos en tierra "
    ),
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Trabajo futuro ────────────────────────────────────────────────────────────
st.markdown("## Trabajo futuro propuesto")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    highlight(
        "<strong>Clustering espacial de eventos de bombardeo</strong> — Aplicar K-Means sobre "
        "datos georreferenciados de ACLED para identificar zonas de concentración de ataques "
        "y caracterizar patrones espaciales de intensidad del conflicto a escala de oblast."
    ),
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

futuro_items = [
    ("Extensión comparativa a otros conflictos",
     "Aplicar el mismo protocolo ScoRBA a Sudán, Gaza y Myanmar para construir una base de "
     "conocimiento comparada sobre análisis geoespacial en conflictos armados contemporáneos."),
]

for titulo, desc in futuro_items:
    st.markdown(
        f"<div style='"
        f"border-left:2px solid rgba(0,188,212,0.4);"
        f"padding:16px 20px;margin:10px 0;"
        f"background:rgba(0,188,212,0.02);border-radius:0 6px 6px 0'>"
        f"<p style='color:#d0e8f5;font-weight:600;font-size:0.98rem;margin:0 0 5px 0'>{titulo}</p>"
        f"<p style='color:#7aadcc;font-size:0.9rem;margin:0;line-height:1.55'>{desc}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Términos ─────────────────────────────────────────────────────────────────────────────
st.markdown("### Términos del estudio")
st.markdown("<br>", unsafe_allow_html=True)
terminos = [
    "Análisis geoespacial", "Teledetección", "SAR", "Sentinel-1",
    "VIIRS", "ScoRBA", "PRISMA 2020", "Machine Learning",
    "Conflicto armado", "Ucrania", "Abandono de tierras",
    "Daño urbano", "Luz nocturna", "Google Earth Engine",
    "Fusión multisensor", "Modelado contrafactual",
]
st.markdown(" ".join(badge(t) for t in terminos), unsafe_allow_html=True)
