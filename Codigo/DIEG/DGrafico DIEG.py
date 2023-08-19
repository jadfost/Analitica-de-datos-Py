import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos de DIEG PIONEROS y DIEG DISTINGUIDOS
data_dieg_pioneros = pd.read_csv('Datos/DIEG/DIEG PIONEROS.csv')
data_dieg_distinguidos = pd.read_csv('Datos/DIEG/DIEG Distinguidos.csv')


# Agregar una columna 'Origen' a cada DataFrame para identificar el origen de los datos
data_dieg_pioneros['Origen'] = 'Pioneros'
data_dieg_distinguidos['Origen'] = 'Distinguidos'

# Combinar los datos de ambas tablas
data_combinada = pd.concat([data_dieg_pioneros, data_dieg_distinguidos])

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.P("Selecciona un programa académico:"),
    dcc.Dropdown(
        id='programa-dropdown',
        options=[{'label': programa, 'value': programa} for programa in data_combinada['PROGRAMA ACADÉMICO'].unique()],
        value='PIME',  # Valor inicial
        multi=False
    ),
    html.P("Selecciona el campo a comparar:"),
    dcc.Dropdown(
        id='columna-dropdown',
        multi=False
    ),
    dcc.Graph(id='grafico-circular')
])

# Crear una función para actualizar las opciones del filtro de columnas
@app.callback(
    Output('columna-dropdown', 'options'),
    Input('programa-dropdown', 'value')
)
def actualizar_columnas(programa_seleccionado):
    if programa_seleccionado is not None:
        columnas = data_combinada[data_combinada['PROGRAMA ACADÉMICO'] == programa_seleccionado].columns
    else:
        columnas = []

    opciones = [{'label': columna, 'value': columna} for columna in columnas]
    return opciones

# Crear una función para actualizar el gráfico circular
@app.callback(
    Output('grafico-circular', 'figure'),
    Input('columna-dropdown', 'value'),
    Input('programa-dropdown', 'value')
)
def actualizar_grafico(columna_seleccionada, programa_seleccionado):
    if programa_seleccionado is not None:
        data_filtrada = data_combinada[data_combinada['PROGRAMA ACADÉMICO'] == programa_seleccionado]

        if columna_seleccionada is not None:
            fig = px.pie(data_filtrada, names=columna_seleccionada, title=f'Distribución de {columna_seleccionada}')
        else:
            fig = px.pie()  # Gráfico vacío si no se ha seleccionado una columna
    else:
        fig = px.pie()  # Gráfico vacío si no se ha seleccionado un programa académico

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)