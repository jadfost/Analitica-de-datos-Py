import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Cargar los datos de DIEG PIONEROS (actualiza la ruta del archivo CSV)
data_dieg_pioneros = pd.read_csv('Datos/DIEG/DIEG PIONEROS.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    # Título de la aplicación
    html.H1("Visualización de Participantes en el Encuentro para DIEG PIONEROS"),

    # Selección de programa académico
    html.P("Selecciona un programa académico:"),
    dcc.Dropdown(
        id='programa-dropdown',
        options=[{'label': programa, 'value': programa} for programa in data_dieg_pioneros['PROGRAMA ACADÉMICO'].unique()],
        value='PIME',  # Cambia el valor inicial según tus datos
        multi=False
    ),

    # Selección de sede
    html.P("Selecciona una Sede:"),
    dcc.Dropdown(
        id='sede-dropdown',
        options=[{'label': sede, 'value': sede} for sede in data_dieg_pioneros['SEDE'].unique()],
        value='Tunja',  # Cambia el valor inicial según tus datos
        multi=False
    ),

    # Gráfico de barras
    dcc.Graph(id='bar-chart'),

    # Explicación del gráfico
    html.Div([
        html.P("Este gráfico muestra la cantidad de participantes en el Encuentro para el programa académico y sede seleccionados a lo largo de varios años."),
        html.P("Cada barra representa un año específico y la altura de la barra corresponde al número de participantes en ese año."),
        html.P("Las barras están agrupadas por año, lo que facilita la comparación de la participación a lo largo del tiempo."),
        html.P("El título del gráfico indica el programa académico y la sede seleccionados, proporcionando un contexto claro para los datos presentados.")
    ], style={'margin-top': '20px'})
])

# Crear una función para actualizar el gráfico en función de las selecciones de los filtros
@app.callback(
    Output('bar-chart', 'figure'),
    Input('programa-dropdown', 'value'),
    Input('sede-dropdown', 'value')
)
def update_graph(selected_programa, selected_sede):
    filtered_data = data_dieg_pioneros[(data_dieg_pioneros['PROGRAMA ACADÉMICO'] == selected_programa) &
                                       (data_dieg_pioneros['SEDE'] == selected_sede)]
    
    years = data_dieg_pioneros.columns[3:]
    
    data = []
    for year in years:
        data.append(go.Bar(
            x=[year],
            y=[filtered_data[year].sum()],
            name=year
        ))
    
    layout = go.Layout(
        title=f'Participantes en el Encuentro para {selected_programa} en {selected_sede}',
        barmode='group'  # Cambia a 'stack' para un gráfico de barras apiladas
    )
    
    return {'data': data, 'layout': layout}

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
