import streamlit as st
import pandas as pd
import plotly.express as px

def show_sheets_page():
    st.title("Lecture de Google Sheets dans Streamlit")

    # Remplace cet ID par celui de ta feuille Google Sheets
    sheet_id = "1JUDA-tJpzyUpDSXb-daKN7ACVAP7LUboRVVplQD34eA"
    sheet_name = "listdepart"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)

        # 👇 Affichage du graphique en barres
        # Remplace 'NomColonneX' et 'NomColonneY' par les noms réels
        col_x = "Fonction"
        col_y = "Motif de départ"

        # Vérifier que les colonnes existent
        if col_x in df.columns and col_y in df.columns:
            fig = px.bar(df, x=col_x, y=col_y, title=f"{col_y} par {col_x}")
            st.plotly_chart(fig)
        else:
            st.warning("Les colonnes spécifiées n'existent pas dans la feuille Google Sheets.")

    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")

# Appel de la fonction
show_sheets_page()