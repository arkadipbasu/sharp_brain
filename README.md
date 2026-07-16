# Pattern Vault — Streamlit Edition

Same game, same features, now hostable online with Streamlit.

- `app.py` — Streamlit entry point. Embeds the game via `streamlit.components.v1.html`.
- `pattern_vault_game.html` — the original game (HTML/CSS/JS), unchanged. All logic —
  Memory Vault (Sequence Vault, Digit Span, Spatial Recall) and Data Sprint
  (Odd One Out, Number Chain, Compare, Percent Snap, Closest to Average),
  scoring, streaks, adaptive difficulty, and the session dashboard — runs
  exactly as it did as a standalone HTML file. Streamlit just serves it.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL Streamlit prints (usually http://localhost:8501).

## Deploy online (Streamlit Community Cloud)

1. Push this folder (`app.py`, `pattern_vault_game.html`, `requirements.txt`) to a GitHub repo.
2. Go to https://share.streamlit.io, sign in, and click "New app".
3. Point it at the repo and set the main file to `app.py`.
4. Deploy — you'll get a public URL to share.

Any other Streamlit-compatible host (Render, Hugging Face Spaces with the
Streamlit SDK, your own server via `streamlit run app.py --server.port ...`)
works the same way — just keep `app.py` and `pattern_vault_game.html` in the
same directory.

## Notes

- The game keeps all state (score, streak, history) in the browser via
  JavaScript, same as before — it resets on page refresh. If you want
  scores to persist server-side across sessions/users, that would need a
  rework to move state into Streamlit's `st.session_state` and a backing
  store, which changes the interaction model from the original real-time
  JS game (flashing tiles, countdown timers) to a rerun-based one.
