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
    dcc.Dropdown(
        id='tabla-dropdown',
        options=[
            {'label': 'Docentes', 'value': 'docentes'},
            {'label': 'Estudiantes', 'value': 'estudiantes'}
        ],
        value='docentes',  # Valor inicial
        multi=False
    ),
    dcc.Dropdown(
        id='campo-dropdown',
        options=[{'label': columna, 'value': columna} for columna in df_docentes.columns],
        value='PE  Periodo movilidad',  # Valor inicial
        multi=False
    ),
    dcc.Graph(id='grafico-barras')
])

# Crear una función para actualizar el gráfico de barras
@app.callback(
    Output('grafico-barras', 'figure'),
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

    if not data.empty and campo_seleccionado in data.columns:
        fig = px.bar(data, x=campo_seleccionado, title=f'{titulo} - {campo_seleccionado}')
    else:
        fig = px.bar()  # Gráfico vacío si no se ha seleccionado una tabla o campo válido

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)