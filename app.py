import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "age": [25, 30, 35, 40, 45],
    "salaire": [50000, 60000, 70000, 80000, 90000],
    "experience": [2, 5, 8, 10, 12]
}
df = pd.DataFrame(data)
df.to_csv("app_data.csv", index=False)




st.title('Visualisation des données avec Streamlit')
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données")
    st.write(df.head())

    x_col = st.selectbox("Choisissez la colonne pour l'axe X", df.columns)
    y_col = st.selectbox("Choisissez la colonne pour l'axe Y", df.columns)


    st.write(f"Graphique de {x_col} vs {y_col}")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    st.pyplot(plt)