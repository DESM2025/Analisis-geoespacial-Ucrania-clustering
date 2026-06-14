import base64
import os

import streamlit as st


def setup_page(title: str) -> None:
    st.set_page_config(page_title=title, layout="wide")
    apply_theme()
    add_sidebar_footer()


def apply_theme() -> None:
    st.markdown(
        """
<style>
.stApp {
    background: linear-gradient(160deg, #060d1a 0%, #0b1c30 45%, #0f2540 100%);
    color: #d8ecf9;
}
[data-testid="stAppViewContainer"] { color: #d8ecf9; }
h1, h2, h3 { color: #f0f8ff !important; letter-spacing: -0.3px; }
section.main .block-container {
    font-size: 1.18rem !important;
    padding-top: 2.2rem;
    max-width: 1100px;
}
section.main .block-container h1 { font-size: 3.1rem !important; line-height: 1.1 !important; }
section.main .block-container h2 { font-size: 2.15rem !important; line-height: 1.15 !important; }
section.main .block-container h3 { font-size: 1.55rem !important; line-height: 1.2 !important; }
section.main .block-container p,
section.main .block-container li,
section.main .block-container label,
section.main .block-container [data-testid="stMarkdownContainer"] p,
section.main .block-container [data-testid="stMarkdownContainer"] li {
    color: #c0d8ef;
    font-size: 1.15rem !important;
    line-height: 1.72 !important;
}
section[data-testid="stSidebar"] {
    background: #04090f;
    border-right: 1px solid rgba(0, 188, 212, 0.12);
}
[data-testid="stSidebarNav"] { border-bottom: none !important; }
section[data-testid="stSidebar"] hr { display: none !important; }
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
.c-line {
    border: none;
    border-top: 1px solid rgba(0, 188, 212, 0.3);
    margin: 1.8rem 0;
}
.badge {
    display: inline-block;
    background: rgba(0, 188, 212, 0.15);
    border: 1px solid rgba(0, 188, 212, 0.35);
    border-radius: 20px;
    padding: 3px 14px;
    font-size: 0.82rem;
    color: #00BCD4;
    margin: 3px 3px 3px 0;
}
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
div[data-testid="stAlert"] {
    background: rgba(0, 188, 212, 0.08) !important;
    border: 1px solid rgba(0, 188, 212, 0.28) !important;
    color: #d8ecf9 !important;
}
[data-testid="stDataFrame"] { background: rgba(255,255,255,0.02) !important; }
button[data-baseweb="tab"] { color: #7aadcc !important; background: transparent !important; }
button[data-baseweb="tab"][aria-selected="true"] {
    color: #00BCD4 !important;
    border-bottom: 2px solid #00BCD4 !important;
}
.sidebar-footer {
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(0,188,212,0.18);
    font-size: 0.75rem;
    line-height: 1.5;
    color: #5a8aaa;
}
.sidebar-logo-card {
    display: inline-block;
    margin-top: 12px;
    padding: 10px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,188,212,0.15);
    border-radius: 10px;
}
.sidebar-logo-card img {
    display: block;
    width: 48px;
    height: auto;
}
</style>
""",
        unsafe_allow_html=True,
    )


def _logo_b64() -> str:
    logo_path = os.path.join(os.path.dirname(__file__), "fotos", "Logo-UTEM-1.png")
    with open(logo_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def img_b64(filename: str) -> str:
    img_path = os.path.join(os.path.dirname(__file__), "fotos", filename)
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def add_sidebar_footer() -> None:
    with st.sidebar:
        st.markdown(
            "<div class='sidebar-footer'>"
            "Diego E. Silva Madariaga<br>"
            "Metodologia de Investigacion<br>"
            "en Ciencia de Datos<br>"
            "UTEM &middot; 1er Semestre 2026"
            "<div class='sidebar-logo-card'>"
            f"<img src='data:image/png;base64,{_logo_b64()}'>"
            "</div>"
            "</div>",
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


def pilar(color: str, titulo: str, texto: str) -> str:
    return (
        f"<div style='border-top:3px solid {color};border:1px solid rgba(255,255,255,0.07);"
        f"border-radius:8px;padding:22px 20px;background:rgba(255,255,255,0.02);height:100%'>"
        f"<p style='color:{color};font-weight:700;font-size:1rem;margin:0 0 10px 0'>{titulo}</p>"
        f"<p style='color:#a0bdd4;font-size:0.93rem;margin:0;line-height:1.6'>{texto}</p></div>"
    )


def card_borde(color: str, titulo: str, texto: str) -> str:
    return (
        f"<div style='border-left:3px solid {color};padding:14px 20px;"
        f"background:rgba(255,255,255,0.02);border-radius:0 8px 8px 0;margin-bottom:12px'>"
        f"<p style='color:{color};font-weight:700;margin:0 0 6px 0'>{titulo}</p>"
        f"<p style='color:#c0d8ef;font-size:0.95rem;margin:0'>{texto}</p></div>"
    )


def nav_buttons(prev_page: str, prev_label: str, next_page: str, next_label: str) -> None:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(hr(), unsafe_allow_html=True)
    col_prev, _, col_next = st.columns([1, 2, 1])
    with col_prev:
        st.page_link(prev_page, label=f"← {prev_label}", use_container_width=True)
    with col_next:
        st.page_link(next_page, label=f"{next_label} →", use_container_width=True)
