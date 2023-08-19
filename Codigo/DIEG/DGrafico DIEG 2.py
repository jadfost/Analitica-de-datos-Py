import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos de DIEG PIONEROS y DIEG DISTINGUIDOS
data_dieg_pioneros = pd.read_csv('Datos/DIEG/DIEG PIONEROS.csv')
data_dieg_distinguidos = pd.read_csv('Datos/DIEG/DIEG Distinguidos.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.P("Selecciona una tabla de DIEG:"),
    dcc.Dropdown(
        id='tabla-dropdown',
        options=[
            {'label': 'DIEG PIONEROS', 'value': 'pioneros'},
            {'label': 'DIEG DISTINGUIDOS', 'value': 'distinguidos'}
        ],
        value='pioneros',  # Valor inicial
        multi=False
    ),
    html.P("Selecciona un programa académico:"),
    dcc.Dropdown(
        id='programa-dropdown',
        options=[{'label': programa, 'value': programa} for programa in data_dieg_pioneros['PROGRAMA ACADÉMICO'].unique()],
        value='PIME',  # Valor inicial
        multi=False
    ),
    html.P("Selecciona una variable de Analisis:"),
    dcc.Dropdown(
        id='columna-dropdown',
        multi=False
    ),
    dcc.Graph(id='grafico-circular')
])

# Crear una función para actualizar las opciones del filtro de columnas
@app.callback(
    Output('columna-dropdown', 'options'),
    Input('tabla-dropdown', 'value'),
    Input('programa-dropdown', 'value')
)
def actualizar_columnas(tabla_seleccionada, programa_seleccionado):
    if tabla_seleccionada == 'pioneros':
        data = data_dieg_pioneros
    elif tabla_seleccionada == 'distinguidos':
        data = data_dieg_distinguidos
    else:
        data = pd.DataFrame()  # Vacío si no se ha seleccionado una tabla

    if programa_seleccionado is not None:
        columnas = data[data['PROGRAMA ACADÉMICO'] == programa_seleccionado].columns
    else:
        columnas = []

    opciones = [{'label': columna, 'value': columna} for columna in columnas]
    return opciones

# Crear una función para actualizar el gráfico circular
@app.callback(
    Output('grafico-circular', 'figure'),
    Input('tabla-dropdown', 'value'),
    Input('columna-dropdown', 'value'),
    Input('programa-dropdown', 'value')
)
def actualizar_grafico(tabla_seleccionada, columna_seleccionada, programa_seleccionado):
    if tabla_seleccionada == 'pioneros':
        data = data_dieg_pioneros
    elif tabla_seleccionada == 'distinguidos':
        data = data_dieg_distinguidos
    else:
        data = pd.DataFrame()  # Vacío si no se ha seleccionado una tabla

    if programa_seleccionado is not None:
        data = data[data['PROGRAMA ACADÉMICO'] == programa_seleccionado]

    if columna_seleccionada is not None:
        fig = px.pie(data, names=columna_seleccionada, title=f'Distribución de {columna_seleccionada}')
    else:
        fig = px.pie()  # Gráfico vacío si no se ha seleccionado una columna

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
