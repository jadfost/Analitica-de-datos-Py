import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Cargar los datos de DIEG Encuentros
data_dieg_encuentros = pd.read_csv('Datos/DIEG/DIEG Encuentros.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Estilo CSS
app.css.append_css({'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'})

# Definir el diseño de la aplicación
app.layout = html.Div([
    # Barra de navegación
    html.Nav([
        html.Div([
            html.H1("Visualización de Datos para DIEG Encuentros", className="navbar-brand"),
        ], className="container"),
    ], className="navbar navbar-dark bg-primary"),

    # Contenedor principal
    html.Div([
        # Fila 1
        html.Div([
            # Columna 1 - Selector de programa académico
            html.Div([
                html.Label("Selecciona un programa académico para DIEG Encuentros:"),
                dcc.Dropdown(
                    id='programa-dropdown-encuentros',
                    options=[
                        {'label': programa, 'value': programa} for programa in data_dieg_encuentros['FACULTAD'].unique() if pd.notna(programa)
                    ],
                    value=data_dieg_encuentros['FACULTAD'].iloc[0]
                )
            ], className="col-md-4"),
            
            # Columna 2 - Gráfico circular
            html.Div([
                dcc.Graph(id='pie-chart-encuentros'),
            ], className="col-md-8"),
        ], className="row"),

        # Fila 2 - Texto explicativo
        html.Div([
            html.Div([
                html.H2("Explicación del Gráfico"),
                html.P("Este gráfico circular muestra el número de participantes en el encuentro por año para el programa académico seleccionado. Cada porción del gráfico representa un año, y el tamaño de cada porción es proporcional al número de participantes en ese año."),
            ], className="col-md-12"),
        ], className="row"),
    ], className="container"),
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
