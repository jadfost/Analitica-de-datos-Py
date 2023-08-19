import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


# Leer el archivo CSV con los datos de OCME
data_ocme = pd.read_csv('Datos/OCME/OCME 10-18.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Visualización de Datos OCME'),
    html.P("Selecciona una variable de analisis:"),
    dcc.Dropdown(
        id='campo-dropdown',
        options=[{'label': columna, 'value': columna} for columna in data_ocme.columns],
        value='AÑO/PERIODO',  # Cambiado a 'AÑO/PERIODO'
        multi=False
    ),
    dcc.Graph(id='grafico-barras')
])

# Crear una función para actualizar el gráfico de barras
@app.callback(
    Output('grafico-barras', 'figure'),
    Input('campo-dropdown', 'value')
)
def actualizar_grafico(campo_seleccionado):
    if campo_seleccionado is not None:
        fig = px.bar(data_ocme, x=campo_seleccionado, title=f'Gráfico de barras para {campo_seleccionado}')
    else:
        fig = px.bar()  # Gráfico vacío si no se ha seleccionado un campo

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
