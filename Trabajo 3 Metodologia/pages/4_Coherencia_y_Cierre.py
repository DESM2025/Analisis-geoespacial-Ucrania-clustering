import sys, os
sys.path.insert(0, os.getcwd())
import streamlit as st
import pandas as pd
from ui_theme import setup_page, hr, highlight, nav_buttons

setup_page("Coherencia y Cierre | Trabajo 3")

st.markdown("# Coherencia, Evidencia y Declaracion de IA")
st.markdown(hr(), unsafe_allow_html=True)

tab_coh, tab_bib, tab_ia = st.tabs(["Coherencia del planteamiento", "Evidencia bibliografica", "Declaracion de IA"])

# ── COHERENCIA ────────────────────────────────────────────────────────────────
with tab_coh:
    st.markdown("### Cadena logica del planteamiento")
    st.markdown("<br>", unsafe_allow_html=True)

    cadena = [
        ("#E53935", "PROBLEMA", "Conflicto activo hace inviable el trabajo de campo.", "Justifica el enfoque satelital y el corpus de 36 articulos"),
        ("#F9A825", "BRECHA", "Ningun estudio usa eventos de combate como unidad de analisis primaria.", "Genera directamente la pregunta de investigacion"),
        ("#00BCD4", "PREGUNTA", "¿En que medida los clusters de combate se corresponden con el daño satelital?", "La hipotesis anticipa una respuesta provisional"),
        ("#7B1FA2", "HIPOTESIS", "Correspondencia espacial positiva en oblasts orientales y meridionales.", "El objetivo general la operacionaliza"),
        ("#0288D5", "OBJ. GENERAL", "Analizar la correspondencia espacial entre clusters de combate y daño satelital.", "Los OE lo descomponen en fases evaluables"),
        ("#00BCD4", "OE 1-4", "Datos -> Metodo -> Evaluacion -> Interpretacion territorial.", "Secuencia logica y temporal coherente"),
    ]

    for i, (color, titulo, contenido, vinculo) in enumerate(cadena):
        st.markdown(
            f"<div style='border:1px solid {color};border-radius:10px;padding:14px 20px;"
            f"background:rgba(255,255,255,0.03);text-align:center'>"
            f"<p style='color:{color};font-weight:700;font-size:0.85rem;margin:0 0 6px 0;letter-spacing:0.5px'>{titulo}</p>"
            f"<p style='color:#d0e8f5;font-size:0.95rem;margin:0;line-height:1.5'>{contenido}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )
        if i < len(cadena) - 1:
            st.markdown(
                f"<div style='text-align:center;margin:2px 0'>"
                f"<div style='color:#5a8aaa;font-size:1.4rem;line-height:1'>&#8595;</div>"
                f"<p style='color:#5a8aaa;font-size:0.78rem;font-style:italic;margin:0 0 2px 0'>{vinculo}</p>"
                f"</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe({
        "Componente": ["Problema", "Brecha", "Pregunta", "Hipotesis", "Obj. General", "OE 1-4"],
        "Contenido central": [
            "Acceso imposible al terreno; metodos remotos necesarios",
            "Ningun estudio usa eventos de combate como unidad de analisis primaria",
            "Correspondencia clustering ACLED vs daño satelital documentado",
            "Correspondencia espacial positiva en oblasts orientales y meridionales",
            "Analizar la correspondencia espacial entre clusters de combate y daño satelital",
            "Datos - Metodo - Evaluacion - Interpretacion territorial",
        ],
        "Vinculacion con el siguiente": [
            "Justifica 36 estudios satelitales",
            "Genera la pregunta",
            "Hipotesis anticipa respuesta",
            "OG la operacionaliza",
            "OE lo descomponen",
            "Secuencia coherente",
        ],
    }, use_container_width=True)

# ── EVIDENCIA BIBLIOGRAFICA ────────────────────────────────────────────────────
with tab_bib:
    st.markdown("### Articulos clave del corpus (11 referencias)")
    st.markdown("<br>", unsafe_allow_html=True)

    st.dataframe({
        "Referencia": [
            "Scher & Van Den Hoek (2025)",
            "Huang et al. (2023)",
            "Wagner et al. (2025)",
            "Li et al. (2026)",
            "Qiu et al. (2026)",
            "Wang et al. (2024)",
            "Xiao et al. (2024)",
            "Lin et al. (2024)",
            "Guo et al. (2025)",
            "Tomchenko et al. (2023)",
            "Kganyago et al. (2025)",
        ],
        "Hallazgo / Rol": [
            "264 km2 daño urbano SAR. 67% a < 10 km del frente.",
            "Daño urbano Mariupol con SAR + optico.",
            "2.34-2.40 M ha abandonadas. ACLED como validacion.",
            "Patrones de tierras productivas antes/despues del conflicto.",
            "82.6% perdida siembra de girasol en el este de Ucrania.",
            "Caida 84% luz nocturna. 1er aniversario del conflicto.",
            "Perdida luz nocturna ofensiva Kiev (VIIRS DNB).",
            "Cuantificacion pixel a pixel del daño con luz nocturna.",
            "Dinamica espaciotemporal de refugiados con luz nocturna.",
            "Incendios causados por la guerra. ACLED como validacion.",
            "Incendios MODIS/VIIRS. ACLED como cruce de validacion.",
        ],
        "Sustenta": [
            "Hipotesis + OE4",
            "Hipotesis + OE4",
            "Hipotesis + OE4",
            "OE4",
            "OE4",
            "Problema + Hipotesis",
            "Problema",
            "OE4",
            "Problema",
            "Brecha",
            "Brecha",
        ],
    }, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Respaldo bibliografico por componente**")
    sustenta_counts = pd.DataFrame(
        {"Referencias": [6, 4, 3, 2]},
        index=["OE4", "Hipotesis", "Problema", "Brecha"],
    )
    st.bar_chart(sustenta_counts, color="#00BCD4", height=260)

# ── DECLARACION IA ─────────────────────────────────────────────────────────────
with tab_ia:
    st.markdown("### Herramientas utilizadas")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<div style='border-left:3px solid #00BCD4;padding:14px 18px;"
        "background:rgba(0,188,212,0.05);border-radius:0 8px 8px 0'>"
        "<p style='color:#00BCD4;font-weight:700;margin:0 0 6px 0'>Claude Sonnet 4.6 (Anthropic, 2026)</p>"
        "<p style='color:#c0d8ef;font-size:0.93rem;margin:0'>Accedido via Cowork. Apoyo en estructuracion "
        "del manuscrito, sintesis critica del estado del arte, redaccion academica y desarrollo de la app.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        highlight(
            "<strong>Declaracion de autoria:</strong> Todas las decisiones investigativas "
            "- identificacion de la brecha, formulacion de la pregunta, planteamiento de la "
            "hipotesis y definicion de objetivos - son responsabilidad exclusiva del autor. "
            "La redaccion fue revisada y validada iterativamente hasta la version final."
        ),
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:16px 20px;"
        "background:rgba(255,255,255,0.02);text-align:center;margin-top:16px'>"
        "<p style='color:#d0e8f5;font-weight:700;font-size:1rem;margin:0 0 4px 0'>"
        "Diego Ernesto Silva Madariaga</p>"
        "<p style='color:#5a8aaa;font-size:0.88rem;margin:0'>"
        "Metodologia de Investigacion en Ciencia de Datos · UTEM · 2026</p>"
        "</div>",
        unsafe_allow_html=True,
    )

# ── NAVEGACION ─────────────────────────────────────────────────────────────
nav_buttons("pages/3_Objetivos.py", "Objetivos", "Portada.py", "Portada")
