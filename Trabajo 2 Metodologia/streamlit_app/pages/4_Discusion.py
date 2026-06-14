import streamlit as st
from pages.utils.ui_theme import setup_page, stat, hr, badge, highlight

setup_page("Discusión · Patrones y limitaciones")

st.markdown("# Discusión")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:1.5rem'>"
    "Patrones transversales · Avances · Limitaciones</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

# ── Patrones ───────────────────────────────────────────────────────────────────
st.markdown("## Patrones metodológicos transversales")
st.markdown(
    "Ningún estudio del corpus usa un solo método. Lo que aparece repetidamente son cuatro "
    "estrategias que se combinan entre sí, y esa combinación es lo que explica la solidez "
    "de los resultados más robustos."
)
st.markdown("<br>", unsafe_allow_html=True)

patrones = [
    ("1. Fusión multisensor", "#00BCD4",
     "Los estudios que combinan SAR (Sentinel-1), óptico (Sentinel-2) y luz nocturna (VIIRS) "
     "obtienen resultados más sólidos que los que dependen de una sola plataforma. Cada sensor "
     "cubre los puntos ciegos de los otros: el SAR funciona bajo nubosidad, el óptico entrega "
     "información espectral fina, el VIIRS captura actividad nocturna."),
    ("2. Modelado contrafactual", "#0288D5",
     "En lugar de comparar directamente pre- y post-guerra, los modelos se entrenan con datos "
     "2019–2021 para simular el escenario sin conflicto. La diferencia con lo observado es el "
     "daño atribuible a la guerra, aislado de la variabilidad climática y los cambios de uso "
     "del suelo que ya existían antes."),
    ("3. Cruce con datos de eventos (ACLED + FIRMS)", "#00838F",
     "Cruzar destrucción satelital con eventos de combate verificados permite pasar de "
     "correlación a causalidad: los estudios que usan ACLED y FIRMS demuestran que la "
     "magnitud del daño aumenta con la proximidad al frente, no solo que coinciden."),
    ("4. Computación en la nube", "#4527A0",
     "Google Earth Engine no es solo comodidad: analizar más de 17.000 asentamientos "
     "simultáneamente en todo el territorio ucraniano sería directamente inviable en "
     "infraestructura local, sin importar el algoritmo que se use."),
]

