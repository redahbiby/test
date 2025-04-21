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

        # 📊 1. Pie chart : Répartition par fonction
        st.subheader("📌 Répartition des départs par Fonction")
        fonctions_count = df["Fonction"].value_counts().reset_index()
        fonctions_count.columns = ["Fonction", "Nombre"]
        fig_fonctions = px.pie(fonctions_count, names="Fonction", values="Nombre", title="Départs par Fonction")
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

        # 🌞 4. Sunburst chart : Fonction → Motif
        st.subheader("📌 Vue hiérarchique : Fonction → Motif (Sunburst)")
        fig_sunburst = px.sunburst(grouped, 
                                   path=["Fonction", "Motif de départ"], 
                                   values="Nombre", 
                                   title="Hiérarchie des départs : Fonction → Motif")
        st.plotly_chart(fig_sunburst)

    except Exception as e:
        st.error(f"❌ Erreur lors du chargement des données : {e}")

# 🚀 Appel de la fonction
show_sheets_page()
