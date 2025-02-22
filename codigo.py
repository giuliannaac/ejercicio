df = pd.read_csv("https://raw.githubusercontent.com/giuliannaac/ejercicio/ef67e6ec174f26cb04a9a25eb3aca9edceb42334/Credit.csv")
st.title("Titulo x")
df.drop(columns=["Unnamed: 0"], inplace=True)
# Ver información general del dataset
df.info()
st.write("### Distribución de la Variable Balance") fig, ax = plt.subplots(figsize=(8, 5)) sns.histplot(df["Balance"], bins=30, kde=True, color='blue', ax=ax) ax.set_title("Distribución de la Variable Balance") ax.set_xlabel("Balance") ax.set_ylabel("Frecuencia") 
st.pyplot(fig)
st.write("### Matriz de Correlación") fig, ax = plt.subplots(figsize=(10, 6)) sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax) 
st.pyplot(fig)
