import pandas as pd  # importo pandas

errores = [] # Inicio lista de errores

# 1- Leer y mostrar archivo CSV
df = pd.read_csv("estudios.csv")
print(df)
print()

# 2- Limpiar espacios en blanco en los campos de texto
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# 3- Convertir la columna 'Fecha' a tipo fecha (datetime)
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# 4- Validaciones
# Detectar registros con edad menor a 0 o mayor a 120
df['Edad'] = pd.to_numeric(df['Edad'], errors='coerce')
edades_invalidas = df[(df['Edad'] < 0) | (df['Edad'] > 120)]
print("Pacientes con edad inválida:")
print(edades_invalidas[['Paciente', 'Edad']])
# Si hay edades inválidas agregar mensaje a la lista de errores
if not edades_invalidas.empty:
    errores.append("Hay pacientes con edad inválida.")
print()


# Detectar registros con el campo 'Estudio' vacío
estudios_vacios = df[df['Estudio'].isna() | (df['Estudio'] == '')]

if not estudios_vacios.empty:
    print("Registros con el campo 'Estudio' vacío:")
    print(estudios_vacios[['Paciente', 'Estudio']])
    errores.append("Hay registros con el campo 'Estudio' vacío.")# agrego mensaje a la lista de errores
else:
    print("No hay registros con el campo 'Estudio' vacío.")

print()

# Detectar IDs de estudio duplicados (ID_Estudio debería ser único)
ids_duplicados = df[df.duplicated(subset=['ID_Estudio'], keep=False)]

if not ids_duplicados.empty:
    print("Registros con ID_Estudio duplicado:")
    print(ids_duplicados[['ID_Estudio']])
    errores.append("Hay IDs de estudio duplicados.")  # agrego mensaje a la lista de errores
else:
    print("No hay IDs de estudio duplicados.")

print()

# Contar estudios con estado "Fallido"
fallidos = df[df['Estado'] == 'Fallido']
print(f"Cantidad de estudios con estado 'Fallido': {len(fallidos)}")
print()

# 5- Resumen: Cantidad de estudios por tipo (excluyendo vacíos)
estudios_no_vacios = df[~df['Estudio'].isna() & (df['Estudio'] != '')]
cantidad_por_estudio = estudios_no_vacios['Estudio'].value_counts()
print("\nCantidad de estudios por tipo (excluyendo vacíos):")
print(cantidad_por_estudio)
print()

# Resumen: Rango de fechas (fecha más antigua y más reciente)
fecha_min = df['Fecha'].min()
fecha_max = df['Fecha'].max()
print(f"\nRango de fechas de los estudios: {fecha_min.date()} a {fecha_max.date()}")


# 6- Validaciones finales
# Resumen de errores
if errores:
    print("\nResumen de errores encontrados:")
    for error in errores:
        print("-", error)
else:
    print("\nTodos los datos son válidos.")