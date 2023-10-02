import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos desde los archivos CSV
df1 = pd.read_csv('Datos/DIRS/DIRS 1.csv')
df2 = pd.read_csv('Datos/DIRS/DIRS 2.csv')
df3 = pd.read_csv('Datos/DIRS/DIRS 3.csv')
df4 = pd.read_csv('Datos/DIRS/DIRS 4.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Visualización de Datos DIRS'),
    html.P("Selecciona una tabla de DIRS para visualizar datos relevantes."),
    dcc.Dropdown(
        id='tabla-dropdown',
        options=[
            {'label': 'DIRS 1 - Proyectos de Proyección Social', 'value': 'DIRS 1'},
            {'label': 'DIRS 2 - Alternativas de Grado', 'value': 'DIRS 2'},
            {'label': 'DIRS 3 - Prácticas y Comunidad', 'value': 'DIRS 3'},
            {'label': 'DIRS 4 - Actividades y Comunidad', 'value': 'DIRS 4'},
        ],
        value='DIRS 1',  # Valor inicial: Tabla 1
        multi=False
    ),
    html.P("Selecciona una variable de análisis para obtener información relevante."),
    dcc.Dropdown(
        id='campo-dropdown',
        multi=False
    ),
    dcc.Graph(id='grafico-barras')
])

# Crear una función para actualizar las opciones del filtro de columnas
@app.callback(
    Output('campo-dropdown', 'options'),
    Input('tabla-dropdown', 'value')
)
def actualizar_columnas(tabla_seleccionada):
    df_seleccionado = df1  # Por defecto, seleccionar la tabla 1
    if tabla_seleccionada == 'DIRS 2':
        df_seleccionado = df2
    elif tabla_seleccionada == 'DIRS 3':
        df_seleccionado = df3
    elif tabla_seleccionada == 'DIRS 4':
        df_seleccionado = df4
    columnas = df_seleccionado.columns

    opciones = [{'label': columna, 'value': columna} for columna in columnas]
    return opciones

# Crear una función para actualizar el gráfico de barras
@app.callback(
    Output('grafico-barras', 'figure'),
    Input('tabla-dropdown', 'value'),
    Input('campo-dropdown', 'value')
)
def actualizar_grafico(tabla_seleccionada, campo_seleccionado):
    df_seleccionado = df1  # Por defecto, seleccionar la tabla 1
    if tabla_seleccionada == 'DIRS 2':
        df_seleccionado = df2
    elif tabla_seleccionada == 'DIRS 3':
        df_seleccionado = df3
    elif tabla_seleccionada == 'DIRS 4':
        df_seleccionado = df4

    if campo_seleccionado is not None:
        titulo_grafico = f'Distribución de {campo_seleccionado} en {tabla_seleccionada}'
        fig = px.bar(df_seleccionado, x=campo_seleccionado, title=titulo_grafico)
    else:
        fig = px.bar()  # Gráfico vacío si no se ha seleccionado una columna

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