for titulo, color, desc in patrones:
    st.markdown(
        f"<div style='"
        f"border-top:3px solid {color};"
        f"border-left:1px solid rgba(255,255,255,0.06);"
        f"border-right:1px solid rgba(255,255,255,0.06);"
        f"border-bottom:1px solid rgba(255,255,255,0.06);"
        f"border-radius:8px;padding:22px 26px;margin:14px 0;"
        f"background:rgba(255,255,255,0.02)'>"
        f"<p style='color:{color};font-weight:700;font-size:1.1rem;margin:0 0 10px 0'>{titulo}</p>"
        f"<p style='color:#a0bdd4;font-size:0.97rem;margin:0;line-height:1.65'>{desc}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Avances ────────────────────────────────────────────────────────────────────
st.markdown("## Qué cambió respecto a conflictos anteriores")
st.markdown(
    "En Siria y Yemen lo habitual era un solo sensor, una ciudad, datos mensuales. "
    "En Ucrania eso ya no funciona. Hay tres diferencias concretas:"
)
st.markdown("<br>", unsafe_allow_html=True)

avances = [
    ("Luz nocturna diaria",
     "Composites diarios (vs. mensuales anteriores) capturan eventos de <40 días "
     "como la ofensiva relámpago sobre Kiev (feb–mar 2022). Permite reconstruir "
     "la cronología del impacto con precisión sin precedente."),
    ("CCD a escala nacional",
     "Monitoreo simultáneo de 17,000+ asentamientos; en conflictos previos se "
     "analizaban solo ciudades individuales de forma aislada. Habilitado por "
     "Google Earth Engine y Sentinel-1 de acceso abierto."),
    ("Visión por computadora submétrica",
     "Imágenes de 30 cm permiten contar vehículos y personas en rutas de evacuación, "
     "estimando flujos de refugiados sin datos censales. Primera aplicación "
     "sistemática en un conflicto activo de esta escala."),
]

for titulo, desc in avances:
    st.markdown(
        f"<div style='"
        f"border-left:4px solid #00BCD4;"
        f"background:rgba(0,188,212,0.04);"
        f"border-radius:0 8px 8px 0;"
        f"padding:20px 24px;margin:12px 0'>"
        f"<p style='color:#00BCD4;font-weight:600;font-size:1.02rem;margin:0 0 8px 0'>{titulo}</p>"
        f"<p style='color:#9bbdd4;font-size:0.95rem;margin:0;line-height:1.6'>{desc}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Limitaciones ───────────────────────────────────────────────────────────────
st.markdown("## Principales limitaciones")
st.markdown(
    "El corpus identifica tres limitaciones estructurales que condicionan la validez "
    "y la generalización de los hallazgos."
)
st.markdown("<br>", unsafe_allow_html=True)

limites = [
    ("Sin verificación directa sobre el terreno", "#E65100",
     "Las zonas de combate activo y la presencia de campos minados impiden el acceso para "
     "verificación directa. Toda la validación depende de fuentes secundarias: OpenStreetMap, "
     "informes de ONGs e imágenes de alta resolución comerciales. Esto introduce sesgo de "
     "confirmación que no puede medirse completamente."),
    ("Limitaciones de sensores ópticos", "#F57F17",
     "La nubosidad persistente, el humo de incendios y la nieve estacional en el este de Ucrania "
     "generan brechas temporales significativas en las series de Sentinel-2 y Landsat. "
     "Los estudios deben interpolar o excluir períodos críticos, reduciendo la cobertura temporal."),
    ("Mediciones indirectas y suposiciones", "#827717",
     "Asumir que la caída en luz nocturna equivale a refugiados ignora toques de queda, "
     "cortes eléctricos preventivos y cambios de comportamiento. Los modelos de simulación "
     "asumen estacionariedad climática que puede no sostenerse bajo el cambio climático global."),
]

for titulo, color, desc in limites:
    st.markdown(
        f"<div style='"
        f"border-left:4px solid {color};"
        f"background:rgba(255,255,255,0.02);"
        f"border-radius:0 8px 8px 0;"
        f"padding:20px 24px;margin:12px 0'>"
        f"<p style='color:{color};font-weight:600;font-size:1.02rem;margin:0 0 8px 0'>{titulo}</p>"
        f"<p style='color:#9bbdd4;font-size:0.95rem;margin:0;line-height:1.6'>{desc}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Vacío identificado ─────────────────────────────────────────────────────────
st.markdown("## Vacío en la literatura")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    highlight(
        "A pesar del volumen y calidad de los 36 estudios revisados, el análisis sistemático "
        "revela una ausencia notable: <strong>ninguno aplica técnicas de agrupamiento espacial "
        "sobre los propios eventos de combate</strong> para identificar zonas de concentración "
        "de ataques ni construye un índice de peligrosidad para la población civil.<br><br>"
        "Los estudios parten sistemáticamente del satélite hacia el terreno —detectando daño "
        "desde imágenes— pero no desde los eventos en tierra hacia el espacio. Esta brecha "
        "impide caracterizar la intensidad del conflicto desde su origen y cruzarla con el "
        "daño documentado satelitalmente."
    ),
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Líneas de investigación futura (de los autores del corpus) ─────────────────
st.markdown("## Líneas de investigación futura identificadas en el corpus")
st.markdown(
    "Los propios autores de los 36 estudios señalan las siguientes direcciones prioritarias "
    "para continuar el campo:"
)
st.markdown("<br>", unsafe_allow_html=True)

futuras = [
    ("#00BCD4", "Inteligencia Artificial y Deep Learning",
     "Mejorar la precisión de clasificaciones y automatizar la detección de daños a escala "
     "nacional, reduciendo la supervisión manual requerida actualmente.",
     "Zatserkovnyi et al., 2025; Qiu et al., 2026"),
    ("#0288D5", "Fusión de datos multisensor",
     "Superar los problemas de nubosidad, resolución temporal y limitaciones de los sensores "
     "ópticos mediante la integración sistemática de múltiples plataformas.",
     "Scher & Van Den Hoek, 2025; Li et al., 2026"),
    ("#00838F", "Fuentes no convencionales (Big Data)",
     "Incorporar datos de dispositivos móviles, redes sociales y GPS anónimos para "
     "mejorar el rastreo de población desplazada más allá de los proxies satelitales.",
     "Rufener et al., 2024"),
    ("#4527A0", "Transferibilidad a otros conflictos",
     "Aplicar los marcos metodológicos desarrollados en Ucrania hacia otros contextos de "
     "conflicto activo (Sudán, Gaza, Myanmar) o emergencias humanitarias a escala global.",
     "Scher & Van Den Hoek, 2025; Wagner et al., 2025"),
]

for color, titulo, desc, refs in futuras:
    st.markdown(
        f"<div style='border-top:2px solid {color};"
        f"border-left:1px solid rgba(255,255,255,0.05);"
        f"border-right:1px solid rgba(255,255,255,0.05);"
        f"border-bottom:1px solid rgba(255,255,255,0.05);"
        f"border-radius:8px;padding:18px 22px;margin:12px 0;"
        f"background:rgba(255,255,255,0.02)'>"
        f"<p style='color:{color};font-weight:600;font-size:1rem;margin:0 0 6px 0'>{titulo}</p>"
        f"<p style='color:#a0bdd4;font-size:0.93rem;margin:0 0 8px 0;line-height:1.6'>{desc}</p>"
        f"<p style='color:#4a7a99;font-size:0.82rem;margin:0;font-style:italic'>{refs}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )
