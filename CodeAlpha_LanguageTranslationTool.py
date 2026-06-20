"""
CodeAlpha Artificial Intelligence Internship
Task 1: Language Translation Tool
---------------------------------------------
Description:
A command-line / simple GUI based Language Translation Tool that lets a user
enter text, choose a source and target language, and get the translated text
using the free Google Translate engine (via the `deep-translator` library).

Author: CodeAlpha Intern
"""

from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------------------------------------------
# Supported languages (code : full name) — feel free to add more from
# deep_translator.GoogleTranslator().get_supported_languages(as_dict=True)
# -------------------------------------------------------------------
LANGUAGES = {
    "auto": "Auto Detect",
    "en": "English",
    "ur": "Urdu",
    "ar": "Arabic",
    "hi": "Hindi",
    "pa": "Punjabi",
    "bn": "Bengali",
    "fa": "Persian",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "tr": "Turkish",
    "nl": "Dutch",
    "pl": "Polish",
}

NAME_TO_CODE = {v: k for k, v in LANGUAGES.items()}


def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """
    Translates `text` from `source_lang` to `target_lang` using
    Google Translate (free, no API key required).
    """
    if not text.strip():
        return ""
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)


# -------------------------------------------------------------------
# Simple Tkinter GUI
# -------------------------------------------------------------------
class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translation Tool - CodeAlpha")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="🌐 Language Translation Tool",
            font=("Segoe UI", 18, "bold"),
            bg="#f0f4f8",
            fg="#2d3a8c",
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self.root,
            text="CodeAlpha AI Internship - Task 1",
            font=("Segoe UI", 10),
            bg="#f0f4f8",
            fg="#666666",
        )
        subtitle.pack(pady=(0, 15))

        # ---- Language selection row ----
        lang_frame = tk.Frame(self.root, bg="#f0f4f8")
        lang_frame.pack(pady=5)

        tk.Label(lang_frame, text="From:", bg="#f0f4f8", font=("Segoe UI", 10)).grid(
            row=0, column=0, padx=5
        )
        self.src_lang = ttk.Combobox(
            lang_frame, values=list(LANGUAGES.values()), width=18, state="readonly"
        )
        self.src_lang.set("Auto Detect")
        self.src_lang.grid(row=0, column=1, padx=5)

        tk.Label(lang_frame, text="To:", bg="#f0f4f8", font=("Segoe UI", 10)).grid(
            row=0, column=2, padx=5
        )
        self.tgt_lang = ttk.Combobox(
            lang_frame,
            values=[v for k, v in LANGUAGES.items() if k != "auto"],
            width=18,
            state="readonly",
        )
        self.tgt_lang.set("Urdu")
        self.tgt_lang.grid(row=0, column=3, padx=5)

        # ---- Input text box ----
        tk.Label(
            self.root, text="Enter Text:", bg="#f0f4f8", font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=40, pady=(20, 5))

        self.input_box = tk.Text(self.root, height=6, width=62, font=("Segoe UI", 11))
        self.input_box.pack(padx=40)

        # ---- Translate button ----
        translate_btn = tk.Button(
            self.root,
            text="🔄 Translate",
            command=self.do_translate,
            bg="#2d3a8c",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
        )
        translate_btn.pack(pady=20)

        # ---- Output text box ----
        tk.Label(
            self.root,
            text="Translation:",
            bg="#f0f4f8",
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", padx=40)

        self.output_box = tk.Text(
            self.root, height=6, width=62, font=("Segoe UI", 11), bg="#f8f9ff"
        )
        self.output_box.pack(padx=40, pady=(5, 10))
        self.output_box.config(state="disabled")

        copy_btn = tk.Button(
            self.root,
            text="📋 Copy Result",
            command=self.copy_result,
            bg="#eef0fb",
            fg="#2d3a8c",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
        )
        copy_btn.pack()

    def do_translate(self):
        text = self.input_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input needed", "Please enter some text to translate.")
            return

        src_name = self.src_lang.get()
        tgt_name = self.tgt_lang.get()
        src_code = NAME_TO_CODE.get(src_name, "auto")
        tgt_code = NAME_TO_CODE.get(tgt_name, "en")

        try:
            result = translate_text(text, src_code, tgt_code)
        except Exception as e:
            messagebox.showerror("Translation Error", f"Could not translate text.\n\n{e}")
            return

        self.output_box.config(state="normal")
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, result)
        self.output_box.config(state="disabled")

    def copy_result(self):
        result = self.output_box.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            messagebox.showinfo("Copied", "Translation copied to clipboard!")


# -------------------------------------------------------------------
# CLI fallback mode (if someone wants to run without GUI)
# -------------------------------------------------------------------
def run_cli():
    print("=" * 50)
    print("  Language Translation Tool - CodeAlpha (CLI mode)")
    print("=" * 50)
    text = input("\nEnter text to translate: ")
    src = input("Source language code (or 'auto'): ").strip() or "auto"
    tgt = input("Target language code (e.g. 'ur', 'fr', 'es'): ").strip() or "en"

    try:
        translated = translate_text(text, src, tgt)
        print("\nTranslated Text:")
        print(translated)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import sys

    if "--cli" in sys.argv:
        run_cli()
    else:
        root = tk.Tk()
        app = TranslationApp(root)
        root.mainloop()
