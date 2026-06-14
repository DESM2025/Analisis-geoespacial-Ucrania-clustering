import streamlit as st
from pathlib import Path

# Rutas base
_UTILS      = Path(__file__).parent          # pages/utils/
_APP_DIR    = _UTILS.parent.parent           # streamlit_app/
PROJECT_DIR = _APP_DIR.parent               # Trabajo 2 Metodologia/
CAPTURAS    = PROJECT_DIR / "Capturas"
PRISMA_IMG  = PROJECT_DIR / "prisma" / "prisma.png"


def setup_page(title: str) -> None:
    st.set_page_config(page_title=title, layout="wide")
    apply_theme()
    add_sidebar_footer()


def apply_theme() -> None:
    st.markdown(
        """
<style>
/* ── Fondo ── */
.stApp {
    background: linear-gradient(160deg, #060d1a 0%, #0b1c30 45%, #0f2540 100%);
    color: #d8ecf9;
}
[data-testid="stAppViewContainer"] { color: #d8ecf9; }

/* ── Tipografía ── */
h1, h2, h3 { color: #f0f8ff !important; letter-spacing: -0.3px; }

section.main .block-container {
    font-size: 1.18rem !important;
    padding-top: 2.2rem;
    max-width: 1100px;
}
section.main .block-container h1 {
    font-size: 3.1rem !important;
    line-height: 1.1  !important;
}
section.main .block-container h2 {
    font-size: 2.15rem !important;
    line-height: 1.15 !important;
}
section.main .block-container h3 {
    font-size: 1.55rem !important;
    line-height: 1.2  !important;
}
section.main .block-container p,
section.main .block-container li,
section.main .block-container label,
section.main .block-container [data-testid="stMarkdownContainer"] p,
section.main .block-container [data-testid="stMarkdownContainer"] li {
    color: #c0d8ef;
    font-size: 1.15rem !important;
    line-height: 1.72  !important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #04090f;
    border-right: 1px solid rgba(0, 188, 212, 0.12);
}
section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* ── Tarjetas de stat ── */
.stat {
    background  : rgba(0, 188, 212, 0.07);
    border      : 1px solid rgba(0, 188, 212, 0.22);
    border-top  : 3px solid #00BCD4;
    border-radius: 8px;
    padding     : 18px 22px;
    margin      : 7px 0;
}
.stat-n { font-size: 2.5rem; font-weight: 700; color: #00BCD4; line-height: 1.1; }
.stat-l { font-size: 0.86rem; color: #7aadcc; margin-top: 5px; }

/* ── Separador ── */
.c-line {
    border: none;
    border-top: 1px solid rgba(0, 188, 212, 0.3);
    margin: 1.8rem 0;
}

/* ── Pill badge ── */
.badge {
    display      : inline-block;
    background   : rgba(0, 188, 212, 0.15);
    border       : 1px solid rgba(0, 188, 212, 0.35);
    border-radius: 20px;
    padding      : 3px 14px;
    font-size    : 0.82rem;
    color        : #00BCD4;
    margin       : 3px 3px 3px 0;
}

/* ── Bloque de cita / highlight ── */
.highlight {
    border-left  : 3px solid #00BCD4;
    background   : rgba(0, 188, 212, 0.06);
    border-radius: 0 6px 6px 0;
    padding      : 14px 18px;
    margin       : 12px 0;
    color        : #d0e8f5;
    font-size    : 1.08rem !important;
    line-height  : 1.65 !important;
}

/* ── Alerts / info ── */
div[data-testid="stAlert"] {
    background: rgba(0, 188, 212, 0.08) !important;
    border    : 1px solid rgba(0, 188, 212, 0.28) !important;
    color     : #d8ecf9 !important;
}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.02) !important;
}

/* ── Tabs ── */
button[data-baseweb="tab"] { color: #7aadcc !important; background: transparent !important; }
button[data-baseweb="tab"][aria-selected="true"] {
    color       : #00BCD4 !important;
    border-bottom: 2px solid #00BCD4 !important;
}

/* ── Code ── */
.stCodeBlock pre { background: rgba(0,0,0,0.35) !important; }

/* ── Sidebar footer ── */
.sidebar-spacer { flex: 1; }
.sidebar-footer {
    margin-top : 1rem;
    padding-top: 0.75rem;
    border-top : 1px solid rgba(0,188,212,0.18);
    font-size  : 0.75rem;
    line-height: 1.5;
    color      : #5a8aaa;
}
</style>
""",
        unsafe_allow_html=True,
    )


def add_sidebar_footer() -> None:
    with st.sidebar:
        st.markdown('<div class="sidebar-spacer"></div>', unsafe_allow_html=True)
        st.markdown(
            """
<div class="sidebar-footer">
    Diego E. Silva Madariaga<br>
    Metodología de Investigación<br>
    en Ciencia de Datos<br>
    UTEM · 1er Semestre 2026
</div>
""",
            unsafe_allow_html=True,
        )


def stat(num: str, lbl: str) -> str:
    return (
        f"<div class='stat'>"
        f"<div class='stat-n'>{num}</div>"
        f"<div class='stat-l'>{lbl}</div>"
        f"</div>"
    )


def hr() -> str:
    return "<hr class='c-line'>"


def badge(text: str) -> str:
    return f"<span class='badge'>{text}</span>"


def highlight(text: str) -> str:
    return f"<div class='highlight'>{text}</div>"


def show_img(filename: str, caption: str = "") -> None:
    ruta = CAPTURAS / filename
    if ruta.exists():
        st.image(str(ruta), caption=caption, use_container_width=True)
    else:
        st.caption(f"_(imagen no encontrada: {filename})_")
