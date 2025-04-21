import streamlit as st
import pandas as pd
import plotly.express as px

def show_sheets_page():
    st.image("Logo_Auto_Hall.png", width=180, caption="Logo Auto Hall")
    st.title("List Depart Auto Hall 2025")

    # 🔗 Lien vers Google Sheets (en CSV)
    sheet_id = "1JUDA-tJpzyUpDSXb-daKN7ACVAP7LUboRVVplQD34eA"
    sheet_name = "listdepart"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        # 📥 Lecture des données
        df = pd.read_csv(url)
        st.success("✅ Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)

       # Comptage des fonctions
fonctions_count = df["Fonction"].value_counts().reset_index()
fonctions_count.columns = ["Fonction", "Nombre"]

# Séparation entre ceux avec plusieurs départs et ceux avec 1 seul
majoritaires = fonctions_count[fonctions_count["Nombre"] > 1]
autres_total = fonctions_count[fonctions_count["Nombre"] == 1]["Nombre"].sum()

# Ajout d’une ligne "Autres" si nécessaire
if autres_total > 0:
    autres_row = pd.DataFrame([["Autres", autres_total]], columns=["Fonction", "Nombre"])
    fonctions_count_grouped = pd.concat([majoritaires, autres_row], ignore_index=True)
else:
    fonctions_count_grouped = majoritaires

# Pie chart
st.subheader("📌 Répartition des départs par Fonction (avec regroupement)")
fig_fonctions = px.pie(fonctions_count_grouped, 
                       names="Fonction", 
                       values="Nombre", 
                       title="Départs par Fonction (regroupés)")
st.plotly_chart(fig_fonctions)


        # 📊 2. Pie chart : Répartition par motif
        st.subheader("📌 Répartition des motifs de départ")
        motifs_count = df["Motif de départ"].value_counts().reset_index()
        motifs_count.columns = ["Motif", "Nombre"]
        fig_motifs = px.pie(motifs_count, names="Motif", values="Nombre", title="Motifs de départ")
        st.plotly_chart(fig_motifs)

        # 📊 3. Bar chart groupé : Fonction → Motif
        st.subheader("📌 Répartition des motifs selon les fonctions (Bar Chart)")
        grouped = df.groupby(["Fonction", "Motif de départ"]).size().reset_index(name="Nombre")
        fig_bar = px.bar(grouped, 
                         x="Fonction", 
                         y="Nombre", 
                         color="Motif de départ", 
                         barmode="group", 
                         title="Motifs de départ par Fonction")
        st.plotly_chart(fig_bar)


    except Exception as e:
        st.error(f"❌ Erreur lors du chargement des données : {e}")

# 🚀 Appel de la fonction
show_sheets_page()
