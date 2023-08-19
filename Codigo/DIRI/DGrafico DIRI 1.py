import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos desde los archivos CSV en DataFrames
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv')
df_mov_estudiantil = pd.read_csv('Datos/DIRI/DIRI Mov.estudiantil.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Visualización de Datos DIRI'),
    html.P("Selecciona una variable de analisis:"),
    dcc.Dropdown(
        id='tabla-dropdown',
        options=[
            {'label': 'Mov. Docente', 'value': 'docentes'},
            {'label': 'Mov. Estudiantil', 'value': 'estudiantil'}
        ],
        value='docentes',  # Valor inicial
        multi=False
    ),
    dcc.Graph(id='grafico-circular')
])

# Crear una función para actualizar el gráfico circular
@app.callback(
    Output('grafico-circular', 'figure'),
    Input('tabla-dropdown', 'value')
)
def actualizar_grafico(tabla_seleccionada):
    if tabla_seleccionada == 'docentes':
        data = df_docentes
        titulo = 'Movimiento Docente'
        columnas_relevantes = ['POBLACION ENTRANTE - NOMBRE DEL CONVENIO', 'POBLACION SALIENTE - NOMBRE DEL CONVENIO']
    elif tabla_seleccionada == 'estudiantil':
        data = df_mov_estudiantil
        titulo = 'Movimiento Estudiantil'
        columnas_relevantes = ['POBLACION ENTRANTE - NOMBRE DEL CONVENIO', 'POBLACION SALIENTE TUNJA - NOMBRE DEL CONVENIO', 'POBLACION SALIENTE SOGAMOSO -NOMBRE DEL CONVENIO']
    else:
        data = pd.DataFrame()
        titulo = ''

    if not data.empty:
        fig = px.pie(data, names=columnas_relevantes, title=f'Distribución en {titulo}')
    else:
        fig = px.pie()  # Gráfico vacío si no se ha seleccionado una tabla

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
