import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos desde los archivos CSV en DataFrames
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv')
df_estudiantes = pd.read_csv('Datos/DIRI/DIRI Mov.estudiantil.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Visualización de Datos DIRI'),
    html.P('Selecciona una tabla:'),
    dcc.Dropdown(
        id='tabla-dropdown',
        options=[
            {'label': 'Docentes', 'value': 'docentes'},
            {'label': 'Estudiantes', 'value': 'estudiantes'}
        ],
        value='docentes',  # Valor inicial
        multi=False
    ),
    html.P('Selecciona una variable de análisis:'),
    dcc.Dropdown(
        id='campo-dropdown',
        multi=False
    ),
    dcc.Graph(id='grafico-circular')
])

# Crear una función para actualizar las opciones del menú desplegable de campos
@app.callback(
    Output('campo-dropdown', 'options'),
    Input('tabla-dropdown', 'value')
)
def actualizar_campos_disponibles(tabla_seleccionada):
    if tabla_seleccionada == 'docentes':
        columnas_disponibles = df_docentes.columns
    elif tabla_seleccionada == 'estudiantes':
        columnas_disponibles = df_estudiantes.columns
    else:
        columnas_disponibles = []

    opciones = [{'label': columna, 'value': columna} for columna in columnas_disponibles]
    return opciones

# Crear una función para actualizar el gráfico circular
@app.callback(
    Output('grafico-circular', 'figure'),
    Input('tabla-dropdown', 'value'),
    Input('campo-dropdown', 'value')
)
def actualizar_grafico(tabla_seleccionada, campo_seleccionado):
    if tabla_seleccionada == 'docentes':
        data = df_docentes
        titulo = 'Docentes'
    elif tabla_seleccionada == 'estudiantes':
        data = df_estudiantes
        titulo = 'Estudiantes'
    else:
        data = pd.DataFrame()
        titulo = ''

    # Filtrar filas con campos vacíos en la columna seleccionada
    if not data.empty and campo_seleccionado in data.columns:
        data = data.dropna(subset=[campo_seleccionado])

    if not data.empty and campo_seleccionado in data.columns:
        fig = px.pie(data, names=campo_seleccionado, title=f'{titulo} - {campo_seleccionado}')
    else:
        fig = px.pie()  # Gráfico circular vacío si no se ha seleccionado una tabla o campo válido

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
