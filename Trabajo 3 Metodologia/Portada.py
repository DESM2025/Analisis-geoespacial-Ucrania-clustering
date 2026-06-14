import streamlit as st
from ui_theme import setup_page, hr, badge, img_b64

setup_page("Portada | Trabajo 3")

# ── Título ──
st.markdown(
    "<h1 style='font-size:2.1rem;line-height:1.25;margin-bottom:0.3rem'>"
    "Correspondencia Espacial entre Clústeres de Intensidad de Combate<br>"
    "<span style='color:#7aadcc'>y Daño Satelital en el Conflicto Ruso-Ucraniano</span></h1>",
    unsafe_allow_html=True,
)

st.markdown(hr(), unsafe_allow_html=True)

col_info, col_badges = st.columns([1.6, 1], gap="large")

with col_info:
    st.markdown(
        "<p style='color:#a0bdd4;font-size:1.05rem;margin:0 0 6px 0'>"
        "<strong style='color:#d0e8f5'></strong> Diego Ernesto Silva Madariaga</p>"
        "<p style='color:#a0bdd4;font-size:1.05rem;margin:0 0 6px 0'>"
        "<strong style='color:#d0e8f5'></strong> Metodología de Investigación en Ciencia de Datos</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='margin-top:16px;border-radius:10px;overflow:hidden;"
        f"border:1px solid rgba(0,188,212,0.18)'>"
        f"<img src='data:image/jpeg;base64,{img_b64('arcwatch-banner-learntouseclustering-wide.jpg')}' "
        f"style='width:100%;display:block'></div>",
        unsafe_allow_html=True,
    )

with col_badges:
    st.markdown(
        "<p style='color:#7aadcc;font-size:0.9rem;margin:0 0 10px 0;font-weight:600'>"
        "Área OCDE</p>"
        "<div style='border-left:3px solid #00BCD4;padding:10px 16px;"
        "background:rgba(0,188,212,0.06);border-radius:0 8px 8px 0;margin-bottom:14px'>"
        "<p style='color:#d0e8f5;font-size:0.9rem;margin:0 0 2px 0'>"
        "<strong style='color:#d0e8f5'>Ciencias Sociales → Geografía</strong></p>"
        "<p style='color:#7aadcc;font-size:0.82rem;margin:0'>campo OCDE principal</p></div>"
        "<div style='border-left:3px solid rgba(0,188,212,0.4);padding:10px 16px;"
        "background:rgba(0,188,212,0.03);border-radius:0 8px 8px 0;margin-bottom:30px'>"
        "<p style='color:#d0e8f5;font-size:0.9rem;margin:0 0 2px 0'>Ciencia de Datos</p>"
        "<p style='color:#7aadcc;font-size:0.82rem;margin:0'>enfoque metodológico</p></div>"
        "<p style='color:#7aadcc;font-size:0.9rem;margin:0 0 10px 0;font-weight:600'>"
        "Objetivos de Desarrollo Sostenible</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<span style='display:inline-block;background:rgba(229,57,53,0.15);"
        "border:1px solid rgba(229,57,53,0.4);border-radius:20px;padding:5px 16px;"
        "font-size:0.9rem;color:#ef9a9a'>ODS 16 · Paz, Justicia e Instituciones Sólidas</span>"
        "&nbsp;"
        "<span style='display:inline-block;background:rgba(249,168,37,0.12);"
        "border:1px solid rgba(249,168,37,0.4);border-radius:20px;padding:5px 16px;"
        "font-size:0.9rem;color:#ffe082'>ODS 11 · Ciudades y Comunidades Sostenibles</span>",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Mapa de navegación ──
st.markdown("## Estructura de la presentación")
st.markdown("<br>", unsafe_allow_html=True)

secciones = [
    ("1", "#00BCD4", "Estado del Arte", "Problema · Avances y Brechas · Enfoque Propuesto", "/Estado_del_Arte"),
    ("2", "#7B1FA2", "Pregunta e Hipótesis", "Pregunta de investigación e hipótesis correlacional", "/Pregunta_e_Hipotesis"),
    ("3", "#0288D5", "Objetivos", "Objetivo general y objetivos específicos OE1–4", "/Objetivos"),
    ("4", "#F9A825", "Coherencia y Cierre", "Coherencia · Evidencia bibliográfica · Declaración IA", "/Coherencia_y_Cierre"),
]

col1, col2 = st.columns(2, gap="large")
for i, (num, color, titulo, desc, url) in enumerate(secciones):
    col = col1 if i % 2 == 0 else col2
    with col:
        st.markdown(
            f"<a href='{url}' target='_self' style='text-decoration:none;display:block;margin-bottom:10px'>"
            f"<div style='border-left:3px solid {color};padding:12px 16px;"
            f"background:rgba(255,255,255,0.02);border-radius:0 8px 8px 0;"
            f"cursor:pointer;transition:background 0.18s' "
            f"onmouseover=\"this.style.background='rgba(255,255,255,0.055)'\" "
            f"onmouseout=\"this.style.background='rgba(255,255,255,0.02)'\">"
            f"<p style='color:{color};font-weight:700;font-size:0.9rem;margin:0 0 2px 0'>"
            f"{num}. {titulo}</p>"
            f"<p style='color:#7aadcc;font-size:0.85rem;margin:0'>{desc}</p>"
            f"</div></a>",
            unsafe_allow_html=True,
        )
