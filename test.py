
import streamlit as st
st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")
nom = st.text_input("**1-Quel est votre nom ?**")
if nom:
    st.success("Enchanté, {} !".format(nom))
age= st.slider("**2-entrez votre age svp?**",0,100,50)
st.write(f"votre age est: {age} ans ")
genre = st.radio("**3-Quel est votre genre ?**", ["Homme", "Femme"])
st.write(f"Genre choisi : {genre}")
st.write('**4-comment vous trouvez notre service?**')
if st.checkbox("je suis satisfait(e) "):
    st.write("✔️ merci pour votre visite !")
else:
    st.write("❌ je ne suis pas satisfait(e).")

if st.button("save"):
    st.balloons()