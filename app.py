"""
Pattern Vault — Streamlit host
--------------------------------
Serves the Pattern Vault memory & analytics trainer for online hosting
(e.g. Streamlit Community Cloud). All gameplay logic, visuals, and
interactivity are unchanged from the original HTML/JS build — this file
just embeds that game inside a Streamlit page so it can be deployed and
shared with a single URL.
"""

import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pattern Vault — Memory & Analytics Trainer",
    page_icon="🧠",
    layout="centered",
)

# Hide Streamlit's default chrome so the game reads as a standalone app.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 1.2rem; padding-bottom: 1rem; max-width: 980px;}
        iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

GAME_FILE = pathlib.Path(__file__).parent / "pattern_vault_game.html"
game_html = GAME_FILE.read_text(encoding="utf-8")

# Render the full game (HTML + CSS + JS) inside a sandboxed component.
# height is generous enough for the stage, dashboard, and history log
# without introducing an inner scrollbar on desktop; the page itself
# will scroll for shorter viewports/mobile.
components.html(game_html, height=1500, scrolling=True)

st.caption(
    "Runs entirely client-side in your browser — no data leaves your session, "
    "and progress resets on refresh."
)
