st.title("Análisis del Dataset Credit")
 
# Cargar los datos desde GitHub
df = pd.read_csv("https://raw.githubusercontent.com/giuliannaac/ejercicio/main/Credit.csv")
 
# Eliminar la columna innecesaria
df.drop(columns=["Unnamed: 0"], inplace=True)
 
# Mostrar información del dataset
st.write("### Información General del Dataset")
st.write(df.info())
 
# Gráfico de distribución de la variable Balance
st.write("### Distribución de la Variable Balance")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Balance"], bins=30, kde=True, color='blue', ax=ax)
ax.set_title("Distribución de la Variable Balance")
ax.set_xlabel("Balance")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
 
# Matriz de correlación
st.write("### Matriz de Correlación")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)
 
# Relación entre Balance y Variables Categóricas
st.write("### Relación entre Balance y Variables Categóricas")
categorical_vars = ["Gender", "Student", "Married", "Ethnicity"]
 
fig, axes = plt.subplots(2, 2, figsize=(15, 8))
for i, var in enumerate(categorical_vars):
    sns.boxplot(x=df[var], y=df["Balance"], hue=df[var], palette="Set2", ax=axes[i//2, i%2])
    axes[i//2, i%2].set_title(f"Balance por {var}")
st.pyplot(fig)
 
# Cálculo de VIF (colinealidad)
st.write("### Análisis de Colinealidad (VIF)")
num_vars = ["Income", "Limit", "Rating", "Cards", "Age", "Education"]
X = df[num_vars]
 
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
 
st.write(vif_data)
