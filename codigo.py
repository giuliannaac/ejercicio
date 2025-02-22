df = pd.read_csv("Credit.csv")
df.drop(columns=["Unnamed: 0"], inplace=True)
# Ver información general del dataset
df.info()
plt.figure(figsize=(8, 5))
sns.histplot(df["Balance"], bins=30, kde=True, color='blue')
plt.title("Distribución de la Variable Balance")
plt.xlabel("Balance")
plt.ylabel("Frecuencia")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación entre Variables Numéricas")
plt.show()

# Relación entre la variable balance y las variables categóricas
categorical_vars = ["Gender", "Student", "Married", "Ethnicity"]

plt.figure(figsize=(15, 8))
for i, var in enumerate(categorical_vars, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x=df[var], y=df["Balance"], hue=df[var], palette="Set2", legend=False)
    plt.title(f"Balance por {var}")
    plt.xlabel(var)
    plt.ylabel("Balance")
plt.tight_layout()
plt.show()

# Análisis de colinealidad (VIF) Se excluyen las variables categóricas porque el VIF solo se aplica a variables numéricas
num_vars = ["Income", "Limit", "Rating", "Cards", "Age", "Education"]
X = df[num_vars]

# Calcular VIF
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

