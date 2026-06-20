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

---

## Task 2: FAQ Chatbot
**File:** `CodeAlpha_ChatbotFAQs.py`

### How to run
```bash
pip install -r requirements_chatbot.txt
python CodeAlpha_ChatbotFAQs.py
```
Run with `--cli` flag for command-line mode:
```bash
python CodeAlpha_ChatbotFAQs.py --cli
```

### How it works
1. A list of FAQ (question, answer) pairs is stored in `FAQ_DATA`.
2. NLTK preprocesses both the FAQs and the user's question (lowercase, remove
   punctuation, tokenize, remove stopwords).
3. scikit-learn's `TfidfVectorizer` converts all questions into numeric vectors.
4. `cosine_similarity` compares the user's question vector against every FAQ
   question vector to find the closest match.
5. If the similarity score is above a threshold (0.25), the matching FAQ's
   answer is returned in the chat window. Otherwise a fallback message is shown.

### Sample questions you can ask the chatbot
- How do I reset my password?
- How can I create an account?
- What payment methods do you accept?
- How do I cancel my subscription?
- Is there a free trial available?
- How long does shipping take?
- How do I track my order?
- What is your return policy?
- How do I contact customer support?
- Do you offer student discounts?
- What browsers are supported?
- How do I update my profile information?

You don't have to type these exact words — the chatbot uses similarity matching,
so rephrased versions (e.g. "How do I get my money back?" instead of "What is
your return policy?") will still match the correct answer.

