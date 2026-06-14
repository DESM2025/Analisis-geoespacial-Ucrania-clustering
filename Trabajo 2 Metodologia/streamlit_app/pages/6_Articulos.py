import streamlit as st
import pandas as pd
from pathlib import Path
from pages.utils.ui_theme import setup_page, stat, hr, badge, highlight, PROJECT_DIR

setup_page("Artículos incluidos · Corpus final")

st.markdown("# Artículos incluidos")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:1.5rem'>"
    "Corpus final · 36 estudios seleccionados mediante PRISMA 2020</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

# ── Cargar datos ──────────────────────────────────────────────────────────────
xlsx_path = PROJECT_DIR / "articulos_finales_ucrania.xlsx"

@st.cache_data
def load_articles():
    df = pd.read_excel(xlsx_path, engine="openpyxl")
    cols = {
        "author": "Autores",
        "year": "Año",
        "title": "Título",
        "journal": "Revista / Fuente",
        "doi": "DOI",
    }
    df_clean = df[[c for c in cols if c in df.columns]].rename(columns=cols)
    df_clean["Año"] = df_clean["Año"].astype(str)
    # Primer autor resumido
    def shorten_authors(a):
        if pd.isna(a): return ""
        parts = str(a).split(" and ")
        first = parts[0].split(",")[0].strip()
        return f"{first} et al." if len(parts) > 1 else first
    df_clean["Autores"] = df_clean["Autores"].apply(shorten_authors)
    df_clean = df_clean.fillna("—")
    return df_clean

try:
    df = load_articles()

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1: st.markdown(stat("36", "artículos en el corpus final"), unsafe_allow_html=True)
    with c2: st.markdown(stat("2022–2026", "período de publicación"), unsafe_allow_html=True)
    with c3: st.markdown(stat("2 BD", "Scopus + Web of Science"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Filtros
    col_f1, col_f2 = st.columns([2, 1], gap="medium")
    with col_f1:
        busqueda = st.text_input("Buscar por título, autor o revista", placeholder="Ej: SAR, Wagner, Remote Sensing...")
    with col_f2:
        años = ["Todos"] + sorted(df["Año"].unique().tolist())
        año_sel = st.selectbox("Filtrar por año", años)

    df_filtered = df.copy()
    if busqueda:
        mask = df_filtered.apply(lambda row: busqueda.lower() in " ".join(str(v) for v in row).lower(), axis=1)
        df_filtered = df_filtered[mask]
    if año_sel != "Todos":
        df_filtered = df_filtered[df_filtered["Año"] == año_sel]

    st.markdown(f"<p style='color:#5a8aaa;font-size:0.9rem'>{len(df_filtered)} de 36 artículos mostrados</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Tabla principal
    st.dataframe(
        df_filtered[["Año", "Autores", "Título", "Revista / Fuente"]],
        use_container_width=True,
        hide_index=True,
        height=520,
        column_config={
            "Año":    st.column_config.TextColumn("Año",    width="small"),
            "Autores": st.column_config.TextColumn("Autores", width="medium"),
            "Título":  st.column_config.TextColumn("Título",  width="large"),
            "Revista / Fuente": st.column_config.TextColumn("Revista / Fuente", width="medium"),
        },
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)

    # Distribución por año
    st.markdown("## Distribución por año de publicación")
    st.markdown("<br>", unsafe_allow_html=True)
    año_counts = df["Año"].value_counts().sort_index()
    st.bar_chart(año_counts, color="#00BCD4", height=280)

    st.markdown("<br>", unsafe_allow_html=True)


except Exception as e:
    st.error(f"No se pudo cargar el archivo de artículos: {e}")
    st.markdown(
        highlight(
            "El corpus de 36 artículos fue seleccionado siguiendo el protocolo PRISMA 2020 "
            "a partir de una búsqueda inicial de 114 registros en Scopus y Web of Science."
        ),
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# Criterios aplicados
st.markdown("## Criterios de selección aplicados")
st.markdown("<br>", unsafe_allow_html=True)

criterios = [
    ("Inclusión", "#00BCD4", [
        "Aplica al menos una técnica de análisis geoespacial o teledetección",
        "Contexto de aplicación: conflicto Rusia-Ucrania o sus impactos directos",
        "Publicado en inglés entre 2022 y 2026",
        "Disponible en texto completo",
    ]),
    ("Exclusión", "#E65100", [
        "Artículos de opinión, editoriales o comentarios sin datos empíricos",
        "Técnicas geoespaciales mencionadas solo de forma tangencial",
        "Sin acceso a resumen o texto completo",
        "Estudios duplicados entre bases de datos",
    ]),
]

col_inc, col_exc = st.columns(2, gap="large")
for col, (titulo, color, items) in zip([col_inc, col_exc], criterios):
    with col:
        st.markdown(
            f"<p style='color:{color};font-weight:700;font-size:1.05rem;margin-bottom:10px'>{titulo}</p>",
            unsafe_allow_html=True,
        )
        for item in items:
            st.markdown(
                f"<div style='border-left:2px solid {color};padding:8px 14px;margin:6px 0;"
                f"background:rgba(255,255,255,0.02);border-radius:0 4px 4px 0'>"
                f"<span style='color:#c0d8ef;font-size:0.95rem'>{item}</span></div>",
                unsafe_allow_html=True,
            )
