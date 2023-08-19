import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos desde los archivos CSV
df1 = pd.read_csv('Datos/DIRS/DIRS 1.csv')
df2 = pd.read_csv('Datos/DIRS/DIRS 2.csv')
df3 = pd.read_csv('Datos/DIRS/DIRS 3.csv')
df4 = pd.read_csv('Datos/DIRS/DIRS 4.csv')

# Combinar los datos en un solo DataFrame
data_combinada = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Visualización de Datos DIRS'),
    html.P("Selecciona una variable combinada:"),
    dcc.Dropdown(
        id='campo-dropdown',
        options=[{'label': columna, 'value': columna} for columna in data_combinada.columns],
        value=data_combinada.columns[0],  # Valor inicial: primera columna
        multi=False
    ),
    dcc.Graph(id='grafico-circular')
])

# Crear una función para actualizar el gráfico circular
@app.callback(
    Output('grafico-circular', 'figure'),
    Input('campo-dropdown', 'value')
)
def actualizar_grafico(campo_seleccionado):
    fig = px.pie(data_combinada, names=campo_seleccionado, title=f'Distribución de {campo_seleccionado}')
    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
