import streamlit as st
import backend

st.title('Poem Generator')

mood = st.sidebar.selectbox("Pick a mood", ("Sad", "Happy", "Summer", "Romantic", "Optimistic", "Anger"))

if mood:
    name, peom = backend.peom_gen(mood)
    st.header(name)
    st.write(peom)

