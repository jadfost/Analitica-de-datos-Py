import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Cargar los datos de DIEG Distinguidos y DIEG Pioneros
data_dieg_distinguidos = pd.read_csv('Datos/DIEG/DIEG Distinguidos.csv')
data_dieg_pioneros = pd.read_csv('Datos/DIEG/DIEG PIONEROS.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    # Título de la aplicación
    html.H1("Visualización de graficos"),

    html.P("Selecciona un programa académico (Distinguidos):"),
    dcc.Dropdown(
        id='programa-dropdown-distinguidos',
        options=[{'label': programa, 'value': programa} for programa in data_dieg_distinguidos['PROGRAMA ACADÉMICO'].unique()],
        value='PARQ',  # Cambia el valor inicial según tus datos
        multi=False
    ),
    html.Div(id='distinguidos-explanation', style={'margin-top': '20px'}),
    dcc.Graph(id='pie-chart-distinguidos'),
    
    html.P("Selecciona un programa académico (Pioneros):"),
    dcc.Dropdown(
        id='programa-dropdown-pioneros',
        options=[{'label': programa, 'value': programa} for programa in data_dieg_pioneros['PROGRAMA ACADÉMICO'].unique()],
        value='PIME',  # Cambia el valor inicial según tus datos
        multi=False
    ),
    html.Div(id='pioneros-explanation', style={'margin-top': '20px'}),
    dcc.Graph(id='pie-chart-pioneros')
])

# Función para crear gráfico circular
def create_pie_chart(data, selected_programa, title):
    filtered_data = data[data['PROGRAMA ACADÉMICO'] == selected_programa]
    total_values = filtered_data.iloc[:, 3:].sum()
    
    labels = total_values.index
    values = total_values.values
    
    pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values)])
    pie_chart.update_traces(hole=0.3)  # Agregar el agujero al gráfico circular
    pie_chart.update_layout(title=title)  # Agregar título al gráfico
    
    return pie_chart

# Crear una función para actualizar los gráficos en función de las selecciones de los filtros
@app.callback(
    Output('pie-chart-distinguidos', 'figure'),
    Output('pie-chart-pioneros', 'figure'),
    Output('distinguidos-explanation', 'children'),
    Output('pioneros-explanation', 'children'),
    Input('programa-dropdown-distinguidos', 'value'),
    Input('programa-dropdown-pioneros', 'value')
)
def update_pie_charts(selected_programa_distinguidos, selected_programa_pioneros):
    pie_chart_distinguidos = create_pie_chart(data_dieg_distinguidos, selected_programa_distinguidos, "Distribución de Valores en Distinguidos")
    pie_chart_pioneros = create_pie_chart(data_dieg_pioneros, selected_programa_pioneros, "Distribución de Valores en Pioneros")
    
    distinguidos_explanation = "Este gráfico muestra cómo se distribuyen los valores en el programa académico 'Distinguidos' seleccionado. Cada porción representa un año, y el tamaño de cada porción es proporcional a la suma de los valores para ese año."
    pioneros_explanation = "Este gráfico muestra cómo se distribuyen los valores en el programa académico 'Pioneros' seleccionado. Cada porción representa un año, y el tamaño de cada porción es proporcional a la suma de los valores para ese año."
    
    return pie_chart_distinguidos, pie_chart_pioneros, distinguidos_explanation, pioneros_explanation

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
