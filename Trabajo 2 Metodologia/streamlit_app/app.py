import streamlit as st
from pages.utils.ui_theme import setup_page, stat, hr, badge, highlight, show_img

setup_page("Analisis Geoespacial | Rusia-Ucrania")

# Encabezado
st.markdown("# Analisis Geoespacial del Conflicto Rusia-Ucrania")
st.markdown(
    "<p style='font-size:1.3rem;color:#7aadcc;margin-top:-0.5rem;margin-bottom:0.5rem'>"
    "Revision bibliometrica</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color:#5a8aaa;font-size:0.95rem;margin-bottom:1.5rem'>"
    "Diego E. Silva Madariaga &middot; Metodologia de Investigacion en Ciencia de Datos &middot; UTEM 2026</p>",
    unsafe_allow_html=True,
)
st.markdown(hr(), unsafe_allow_html=True)

# De que trata
st.markdown("## Contexto")
st.markdown("<br>", unsafe_allow_html=True)

col_texto, col_stat = st.columns([1.6, 1], gap="large")

with col_texto:
    st.markdown(
        "El 24 de febrero de 2022, Rusia invadio Ucrania a gran escala. Los combates activos, "
        "los territorios ocupados y los campos minados hicieron inviable cualquier trabajo de campo: "
        "Por lo que se debio buscar nuevas herramientas para documentar el daño "
        "en tiempo real sin exponer a los investigadores."
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "Esta investigacion revisa 36 estudios cientificos publicados entre 2022 y 2026 "
        "que usaron principalmente imagenes satelitales para analizar el conflicto. Se busco saber "
        "que sensores se usaron, que metodologias se aplicaron y que impactos lograron medir."
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        highlight(
            "<strong>Objetivo:</strong> Sistematizar el estado del arte de las metodologias "
            "geoespaciales aplicadas al conflicto Rusia-Ucrania — identificar que funciona, "
            "que falta, y desde donde puede construirse un analisis propio con datos reales."
        ),
        unsafe_allow_html=True,
    )

with col_stat:
    st.markdown(stat("36",         "estudios cientificos analizados"),           unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(stat("2022-2026",  "periodo cubierto por los estudios"),          unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(stat("5 satelites","plataformas mas usadas en los estudios"),     unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# Propuesta propia
st.markdown("## Propuesta de analisis propio")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "Los 36 papers revisados detectan daños desde el satelite hacia el terreno. Ninguno hace el "
    "recorrido inverso de **agrupar los eventos de combate en tierra** para ver donde se concentra "
    "la violencia y que zonas son mas peligrosas para la poblacion civil. "
    "Esa es la brecha que se buscara cubrir mas adelante, usando datos publicos de ACLED."
)
st.markdown("<br>", unsafe_allow_html=True)

# Tres pilares de la propuesta
p1, p2, p3 = st.columns(3, gap="large")

with p1:
    st.markdown(
        "<div style='border-top:3px solid #00BCD4;border:1px solid rgba(0,188,212,0.15);"
        "border-radius:8px;padding:22px 20px;background:rgba(0,188,212,0.04);height:100%'>"
        "<p style='color:#00BCD4;font-weight:700;font-size:1rem;margin:0 0 10px 0'>"
        "Mapeo de eventos</p>"
        "<p style='color:#a0bdd4;font-size:0.93rem;margin:0;line-height:1.6'>"
        "Visualizar geograficamente todos los eventos del conflicto registrados en ACLED: "
        "bombardeos, combates, ataques a civiles y explosiones, con coordenadas y fecha."
        "</p></div>",
        unsafe_allow_html=True,
    )

with p2:
    st.markdown(
        "<div style='border-top:3px solid #0288D5;border:1px solid rgba(2,136,213,0.15);"
        "border-radius:8px;padding:22px 20px;background:rgba(2,136,213,0.04);height:100%'>"
        "<p style='color:#0288D5;font-weight:700;font-size:1rem;margin:0 0 10px 0'>"
        "Clustering de zonas de combate</p>"
        "<p style='color:#a0bdd4;font-size:0.93rem;margin:0;line-height:1.6'>"
        "Aplicar tecnicas de ML (K-Means, DBSCAN) para identificar automaticamente "
        "las zonas con mayor concentracion e intensidad de combate a lo largo del tiempo."
        "</p></div>",
        unsafe_allow_html=True,
    )

with p3:
    st.markdown(
        "<div style='border-top:3px solid #7B1FA2;border:1px solid rgba(123,31,162,0.15);"
        "border-radius:8px;padding:22px 20px;background:rgba(123,31,162,0.04);height:100%'>"
        "<p style='color:#CE93D8;font-weight:700;font-size:1rem;margin:0 0 10px 0'>"
        "Indice de peligro civil</p>"
        "<p style='color:#a0bdd4;font-size:0.93rem;margin:0;line-height:1.6'>"
        "Separar los eventos segun tipo (combate vs. violencia contra civiles) para "
        "construir un indice de peligrosidad por zona y cruzarlo con densidad de poblacion."
        "</p></div>",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

# Fuente de datos
st.markdown(
    "<div style='border-left:4px solid rgba(255,255,255,0.1);padding:14px 20px;"
    "background:rgba(255,255,255,0.02);border-radius:0 8px 8px 0'>"
    "<p style='color:#7aadcc;font-size:0.92rem;margin:0;line-height:1.6'>"
    "<strong style='color:#d0e8f5'>Fuente de datos:</strong> "
    "ACLED (Armed Conflict Location &amp; Event Data Project) &mdash; base publica con "
    "mas de 200,000 eventos georreferenciados del conflicto, incluyendo coordenadas, "
    "fecha, tipo de evento, actores involucrados y numero de victimas civiles."
    "</p></div>",
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# Impactos encontrados en la revision
st.markdown("## Lo que la revision bibliografica encontro")
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4, gap="medium")
with c1: st.markdown(stat("~2.4 M hectareas", "tierras agricolas abandonadas"),           unsafe_allow_html=True)
with c2: st.markdown(stat("264 km2",   "areas urbanas destruidas detectadas"), unsafe_allow_html=True)
with c3: st.markdown(stat("6.33 M",    "personas desplazadas"),         unsafe_allow_html=True)
with c4: st.markdown(stat("2,288",     "ciudades con daño registrado"),             unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(hr(), unsafe_allow_html=True)

# ── Encuadre disciplinar ───────────────────────────────────────────────────────
st.markdown("## Encuadre disciplinar")
st.markdown("<br>", unsafe_allow_html=True)

col_ocde, col_ods = st.columns(2, gap="large")

with col_ocde:
    st.markdown(
        "<div style='border-left:3px solid #00BCD4;padding:18px 22px;"
        "background:rgba(0,188,212,0.04);border-radius:0 8px 8px 0'>"
        "<p style='color:#00BCD4;font-weight:700;font-size:1rem;margin:0 0 10px 0'>"
        "Area OCDE</p>"
        "<p style='color:#a0bdd4;font-size:0.93rem;margin:0 0 6px 0;line-height:1.6'>"
        "<strong style='color:#d0e8f5'>Ciencias Sociales &rarr; Geografia</strong> "
        "(campo OCDE principal)<br>"
        "El problema es de naturaleza geografica: comprender la distribucion espacial "
        "y temporal del dano en territorio ucraniano."
        "</p>"
        "<p style='color:#a0bdd4;font-size:0.93rem;margin:0;line-height:1.6'>"
        "<strong style='color:#d0e8f5'>Ciencia de Datos</strong> (enfoque metodologico)<br>"
        "Clustering espacial no supervisado, series temporales satelitales y "
        "visualizacion geoespacial interactiva."
        "</p></div>",
        unsafe_allow_html=True,
    )

with col_ods:
    st.markdown(
        "<div style='border-left:3px solid #E53935;padding:18px 22px;"
        "background:rgba(229,57,53,0.04);border-radius:0 8px 8px 0;margin-bottom:12px'>"
        "<p style='color:#E53935;font-weight:700;font-size:1rem;margin:0 0 6px 0'>"
        "ODS 16 &mdash; Paz, Justicia e Instituciones Solidas</p>"
        "<p style='color:#a0bdd4;font-size:0.9rem;margin:0;line-height:1.55'>"
        "La propuesta de clustering sobre datos ACLED permite caracterizar zonas de "
        "concentracion de ataques con base en evidencia verificada, contribuyendo a "
        "la transparencia en contextos de conflicto armado."
        "</p></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='border-left:3px solid #F9A825;padding:18px 22px;"
        "background:rgba(249,168,37,0.04);border-radius:0 8px 8px 0'>"
        "<p style='color:#F9A825;font-weight:700;font-size:1rem;margin:0 0 6px 0'>"
        "ODS 11 &mdash; Ciudades y Comunidades Sostenibles</p>"
        "<p style='color:#a0bdd4;font-size:0.9rem;margin:0;line-height:1.55'>"
        "Separar matematicamente combates de bombardeos sobre areas urbanas facilita "
        "la identificacion de corredores de evacuacion y la priorizacion de recursos "
        "humanitarios en zonas de mayor impacto documentado."
        "</p></div>",
        unsafe_allow_html=True,
    )

