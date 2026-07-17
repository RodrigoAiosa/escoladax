"""
styles/seo.py
Injeta meta tags básicas de SEO (título, descrição, idioma) na página Streamlit.

Este arquivo estava referenciado em styles/__init__.py mas não existia no
repositório — isso causava o erro:
    ModuleNotFoundError: No module named 'styles.seo'
ao rodar `streamlit run app.py`, pois styles/__init__.py importa este módulo
incondicionalmente.
"""

import streamlit as st

_META = {
    "pt": {
        "description": (
            "BI Data Generator PRO — gere dados fictícios em modelo estrela "
            "(fato + dimensões) para 55 setores de negócio diferentes, prontos "
            "para praticar Power BI, DAX e modelagem dimensional."
        ),
        "lang": "pt-BR",
    },
    "en": {
        "description": (
            "BI Data Generator PRO — generate fictional star-schema data "
            "(fact + dimension tables) for 55 different business sectors, "
            "ready to practice Power BI, DAX and dimensional modeling."
        ),
        "lang": "en",
    },
}


def inject_seo(lang: str = "pt") -> None:
    """Injeta meta tags de SEO (description, idioma) no <head> da página."""
    info = _META.get(lang, _META["pt"])
    st.markdown(
        f"""
        <meta name="description" content="{info['description']}">
        <meta http-equiv="content-language" content="{info['lang']}">
        <script>
            document.documentElement.lang = "{info['lang']}";
        </script>
        """,
        unsafe_allow_html=True,
    )
