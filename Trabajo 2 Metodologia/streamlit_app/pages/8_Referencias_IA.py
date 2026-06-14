import streamlit as st
from pages.utils.ui_theme import setup_page, hr, badge, highlight

setup_page("Referencias · Declaración de IA · Material suplementario")

st.markdown("# Referencias y uso de IA ")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:1.5rem'>"
    "Referencias principales · Declaración de uso de IA · Acceso al suplementario</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

# ── Declaración de uso de IA ──────────────────────────────────────────────────
st.markdown("## Declaración de uso de Inteligencia Artificial")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='border:1px solid rgba(0,188,212,0.25);border-top:3px solid #00BCD4;"
    "border-radius:8px;padding:26px 28px;background:rgba(0,188,212,0.04)'>"
    "<p style='color:#d0e8f5;font-size:1rem;line-height:1.72;margin:0'>"
    "Durante la elaboración de este trabajo se utilizó el modelo "
    "<strong style='color:#00BCD4'>Claude Sonnet 4.6</strong> (Anthropic, 2026), "
    "accedido a través de la aplicación de escritorio, como herramienta de apoyo en "
    "estructuración y redacción del texto en LaTeX "
    "verificación del formato de citas y generación de esta presentación "
    "interactiva en Streamlit. <strong style='color:#00BCD4'>NotebookLM</strong> (Google) fue "
    "utilizado para extraer informacion relevante de los artículos del corpus;"
    "La librería <strong style='color:#00BCD4'>pybibx</strong> (Python) permitió el procesamiento "
    "automatizado de metadatos bibliométricos y la generación de gráficos.<br><br>"
    "El uso de IA se limito a asistencia en producción textual y técnica, no en el juicio investigativo."
    "</p></div>",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# Tabla de uso por etapa
st.markdown("### Uso de IA por etapa del proceso")
st.markdown("<br>", unsafe_allow_html=True)

etapas = [
    ("Formulación del problema", "Claude Sonnet 4.6",
     "Generación de términos clave y estructuración de operadores booleanos",
     "Cadenas ejecutadas manualmente en Scopus y WoS; artículos seleccionados manualmente"),
    ("Búsqueda bibliográfica", "NotebookLM",
     "Extracción de información relevante de los artículos del corpus",
     "Cada dato verificado y contrastado con el paper original"),
    ("Extracción de datos", "pybibx (Python)",
     "Generación de tablas, gráficos e indicadores bibliométricos",
     "Outputs revisados; gráficos seleccionados manualmente"),
    ("Síntesis y redacción", "Claude Sonnet 4.6",
     "Mejora de coherencia y redacción del manuscrito",
     "Texto revisado y editado de forma iterativa hasta la versión final"),
]

header_style = "background:rgba(13,71,161,0.6);color:white;font-weight:600;padding:10px 14px;font-size:0.88rem"
cell_style = "padding:10px 14px;font-size:0.88rem;color:#c0d8ef;border-top:1px solid rgba(255,255,255,0.06)"
alt_style  = "padding:10px 14px;font-size:0.88rem;color:#c0d8ef;border-top:1px solid rgba(255,255,255,0.06);background:rgba(0,188,212,0.03)"

tabla_html = (
    "<table style='width:100%;border-collapse:collapse;border-radius:8px;overflow:hidden'>"
    "<thead><tr>"
    f"<th style='{header_style}'>Etapa</th>"
    f"<th style='{header_style}'>Herramienta</th>"
    f"<th style='{header_style}'>Uso específico</th>"
    f"<th style='{header_style}'>Verificación humana</th>"
    "</tr></thead><tbody>"
)
for i, (etapa, herr, uso, verif) in enumerate(etapas):
    s = alt_style if i % 2 == 0 else cell_style
    tabla_html += f"<tr><td style='{s}'>{etapa}</td><td style='{s}'>{herr}</td><td style='{s}'>{uso}</td><td style='{s}'>{verif}</td></tr>"
tabla_html += "</tbody></table>"

