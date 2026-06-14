import sys, os
sys.path.insert(0, os.getcwd())
import streamlit as st
from ui_theme import setup_page, hr, nav_buttons

setup_page("Objetivos | Trabajo 3")

st.markdown("# Objetivos de Investigacion")
st.markdown(hr(), unsafe_allow_html=True)

# ── OBJETIVO GENERAL ──────────────────────────────────────────────────────────
st.markdown("## Objetivo General")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='border:1px solid rgba(0,188,212,0.3);border-top:4px solid #00BCD4;"
    "border-radius:8px;padding:24px 26px;background:rgba(0,188,212,0.05);margin-bottom:20px'>"
    "<p style='color:#00BCD4;font-weight:700;font-size:0.9rem;margin:0 0 10px 0;letter-spacing:0.5px'>"
    "OBJETIVO GENERAL</p>"
    "<p style='color:#d0e8f5;font-size:1.05rem;margin:0;line-height:1.75'>"
    "<strong>Analizar</strong> la correspondencia espacial entre los patrones de "
    "concentracion de eventos de combate obtenidos mediante clustering no supervisado "
    "(K-Means y DBSCAN) sobre registros georreferenciados de ACLED (2022-2026) y las "
    "zonas de mayor daño agricola e infraestructural documentadas en la literatura de "
    "teledeteccion satelital del conflicto ruso-ucraniano."
    "</p></div>",
    unsafe_allow_html=True,
)

# ── FLUJO OE1-4 ────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
_flujo = [
    ("#00BCD4", "OE1", "Datos"),
    ("#0288D5", "OE2", "Metodo"),
    ("#7B1FA2", "OE3", "Evaluacion"),
    ("#E53935", "OE4", "Interpretacion"),
]
_flujo_html = "<div style='display:flex;align-items:center;justify-content:space-between;gap:6px;flex-wrap:wrap'>"
for _i, (_color, _num, _label) in enumerate(_flujo):
    _flujo_html += (
        f"<div style='flex:1;min-width:110px;text-align:center;border:1px solid {_color};"
        f"border-radius:8px;padding:12px 6px;background:rgba(255,255,255,0.02)'>"
        f"<p style='color:{_color};font-weight:700;font-size:0.95rem;margin:0'>{_num}</p>"
        f"<p style='color:#a0bdd4;font-size:0.82rem;margin:2px 0 0 0'>{_label}</p></div>"
    )
    if _i < len(_flujo) - 1:
        _flujo_html += "<div style='color:#5a8aaa;font-size:1.3rem;padding:0 2px'>&#8594;</div>"
_flujo_html += "</div>"
st.markdown(_flujo_html, unsafe_allow_html=True)
st.markdown(
    "<p style='color:#5a8aaa;font-size:0.82rem;text-align:center;margin:6px 0 0 0'>"
    "Secuencia de los objetivos especificos</p>",
    unsafe_allow_html=True,
)

st.markdown(hr(), unsafe_allow_html=True)

# ── OBJETIVOS ESPECIFICOS ─────────────────────────────────────────────────────
st.markdown("## Objetivos Especificos")
st.markdown("<br>", unsafe_allow_html=True)

oes = [
    ("#00BCD4", "OE1 - Datos",
     "Recopilar y preprocesar registros ACLED (feb 2022-dic 2026), filtrando por tipo "
     "de evento (bombardeos, combates, explosiones) y transformando coordenadas a UTM "
     "zona 36N (EPSG:32636) para metricas espaciales en unidades metricas consistentes."),
    ("#0288D5", "OE2 - Metodologia",
     "Implementar y comparar K-Means y DBSCAN sobre los registros preprocesados, ajustando "
     "hiperparametros con la curva del codo (k para K-Means) y el grafico de k-distancias "
     "(epsilon para DBSCAN), documentando el proceso para garantizar reproducibilidad."),
    ("#7B1FA2", "OE3 - Evaluacion",
     "Evaluar la calidad interna de los agrupamientos mediante el coeficiente de silueta y "
     "el indice de Davies-Bouldin para cada configuracion de ambos algoritmos, seleccionando "
     "la configuracion optima y comparando cuantitativamente K-Means vs DBSCAN."),
    ("#E53935", "OE4 - Interpretacion",
     "Interpretar la correspondencia espacial entre los clusters de alta intensidad y las regiones "
     "con mayor daño satelital: abandono agricola en Donetsk y Luhansk (Wagner et al., 2025; "
     "Li et al., 2026), daño urbano en Mariupol y el este ucraniano (Scher & Van Den Hoek, 2025; "
     "Huang et al., 2023) y caida de luz nocturna en zonas orientales (Wang et al., 2024)."),
]

for color, titulo, texto in oes:
    st.markdown(
        f"<div style='border-left:5px solid {color};padding:14px 20px;"
        f"background:rgba(255,255,255,0.02);border-radius:0 10px 10px 0;margin-bottom:12px'>"
        f"<p style='color:{color};font-weight:700;margin:0 0 6px 0'>{titulo}</p>"
        f"<p style='color:#c0d8ef;font-size:0.93rem;margin:0;line-height:1.6'>{texto}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

# ── NAVEGACION ─────────────────────────────────────────────────────────────
nav_buttons("pages/2_Pregunta_e_Hipotesis.py", "Pregunta e Hipótesis", "pages/4_Coherencia_y_Cierre.py", "Coherencia y Cierre")
