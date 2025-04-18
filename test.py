import streamlit as st
import pandas as pd
import os


st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")

# 1. Nom
nom = st.text_input("**1-Quel est votre nom ?**")

# 2. Âge
age = st.slider("**2-entrez votre age svp?**", 0, 100, 50)

# 3. Genre
genre = st.radio("**3-Quel est votre genre ?**", ["Homme", "Femme"])

# 4. Satisfaction
st.write('**4-comment vous trouvez notre service?**')
satisfaction = st.checkbox("je suis satisfait(e) ")
avis = "Satisfait(e)" if satisfaction else "Non satisfait(e)"

# Bouton pour sauvegarder
if st.button("save"):
    # Créer un dictionnaire avec les données
    reponse = {
        "Nom": [nom],
        "Âge": [age],
        "Genre": [genre],
        "Satisfaction": [avis]
    }

    # Créer un DataFrame
    df = pd.DataFrame(reponse)

    # Chemin du fichier
    file_path = "reponses.xlsx"

    # Ajouter au fichier existant ou créer un nouveau
    if os.path.exists(file_path):
        old_df = pd.read_excel(file_path)
        df = pd.concat([old_df, df], ignore_index=True)

    df.to_excel(file_path, index=False)

    st.success("✔️ Réponses enregistrées avec succès dans 'reponses.xlsx' !")
    st.balloons()

# 📊 Affichage des réponses enregistrées
st.subheader("📄 Réponses déjà enregistrées")
if os.path.exists("reponses.xlsx"):
    donnees = pd.read_excel("reponses.xlsx")
    st.dataframe(donnees)
else:
    st.info("Aucune réponse enregistrée pour le moment.")
