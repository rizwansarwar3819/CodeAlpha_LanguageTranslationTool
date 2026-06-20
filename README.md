# CodeAlpha AI Internship — Task Submissions

## Task 1: Language Translation Tool
**File:** `CodeAlpha_LanguageTranslationTool.py`

### How to run
```bash
pip install -r requirements_translation.txt
python CodeAlpha_LanguageTranslationTool.py
```
Run with `--cli` flag for command-line mode instead of GUI:
```bash
python CodeAlpha_LanguageTranslationTool.py --cli
```

### How it works
- Uses the free Google Translate engine via the `deep-translator` library (no API key needed).
- User enters text, picks a source & target language from a Tkinter GUI dropdown.
- Click "Translate" → text is sent to Google Translate → result displayed.
- Includes a "Copy Result" button.


