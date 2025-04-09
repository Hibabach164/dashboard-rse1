
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données avec l'encodage adapté
df = pd.read_csv("donnees_rse_1.csv", encoding="ISO-8859-1")

# Nettoyage des colonnes
df.columns = df.columns.str.strip()

# Affichage du titre
st.title("scores")

# Exemple simple de traitement
if "Entreprise" in df.columns:
    entreprises = df["Entreprise"].unique()
    st.write("Entreprises disponibles :", entreprises)
    selected = st.selectbox("Choisir une entreprise", entreprises)
    filtered = df[df["Entreprise"] == selected]
    st.dataframe(filtered)
else:
    st.error("Colonne 'Entreprise' non trouvée dans les données.")
