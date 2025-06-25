from translate import Translator
import streamlit as st

st.title("Chinese ↔ English Translator")
text = st.text_area("Enter text:")
option = st.selectbox("Translate to:", ["chinese", "english"])

if st.button("Translate"):
  if option=="chinese":
    translator = Translator(to_lang="en")
  elif option=="english":
    translator = Translator(to_lang="zh")
  try:
    result = translator.translate(text)
    st.write("Translation:", result)
  except Exception as e:
    st.error(f"Error during translation: {e}")

