from deep_translator import GoogleTranslator
import streamlit as st

st.title("Translator")
text = st.text_area("Enter text:")
option = st.selectbox("Translate to:", ["Chinese","Traditional Chinese", "English","Japanese","Korean"])

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter text to translate.")
    else:
        if option == "Chinese":
            target = 'zh-CN'
        elif option == "Traditional Chinese":
            target = 'zh-TW'
        elif option == "Japanese":
            target = 'ja'
        elif option == "Korean":
            target = 'ko'
        else:  # English
            target = 'en'
        try:
            result = GoogleTranslator(source='auto', target=target).translate(text)
            st.write("Translation:", result)
        except Exception as e:
            st.error(f"Error during translation: {e}")
