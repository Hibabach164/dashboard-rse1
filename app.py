
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard RSE", layout="wide")

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("donnees_rse_1.csv", encoding="ISO-8859-1")

df = load_data()

st.title("🌿 Tableau de bord RSE - Visualisation interactive")

# Filtres interactifs
col1, col2 = st.columns(2)
entreprise_select = col1.selectbox("Choisir une entreprise", ["Toutes"] + sorted(df["Entreprise"].unique().tolist()))
theme_select = col2.selectbox("Choisir un thème RSE", ["Tous"] + sorted(df["Thème RSE"].unique().tolist()))

df_filtered = df.copy()
if entreprise_select != "Toutes":
    df_filtered = df_filtered[df_filtered["Entreprise"] == entreprise_select]
if theme_select != "Tous":
    df_filtered = df_filtered[df_filtered["Thème RSE"] == theme_select]

# Score moyen
mean_score = df_filtered["Score RSE"].astype(str).str.replace(",", ".").astype(float).mean()
st.metric(label="Score RSE moyen", value=f"{mean_score:.1f} / 100")

# Barres thématiques
st.subheader("🔎 Score RSE moyen par thème")
df_bar = df_filtered.copy()
df_bar["Score RSE"] = df_bar["Score RSE"].astype(str).str.replace(",", ".").astype(float)
bar_data = df_bar.groupby("Thème RSE")["Score RSE"].mean().reset_index()

fig_bar = px.bar(bar_data, x="Thème RSE", y="Score RSE", color="Thème RSE", title="Score RSE moyen par thème",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig_bar, use_container_width=True)

# Matrice (Heatmap)
st.subheader("🔥 Carte de chaleur RSE (entreprises x thèmes)")
df_heat = df_filtered.copy()
df_heat["Score RSE"] = df_heat["Score RSE"].astype(str).str.replace(",", ".").astype(float)
heat_data = df_heat.pivot_table(index="Entreprise", columns="Thème RSE", values="Score RSE", aggfunc="mean")

st.dataframe(heat_data.style.background_gradient(cmap='RdYlGn'), use_container_width=True)

# Pied de page
st.markdown("---")
st.markdown("📊 Réalisé avec Streamlit | Données RSE simulées pour mémoire")
