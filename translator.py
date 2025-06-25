from googletrans import Translator
import streamlit as st

st.title("Chinese ↔ English Translator")
text = st.text_area("Enter text:")
option = st.selectbox("Translate to:", ["Chinese", "English"])

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter text to translate.")
    else:
        translator = Translator()
        dest_lang = 'zh-cn' if option == "Chinese" else 'en'
        try:
            result = translator.translate(text, dest=dest_lang)
            st.write("Translation:", result.text)
        except Exception as e:
            st.error(f"Error during translation: {e}")