st.markdown(tabla_html, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Material suplementario ────────────────────────────────────────────────────
st.markdown("## Material Suplementario")
st.markdown("<br>", unsafe_allow_html=True)

# Enlace Colab
st.markdown(
    "<div style='border:1px solid rgba(0,188,212,0.3);border-radius:8px;"
    "padding:22px 26px;background:rgba(0,188,212,0.04)'>"
    "<p style='color:#00BCD4;font-weight:700;font-size:1rem;margin:0 0 10px 0'>"
    "Repositorio de código y datos (Google Colaboratory)</p>"
    "<p style='color:#7aadcc;font-size:0.9rem;margin:0 0 12px 0'>"
    "Código completo de procesamiento bibliométrico con pybibx, generación de gráficos "
    "e indicadores, y tabla con los 36 artículos seleccionados (año, título, abstract)."
    "</p>"
    "<a href='https://colab.research.google.com/drive/1w7vu7xPYRZaBOxYMVbpfmJ7b1sjR5aP8?usp=sharing' "
    "target='_blank' style='background:#00BCD4;color:#060d1a;font-weight:700;padding:9px 22px;"
    "border-radius:6px;text-decoration:none;font-size:0.95rem'>Abrir en Google Colab →</a>"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Referencias principales ───────────────────────────────────────────────────
st.markdown("## Referencias principales")
st.markdown(
    "El listado completo de 36 referencias en formato APA está disponible en el paper y en collab."
)
st.markdown("<br>", unsafe_allow_html=True)

referencias = [
    ("Scher & Van Den Hoek (2025)",
     "Nationwide conflict damage mapping with interferometric synthetic aperture radar: A study of the 2022 Russia–Ukraine conflict.",
     "Science of Remote Sensing, 11.", "https://doi.org/10.1016/j.srs.2025.100217"),
    ("Wagner et al. (2025)",
     "Monitoring cropland cultivation, abandonment, fallowing and recultivation dynamics with regard to conflict intensity in war-affected Ukraine.",
     "Science of Remote Sensing, 12.", "https://doi.org/10.1016/j.srs.2025.100326"),
    ("Wang et al. (2024)",
     "Analysis of nighttime light changes and trends in the 1-year anniversary of the Russia-Ukraine conflict.",
     "IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 17, 4084–4099.", "https://doi.org/10.1109/JSTARS.2024.3357727"),
    ("Huang et al. (2023)",
     "Monitoring urban change in conflict from the perspective of optical and SAR satellites: The case of Mariupol.",
     "Remote Sensing, 15(12).", "https://doi.org/10.3390/rs15123096"),
    ("Guo et al. (2025)",
     "Spatiotemporal dynamics of refugees and displaced persons during the Russia-Ukraine conflict: A nighttime light remote sensing perspective.",
     "Advances in Space Research, 76(4), 2053–2071.", "https://doi.org/10.1016/j.asr.2025.06.009"),
    ("Li et al. (2026)",
     "Dynamic patterns and driving factors of productive cropland in Ukraine before and after Russia-Ukraine conflict.",
     "Geography and Sustainability, 7(1).", "https://doi.org/10.1016/j.geosus.2025.100401"),
    ("Qiu et al. (2026)",
     "Analyzing the disruption of agricultural systems by conflict: A case study of sunflower production in eastern Ukraine.",
     "Agricultural Systems, 233.", "https://doi.org/10.1016/j.agsy.2026.104636"),
    ("Lin et al. (2024)",
     "Pixel-level quantification of damage and recovery caused by the Russia-Ukraine conflict based on nighttime light imagery.",
     "IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 17, 14712–14725.", "https://doi.org/10.1109/JSTARS.2024.3449394"),
    ("Mhanna et al. (2026)",
     "Hydrological and ecological consequences of the Kakhovka dam collapse.",
     "Environmental Research Letters, 21(6).", "https://doi.org/10.1088/1748-9326/ae4d5f"),
    ("Tomchenko et al. (2023)",
     "Assessment and monitoring of fires caused by the war in Ukraine on landscape scale.",
     "Journal of Landscape Ecology (Czech Republic), 16(2), 76–97.", "https://doi.org/10.2478/jlecol-2023-0011"),
]

for autores, titulo, fuente, doi in referencias:
    st.markdown(
        f"<div style='border-left:2px solid rgba(0,188,212,0.3);padding:14px 18px;margin:8px 0;"
        f"background:rgba(255,255,255,0.015);border-radius:0 6px 6px 0'>"
        f"<p style='color:#7aadcc;font-weight:600;font-size:0.95rem;margin:0 0 4px 0'>{autores}</p>"
        f"<p style='color:#c0d8ef;font-size:0.9rem;margin:0 0 4px 0;line-height:1.55'>{titulo}</p>"
        f"<p style='color:#4a7a99;font-size:0.83rem;margin:0 0 4px 0'>{fuente}</p>"
        f"<a href='{doi}' target='_blank' style='color:#00BCD4;font-size:0.8rem;text-decoration:none'>"
        f"{doi}</a>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#4a7a99;font-size:0.88rem;text-align:center'>"
    "Lista completa de 36 referencias en formato APA disponible en el paper (Material Suplementario)"
    "</p>",
    unsafe_allow_html=True,
)
