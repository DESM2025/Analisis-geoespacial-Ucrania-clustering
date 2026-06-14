import streamlit as st
import pandas as pd
from pages.utils.ui_theme import setup_page, stat, hr, badge, highlight

setup_page("Resultados · Métodos y hallazgos")

st.markdown("# Resultados")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:1.5rem'>"
    "Métodos identificados · Sensores · Regiones · Impactos</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Métodos identificados", "Tecnologías satelitales", "Cobertura & Impactos"])

# ══════════════════════════════════════════════════════════════════════════════
# Tab 1 — Métodos
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## Métodos de análisis geoespacial")
    st.markdown(
        "El corpus de 36 artículos emplea una amplia variedad de métodos, desde técnicas "
        "clásicas de teledetección hasta enfoques de inteligencia artificial a escala nacional. "
        "La tabla resume los diez métodos principales con sus sensores y hallazgos clave."
    )
    st.markdown("<br>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Método": [
            "Detección de cambio coherente (CCD) con SAR",
            "Machine Learning (RF, XGBoost, DNN)",
            "Luz nocturna — umbral dual",
            "Muestreo estratificado + regresión espacial",
            "Análisis espectral (NDVI / NDWI)",
            "Simulación del escenario sin guerra (ML)",
            "Inversión satelital (GEOS-Chem)",
            "Detección doble período (DCD)",
            "Visión por computadora + GAM",
            "Puntos calientes Getis-Ord Gi*",
        ],
        "Sensores": [
            "Sentinel-1",
            "Sentinel-1/2, VIIRS, ACLED",
            "VIIRS Black Marble",
            "Planet, Sentinel-1/2",
            "Sentinel-2, Landsat-8",
            "Landsat-7/8, Sentinel-1/2, ERA5",
            "TROPOMI, EDGAR",
            "MODIS NDVI, Landsat 8-9",
            "Maxar WorldView, WorldPop",
            "MODIS LST, Sentinel-5P, FIRMS",
        ],
        "Hallazgo clave": [
            "264 km² de daño; 67 % a <10 km del frente",
            "82.6 % de pérdida en área de girasol",
            "Caída del 84 % en luz nocturna nacional",
            "Fuerte asociación frente–abandono agrícola",
            "Declive severo de vegetación en el este",
            "47.77 % de cuadrículas con reducción productiva",
            "Caídas sistémicas en NOx y CO₂",
            "462,000 ha abandonadas en el este",
            "Estimación del desplazamiento civil",
            "Anomalías térmicas e islas de calor urbano",
        ],
    })
    st.dataframe(df, use_container_width=True, hide_index=True, height=420)

