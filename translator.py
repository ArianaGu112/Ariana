import streamlit as st
from deep_translator import GoogleTranslator

st.title("Chinese ↔ English Translator")
text = st.text_area("Enter text:")
option = st.selectbox("Translate to:", ["Chinese", "English"])

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter text to translate.")
    else:
        target = 'zh-cn' if option == "Chinese" else 'en'
        try:
            result = GoogleTranslator(source='auto', target=target).translate(text)
            st.write("Translation:", result)
        except Exception as e:
            st.error(f"Error during translation: {e}")

