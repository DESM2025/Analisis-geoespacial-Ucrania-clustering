import streamlit as st
from pages.utils.ui_theme import setup_page, stat, hr, badge, highlight, show_img

setup_page("Bibliometría · Análisis cuantitativo")

st.markdown("# Análisis Bibliométrico")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:1.5rem'>"
    "Producción científica · Autores · Redes · Palabras clave</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Producción & Citas", "Autores, Países & Revistas", "Palabras clave & Redes"])

# ══════════════════════════════════════════════════════════════════════════════
# Tab 1 — Producción y Citas
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## Evolución temporal de la producción")
    st.markdown(
        "La producción científica sobre análisis geoespacial del conflicto creció de forma "
        "sostenida desde 2022, con el pico de publicaciones concentrado en 2025, lo que "
        "refleja el tiempo necesario para procesar y publicar datos de los primeros años de guerra."
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Documentos publicados por año")
    show_img("dpy.png", "Documentos por año · 2022–2026")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    st.markdown("#### Citas acumuladas por año")
    show_img("cpy.png", "Citas acumuladas · evolución temporal")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        highlight(
            "El pico en 2025 refleja el tiempo de procesamiento y publicación: los datos de los "
            "primeros años del conflicto tardaron en convertirse en artículos revisados."
        ),
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════════════════════════
# Tab 2 — Autores, Países y Fuentes
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## Autores más productivos")
    show_img("apd.png", "Autores con mayor número de publicaciones en el corpus")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    st.markdown("## Países con mayor producción")
    show_img("cpd.png", "Países más productivos · afiliaciones institucionales")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        highlight(
            "China concentra la mayor cantidad de afiliaciones del corpus. Le sigue Ucrania "
            "—cuyos investigadores colaboran frecuentemente desde el exterior por el conflicto— "
            "y luego Alemania y Estados Unidos en tercer y cuarto lugar."
        ),
        unsafe_allow_html=True,
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    st.markdown("## Revistas más productivas")
    show_img("spd.png", "Fuentes con mayor número de artículos analizados")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    st.markdown("## Distribución por revista")
    show_img("tree_map.png", "Treemap · distribución proporcional por fuente")

# ══════════════════════════════════════════════════════════════════════════════
# Tab 3 — Palabras clave y Redes
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## Nube de palabras clave")
    show_img("word_cloud.png", "Palabras clave más frecuentes en el corpus")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    st.markdown("## Bigramas más frecuentes")
    show_img("ngrams.png", "Bigramas · pares de términos co-ocurrentes")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    st.markdown("## Red de co-ocurrencia de palabras clave")
    show_img("network_adj.png", "Red de co-ocurrencia · nodos = términos, aristas = co-aparición")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    st.markdown("## Mapa de colaboración internacional")
    show_img("network_adj_map.png", "Colaboración geográfica entre autores de los estudios")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Términos dominantes identificados")
    st.markdown("<br>", unsafe_allow_html=True)
    terminos = [
        "remote sensing", "Ukraine", "war damage", "Sentinel-1",
        "land abandonment", "SAR", "NDVI", "nighttime light",
        "Google Earth Engine", "conflict", "machine learning",
        "VIIRS", "change detection", "agriculture",
    ]
    st.markdown(" ".join(badge(t) for t in terminos), unsafe_allow_html=True)
