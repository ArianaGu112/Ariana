from deep_translator import GoogleTranslator
import streamlit as st

st.title("Chinese ↔ English Translator")
text = st.text_area("Enter text:")
option = st.selectbox("Translate to:", ["Chinese", "English"])

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter text to translate.")
    else:
        # 用大写的区域代码 'zh-CN' 或 'en'
        target = 'zh-CN' if option == "Chinese" else 'en'
        try:
            result = GoogleTranslator(source='auto', target=target).translate(text)
            st.write("Translation:", result)
        except Exception as e:
            st.error(f"Error during translation: {e}")
