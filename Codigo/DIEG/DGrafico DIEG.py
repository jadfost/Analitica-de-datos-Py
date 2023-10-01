import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Cargar los datos de DIEG Encuentros
data_dieg_encuentros = pd.read_csv('Datos/DIEG/DIEG Encuentros.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    # Título de la aplicación
    html.H1("Visualización de Datos para DIEG Encuentros"),

    # Dropdown para seleccionar el programa académico de DIEG Encuentros
    html.Div([
        html.H2("Selecciona un programa académico para DIEG Encuentros:"),
        dcc.Dropdown(
            id='programa-dropdown-encuentros',
            options=[
                {'label': programa, 'value': programa} for programa in data_dieg_encuentros['FACULTAD'].unique() if pd.notna(programa)
            ],
            value=data_dieg_encuentros['FACULTAD'].iloc[0]
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    # Gráfico circular para DIEG Encuentros
    html.Div([
        html.H2("Porcentaje de Participación en DIEG Encuentros por Año"),
        dcc.Graph(id='pie-chart-encuentros')
    ], style={'width': '48%', 'display': 'inline-block'}),

    # Texto explicativo
    html.Div([
        html.H2("Explicación del Gráfico"),
        html.P("Este gráfico circular muestra el número de participantes en el encuentro por año para el programa académico seleccionado. Cada porción del gráfico representa un año, y el tamaño de cada porción es proporcional al número de participantes en ese año."),
    ], style={'width': '48%', 'display': 'inline-block'}),
])

# Función para crear el gráfico circular para DIEG Encuentros
@app.callback(
    Output('pie-chart-encuentros', 'figure'),
    Input('programa-dropdown-encuentros', 'value')
)
def update_pie_chart_encuentros(selected_programa):
    filtered_data = data_dieg_encuentros[data_dieg_encuentros['FACULTAD'] == selected_programa]
    years = filtered_data['AÑO']
    participants = filtered_data['NÚMERO DE PARTICIPANTES EN EL ENCUENTRO']
    
    fig = go.Figure(data=[go.Pie(labels=years, values=participants)])
    fig.update_layout(title="Porcentaje de Participación en DIEG Encuentros por Año")
    
    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