# ══════════════════════════════════════════════════════════════════════════════
# Tab 2 — Sensores
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## Plataformas satelitales dominantes")
    st.markdown(
        "Cinco plataformas concentran la mayoría de los estudios. Su combinación — **multisensor** — "
        "es el patrón metodológico más frecuente del corpus, ya que cada sensor compensa "
        "las limitaciones operativas de los demás."
    )
    st.markdown("<br>", unsafe_allow_html=True)

    sensores = [
        ("#00BCD4",
         "Sentinel-1  ·  SAR (Radar de apertura sintética)",
         "Penetra nubes, lluvia, humo y oscuridad nocturna. Herramienta central para la evaluación "
         "de daños urbanos mediante CCD (Coherent Change Detection) y el mapeo de abandono de cultivos "
         "a escala nacional. Opera con resolución de 5–20 m."),
        ("#0288D5",
         "Sentinel-2  ·  Óptico multiespectral",
         "Resolución de 10–20 m en 13 bandas espectrales. Índices NDVI/NDWI para vegetación e "
         "inundaciones, mapeo de áreas quemadas y cambios en uso del suelo agrícola post-conflicto."),
        ("#00838F",
         "VIIRS / NASA Black Marble  ·  Luz nocturna",
         "Composites diarios y mensuales de radiance nocturna. Permite detectar cortes de energía, "
         "estimar desplazamiento de población y cuantificar el deterioro de infraestructura urbana "
         "a través de cambios en la actividad luminosa."),
        ("#1B5E20",
         "MODIS  ·  Terra & Aqua",
         "Series temporales largas (desde 2000) de vegetación (NDVI), temperatura superficial (LST) "
         "y focos de calor activos vía FIRMS. Resolución de 250–1000 m. Ideal para análisis "
         "de tendencias pre y post conflicto."),
        ("#4527A0",
         "Satélites VHR  ·  Planet / Maxar WorldView",
         "Hasta 30 cm de resolución espacial. Permiten validar resultados a nivel de calle: "
         "conteo de cráteres, identificación de vehículos militares y evaluación de daños "
         "en edificios individuales. Usado principalmente para calibración de algoritmos SAR."),
    ]

    for color, nombre, desc in sensores:
        st.markdown(
            f"<div style='"
            f"border-left:4px solid {color};"
            f"background:rgba(255,255,255,0.025);"
            f"border-radius:0 8px 8px 0;"
            f"padding:20px 24px;"
            f"margin:14px 0'>"
            f"<p style='color:{color};font-weight:700;font-size:1.08rem;margin:0 0 8px 0'>{nombre}</p>"
            f"<p style='color:#a8c8e0;font-size:0.95rem;margin:0;line-height:1.6'>{desc}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )

# ══════════════════════════════════════════════════════════════════════════════
# Tab 3 — Cobertura e Impactos
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)

    # ── Regiones ───────────────────────────────────────────────────────────────
    st.markdown("## Regiones más estudiadas")
    st.markdown(
        "La cobertura geográfica del corpus no es uniforme: el este y el sur de Ucrania "
        "concentran la mayoría de los estudios, dada la mayor intensidad del conflicto "
        "y la extensión de las tierras agrícolas afectadas."
    )
    st.markdown("<br>", unsafe_allow_html=True)

    regiones = [
        ("Donetsk & Luhansk",
         "Epicentro de los combates. Mayor cantidad de estudios sobre daño urbano y abandono "
         "agrícola masivo. Incluye ciudades como Mariúpol y Bakhmut."),
        ("Jersón & Zaporiyia",
         "Abandono de tierras de regadío y destrucción de la presa Kajovka con sus consecuencias "
         "hidrológicas y agrícolas aguas abajo."),
        ("Járkov",
         "Infraestructura urbana, islas de calor urbano y combates en zona metropolitana densamente poblada."),
        ("Kiev & oblast",
         "Calidad del aire y emisiones durante la fase inicial de la guerra. Estimación de "
         "desplazamiento masivo de población con proxies satelitales."),
        ("Mariúpol",
         "Caso más citado del corpus: primera calibración y validación masiva de algoritmos SAR "
         "en una ciudad ucraniana completamente sitiada."),
    ]

    for region, desc in regiones:
        st.markdown(
            f"<div style='"
            f"border-left:4px solid #00BCD4;"
            f"background:rgba(0,188,212,0.04);"
            f"border-radius:0 8px 8px 0;"
            f"padding:16px 20px;margin:10px 0'>"
            f"<p style='color:#00BCD4;font-weight:600;font-size:1.02rem;margin:0 0 5px 0'>{region}</p>"
            f"<p style='color:#9bbdd4;font-size:0.93rem;margin:0;line-height:1.55'>{desc}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)

    # ── Impactos ───────────────────────────────────────────────────────────────
    st.markdown("## Jerarquía de impactos documentados")
    st.markdown(
        "Los impactos se organizan por volumen de evidencia satelital disponible "
        "y por la solidez metodológica de los estudios que los cuantifican."
    )
    st.markdown("<br>", unsafe_allow_html=True)

    impactos = [
        ("#00BCD4", "Ambientales", "Muy alta",
         "Incendios forestales y de cultivos, contaminación atmosférica, destrucción de la presa "
         "Kajovka y sus efectos hidrológicos, emisiones de gases de efecto invernadero."),
        ("#0288D5", "Agrícolas", "Muy alta",
         "Abandono de ~2.4 M ha de tierras cultivables, caída de rendimientos en girasol (−82.6 %), "
         "trigo y maíz. 10 % de la producción mundial de trigo en riesgo."),
        ("#00838F", "Urbanos e Infraestructura", "Alta",
         "264 km² de daño estructural en 2,288 asentamientos detectados vía SAR. "
         "Apagones con más del 80 % de caída en luz nocturna nacional."),
        ("#607D8B", "Humanitarios", "Indirecta",
         "Flujo de 6.33 M de refugiados estimado con proxies satelitales (NTL, densidad de población). "
         "Validación parcial con datos del ACNUR."),
        ("#455A64", "Militares", "Contextual",
         "Líneas de frente (ACLED) usadas como variable causal explicativa de los demás impactos. "
         "Correlación espacial significativa con zonas de daño."),
    ]

    for color, nombre, nivel, desc in impactos:
        st.markdown(
            f"<div style='"
            f"border-left:4px solid {color};"
            f"background:rgba(255,255,255,0.02);"
            f"border-radius:0 8px 8px 0;"
            f"padding:18px 22px;margin:12px 0'>"
            f"<div style='display:flex;align-items:center;gap:12px;margin-bottom:8px'>"
            f"<span style='color:{color};font-weight:700;font-size:1.05rem'>{nombre}</span>"
            f"<span style='background:{color};color:#fff;font-size:0.72rem;"
            f"padding:2px 11px;border-radius:12px;font-weight:600'>{nivel}</span>"
            f"</div>"
            f"<p style='color:#8aafc8;font-size:0.93rem;margin:0;line-height:1.55'>{desc}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )
