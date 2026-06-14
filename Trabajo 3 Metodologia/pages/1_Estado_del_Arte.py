import sys, os
sys.path.insert(0, os.getcwd())
import streamlit as st
from ui_theme import setup_page, stat, hr, highlight, pilar, card_borde, nav_buttons

setup_page("Estado del Arte | Trabajo 3")

st.markdown("# Estado del Arte")
st.markdown(hr(), unsafe_allow_html=True)

tab_prob, tab_avbr, tab_fund = st.tabs(["Problema", "Avances y Brechas", "Enfoque Propuesto"])

# ── PROBLEMA ──────────────────────────────────────────────────────────────────
with tab_prob:
    col_texto, col_stat = st.columns([1.6, 1], gap="large")
    with col_texto:
        st.markdown(
            "La invasion de Rusia sobre Ucrania (24 feb 2022) hizo **inviable cualquier "
            "trabajo de campo**: campos minados, combates activos y territorios ocupados. "
            "La comunidad cientifica debio depender exclusivamente de **metodos remotos** "
            "para documentar el impacto (Scher & Van Den Hoek, 2025; Wagner et al., 2025)."
        )
        st.markdown(
            highlight(
                "<strong>Estado del Arte:</strong> evidencia "
                "tres frentes metodologicos dominantes - deteccion de cambios coherentes con "
                "SAR (Sentinel-1) para daño urbano, modelado contrafactual con sensores "
                "opticos (Sentinel-2/Landsat) para abandono agricola, y analisis de luz "
                "nocturna (VIIRS) para apagones y desplazamiento. Estos tres frentes se "
                "concentran en los oblasts orientales y meridionales de Ucrania (Donetsk, "
                "Luhansk, Jerson y Zaporiyia), las mismas zonas que este proyecto busca "
                "contrastar mediante clustering de eventos de combate."
            ),
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            highlight(
                "<strong>Relevancia para Ciencia de Datos:</strong> Integrar fuentes "
                "georreferenciadas heterogeneas (ACLED + satelites multisensor), aplicar "
                "clustering no supervisado sin etiquetas previas, y evaluar resultados con "
                "metricas cuantitativas en ausencia de datos de campo verificables."
            ),
            unsafe_allow_html=True,
        )
    with col_stat:
        st.markdown(stat("2.4 M ha", "tierras agricolas abandonadas"), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(stat("264 km2", "area urbana destruida"), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(stat("84 %", "caida luz nocturna nacional"), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(stat("6.33 M", "personas desplazadas"), unsafe_allow_html=True)

# ── AVANCES Y BRECHAS ─────────────────────────────────────────────────────────
with tab_avbr:
    avances = [
        ("CCD con Sentinel-1",
         "264 km2 de daño urbano en 2,288+ asentamientos. 67% a menos de 10 km del frente.",
         "Scher & Van Den Hoek (2025); Huang et al. (2023)",
         "Mariupol y frente este (Donetsk/Luhansk)"),
        ("Modelado contrafactual con ML",
         "2.34-2.40 M ha agricolas abandonadas. 82.6% de perdida en area de siembra de girasol.",
         "Wagner et al. (2025); Li et al. (2026); Qiu et al. (2026)",
         "Donetsk y Luhansk (este de Ucrania)"),
        ("Luz nocturna VIIRS diaria",
         "Caida del 84% en intensidad luminica nacional. Cronologia de la ofensiva sobre Kiev.",
         "Wang et al. (2024); Xiao et al. (2024); Lin et al. (2024)",
         "Kiev y zonas orientales (escala nacional)"),
        ("Cruce ACLED + satelite",
         "Los trabajos que incorporan ACLED establecen relaciones causales entre distancia al frente y magnitud del daño.",
         "Tomchenko et al. (2023); Kganyago et al. (2025); Wagner et al. (2025)",
         "Zonas cercanas al frente (incendios y abandono agricola)"),
    ]
    for titulo, hallazgo, cita, zona in avances:
        st.markdown(
            f"<div style='border-left:3px solid rgba(0,188,212,0.5);padding:12px 18px;"
            f"background:rgba(255,255,255,0.02);border-radius:0 8px 8px 0;margin-bottom:10px'>"
            f"<p style='color:#00BCD4;font-weight:700;margin:0 0 4px 0'>{titulo} "
            f"<span style='color:#7aadcc;font-weight:400;font-size:0.78rem'>&middot; {zona}</span></p>"
            f"<p style='color:#c0d8ef;font-size:0.93rem;margin:0 0 3px 0'>{hallazgo}</p>"
            f"<p style='color:#5a8aaa;font-size:0.82rem;font-style:italic;margin:0'>{cita}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<div style='border-left:4px solid #E53935;padding:20px 24px;"
        "background:rgba(229,57,53,0.05);border-radius:0 10px 10px 0;margin-bottom:18px'>"
        "<p style='color:#ef9a9a;font-weight:700;font-size:1rem;margin:0 0 8px 0'>"
        "Ningun estudio usa el evento de combate como unidad de analisis primaria</p>"
        "<p style='color:#a0bdd4;font-size:0.95rem;margin:0;line-height:1.65'>"
        "Los 36 articulos parten del daño satelital para inferir la actividad belica. "
        "Los que incorporan ACLED (Tomchenko 2023, Wagner 2025, Kganyago 2025) lo usan solo "
        "como cruce de validacion, nunca como insumo primario de clustering espacial."
        "</p></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        highlight("Consecuencia: no existe un indice de intensidad territorial construido desde "
                  "los propios eventos de combate. Todos van de satelite a terreno; nadie hace "
                  "el recorrido inverso. Esta brecha genera directamente la pregunta de investigacion."),
        unsafe_allow_html=True,
    )

# ── ENFOQUE PROPUESTO ─────────────────────────────────────────────────────────
with tab_fund:
    st.markdown(
        "Estas son las herramientas y conceptos que este proyecto propone aplicar, en "
        "contraste con el enfoque dominante en la literatura revisada."
    )
    st.markdown("<br>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3, gap="large")
    with p1:
        st.markdown(pilar("#00BCD4", "ACLED",
            "Repositorio georreferenciado de eventos belicos: bombardeos, combates "
            "terrestres y explosiones, con precision a nivel de localidad y resolucion "
            "temporal diaria. En la literatura se usa solo como variable auxiliar de "
            "validacion, nunca como insumo primario de clustering."), unsafe_allow_html=True)
    with p2:
        st.markdown(pilar("#0288D5", "K-Means",
            "Agrupa eventos por proximidad geografica minimizando la inercia interna. "
            "El numero de clusters k se ajusta con la curva del codo. "
            "Asigna todos los puntos a algun cluster, sin concepto de ruido."), unsafe_allow_html=True)
    with p3:
        st.markdown(pilar("#CE93D8", "DBSCAN",
            "Identifica zonas densas con geometria arbitraria. Marca eventos aislados "
            "como ruido (clase -1). No requiere especificar k. "
            "Ideal para distribuciones irregulares propias de eventos belicos."), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2 = st.columns(2, gap="large")
    with m1:
        st.markdown(card_borde("#00BCD4", "Coeficiente de silueta",
            "Rango [-1, 1]. Valores cercanos a 1 indican clusters compactos y bien separados."), unsafe_allow_html=True)
    with m2:
        st.markdown(card_borde("#F9A825", "Indice de Davies-Bouldin",
            "Valores mas bajos indican mejor separacion. Compara K-Means vs DBSCAN directamente."), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe({
        "Satelite": ["Sentinel-1 (SAR)", "Sentinel-2 (optico)", "VIIRS / Black Marble"],
        "Uso principal": ["CCD - daño urbano", "NDVI, NDWI, areas quemadas", "Apagones, desplazamiento"],
        "Zona": ["Mariupol y frente este", "Donetsk y Luhansk", "Kiev y zonas orientales"],
        "Referencia clave": ["Scher & Van Den Hoek (2025)", "Wagner et al. (2025)", "Wang et al. (2024)"],
    }, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        highlight(
            "<strong>De la teoria a este proyecto:</strong> la literatura usa ACLED solo como "
            "cruce de validacion y estos sensores para medir el daño desde el satelite, "
            "principalmente en los oblasts orientales y meridionales de Ucrania. Este "
            "proyecto propone invertir el orden: aplicar K-Means y DBSCAN sobre ACLED para caracterizar "
            "primero el combate desde el terreno en esas mismas zonas, el lado del problema "
            "que el estado del arte no cubre."
        ),
        unsafe_allow_html=True,
    )

# ── NAVEGACION ─────────────────────────────────────────────────────────────
nav_buttons("Portada.py", "Portada", "pages/2_Pregunta_e_Hipotesis.py", "Pregunta e Hipótesis")
