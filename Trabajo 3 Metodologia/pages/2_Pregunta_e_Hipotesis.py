import sys, os
sys.path.insert(0, os.getcwd())
import streamlit as st
from ui_theme import setup_page, hr, highlight, card_borde, nav_buttons, img_b64

setup_page("Pregunta e Hipotesis | Trabajo 3")

st.markdown("# Pregunta de Investigacion e Hipotesis")
st.markdown(hr(), unsafe_allow_html=True)

# ── PREGUNTA ──────────────────────────────────────────────────────────────────
st.markdown("## Pregunta de Investigacion")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='border:1px solid rgba(0,188,212,0.35);border-top:4px solid #00BCD4;"
    "border-radius:8px;padding:26px 28px;background:rgba(0,188,212,0.05);margin-bottom:20px'>"
    "<p style='color:#00BCD4;font-weight:700;font-size:0.9rem;margin:0 0 12px 0;letter-spacing:0.5px'>"
    "PREGUNTA PRINCIPAL</p>"
    "<p style='color:#d0e8f5;font-size:1.08rem;margin:0;line-height:1.75;font-style:italic'>"
    "En que medida los patrones espaciales de concentracion de eventos de combate "
    "identificados mediante clustering no supervisado sobre registros ACLED "
    "se corresponden con las zonas de mayor daño agricola y urbano documentado "
    "satelitalmente en el conflicto ruso-ucraniano (2022-2026)?"
    "</p></div>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown(card_borde("#00BCD4", "Especifica", "Delimita fenomeno, metodo (clustering), datos (ACLED) y contexto (2022-2026)."), unsafe_allow_html=True)
    st.markdown(card_borde("#00BCD4", "Emerge de la brecha", "Nadie ha usado ACLED como insumo primario de clustering espacial."), unsafe_allow_html=True)
with col2:
    st.markdown(card_borde("#00BCD4", "Abordable con Ciencia de Datos", "Requiere clustering no supervisado y metricas de validacion cuantitativa."), unsafe_allow_html=True)
    st.markdown(card_borde("#00BCD4", "No trivialmente descriptiva", "Evalua correspondencia entre dos fuentes independientes. La respuesta no es obvia."), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── HIPOTESIS ─────────────────────────────────────────────────────────────────
st.markdown("## Hipotesis")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='border:1px solid rgba(0,188,212,0.3);border-top:4px solid #7B1FA2;"
    "border-radius:8px;padding:26px 28px;background:rgba(123,31,162,0.04);margin-bottom:20px'>"
    "<p style='color:#CE93D8;font-weight:700;font-size:0.9rem;margin:0 0 12px 0;letter-spacing:0.5px'>"
    "HIPOTESIS CORRELACIONAL</p>"
    "<p style='color:#d0e8f5;font-size:1.05rem;margin:0;line-height:1.75'>"
    "Los clusters de alta concentracion de eventos de combate que se identifiquen mediante "
    "K-Means y DBSCAN sobre registros ACLED (2022-2026) presentaran una "
    "<strong>correspondencia espacial positiva</strong> con las zonas de mayor daño "
    "agricola y urbano documentadas satelitalmente en los oblasts orientales y meridionales de Ucrania "
    "(Donetsk, Luhansk, Jerson y Zaporiyia)."
    "</p></div>",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)
col_mapa, col_fund = st.columns([1, 1.1], gap="large")
with col_mapa:
    st.markdown(
        f"<div style='border-radius:10px;overflow:hidden;border:1px solid rgba(123,31,162,0.25);"
        f"background:rgba(255,255,255,0.02)'>"
        f"<img src='data:image/png;base64,{img_b64('UKR3.png')}' "
        f"style='width:100%;display:block'></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:#5a8aaa;font-size:0.8rem;text-align:center;margin-top:6px'>"
        "Zonas de mayor actividad de combate: oblasts orientales y meridionales de la hipotesis</p>",
        unsafe_allow_html=True,
    )
with col_fund:
    st.markdown("**Fundamento empirico del corpus:**")
    fundamentos = [
        "67% del daño urbano ocurre a menos de 10 km del frente (Scher & Van Den Hoek, 2025)",
        "La intensidad del conflicto predice el abandono agricola a escala regional (Wagner et al., 2025)",
        "Los cruces ACLED-satelite existentes reportan consistencia espacial entre eventos y zonas de daño",
    ]
    for f in fundamentos:
        st.markdown(f"- {f}")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    highlight(
        "<strong>Tipo:</strong> Correlacional (no causal). Propone covariacion espacial positiva "
        "entre clusters de combate (ACLED) y daño documentado satelitalmente, sin controlar "
        "por factores confundentes climaticos o de acceso al terreno."
    ),
    unsafe_allow_html=True,
)

# ── NAVEGACION ─────────────────────────────────────────────────────────────
nav_buttons("pages/1_Estado_del_Arte.py", "Estado del Arte", "pages/3_Objetivos.py", "Objetivos")
