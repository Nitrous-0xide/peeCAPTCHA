# PeeCaptcha V1 🧩

A lightweight, customizable Python library for generating simple, distorted image CAPTCHAs using Pillow (`PIL`). Designed to protect web forms (like Flask or FastAPI apps) from basic automated bots while remaining easy for humans to solve.

---

## Features ✨

* **Ambiguity Reduction:** Excludes easily confused characters (e.g., `0`, `O`, `1`, `I`, `L`) from the generated text.
* **Randomized Distortion:** Rotates individual characters at varying angles and offsets them randomly.
* **Noise Lines:** Draws random background lines over the image to hinder basic OCR scripts.
* **Pixelation Effect:** Applies downscaling and upscaling effects to obscure clean vector edges.
* **Flask Ready:** Returns an in-memory image buffer (`BytesIO`) alongside the generated text string for effortless session integration.

---

## Installation 📦

Ensure you have Pillow installed:

```bash
pip install Pillow
```
## DEMO
There is a demo program included with the library `peeCAPTCHA.py`. `app.py` and `templates/index.html` show proper usage of the library.
