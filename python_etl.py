import pandas as pd
# Crear datos dummy
data = {
'Fecha': pd.date_range(start='2024-01-01', periods=20),
'Producto': np.random.choice(['Producto A', 'Producto B', 'Producto C'], size=20),
'Cantidad': np.random.randint(1, 100, size=20),
'Precio_Unitario': np.random.uniform(10, 100, size=20)
}

# Crear DataFrame
df_ventas = pd.DataFrame(data)

# Mostrar DataFrame
print(df_ventas)
