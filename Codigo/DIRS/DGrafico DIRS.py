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
    html.P("Selecciona una variable combinada para ver su distribución:"),
    dcc.Dropdown(
        id='campo-dropdown',
        options=[{'label': columna[:20], 'value': columna} for columna in data_combinada.columns],  # Limitar a 20 caracteres
        value=data_combinada.columns[0],  # Valor inicial: primera columna
        multi=False
    ),
    dcc.Graph(id='grafico-circular'),
    html.Div(id='descripcion-grafico')  # Aquí mostraremos la descripción del gráfico
])

# Crear una función para limitar la cantidad de categorías mostradas y agrupar otras en "Otros"
def limitar_categorias(data, campo_seleccionado, max_categorias=10):
    conteo_valores = data[campo_seleccionado].value_counts()
    etiquetas = conteo_valores.index.tolist()[:max_categorias]
    valores = conteo_valores.tolist()[:max_categorias]
    
    if len(conteo_valores) > max_categorias:
        etiquetas.append('Otros')
        valores.append(sum(conteo_valores[max_categorias:]))
    
    return etiquetas, valores

# Crear una función para actualizar el gráfico circular y su descripción
@app.callback(
    [Output('grafico-circular', 'figure'), Output('descripcion-grafico', 'children')],
    Input('campo-dropdown', 'value')
)
def actualizar_grafico(campo_seleccionado):
    etiquetas, valores = limitar_categorias(data_combinada, campo_seleccionado)
    fig = px.pie(names=etiquetas, values=valores, title=f'Distribución de {campo_seleccionado}')
    
    descripcion = f"A continuación, se presenta la distribución de la variable '{campo_seleccionado}'. Este gráfico muestra cómo se divide la variable en diferentes categorías."
    
    return fig, html.P(descripcion)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
