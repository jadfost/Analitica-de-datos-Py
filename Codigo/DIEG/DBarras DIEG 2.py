import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos de DIEG PIONEROS
data_dieg_pioneros = pd.read_csv('Datos/DIEG/DIEG PIONEROS.csv')

# Crear una nueva columna 'NUM_PARTICIPANTES' que suma los valores de los años
data_dieg_pioneros['NUM_PARTICIPANTES'] = data_dieg_pioneros[['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021-10', '2021-20']].sum(axis=1)

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.P("Selecciona un programa académico:"),
    dcc.Dropdown(
        id='programa-dropdown',  # Cambiar el ID del filtro
        options=[{'label': programa, 'value': programa} for programa in data_dieg_pioneros['PROGRAMA ACADÉMICO'].unique()],  # Cambiar la columna de opciones
        value='PIME',  # Valor inicial
        multi=False
    ),
    html.P("Selecciona una Sede:"),
    dcc.Dropdown(
        id='sede-dropdown',
        options=[{'label': sede, 'value': sede} for sede in data_dieg_pioneros['SEDE'].unique()],
        value='Tunja',
        multi=False
    ),
    html.P("Selecciona un Año:"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in data_dieg_pioneros.columns[3:]],
        value='2014',
        multi=False
    ),
    dcc.Graph(id='bar-chart')
])

# Crear una función para actualizar el gráfico en función de las selecciones de los filtros
@app.callback(
    Output('bar-chart', 'figure'),
    Input('programa-dropdown', 'value'),  # Cambiar la entrada del filtro
    Input('sede-dropdown', 'value'),
    Input('year-dropdown', 'value')
)
def update_graph(selected_programa, selected_sede, selected_year):
    filtered_data = data_dieg_pioneros[(data_dieg_pioneros['PROGRAMA ACADÉMICO'] == selected_programa) &  # Cambiar la columna de filtro
                                       (data_dieg_pioneros['SEDE'] == selected_sede)]
    
    fig = px.bar(filtered_data, x=selected_year, y='NUM_PARTICIPANTES',
                 title=f'Participantes en el Encuentro para {selected_programa} en {selected_sede}')  # Cambiar el título
    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
