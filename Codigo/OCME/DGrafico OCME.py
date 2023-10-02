import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar los datos de OCME
data_ocme = pd.read_csv('Datos/OCME/OCME 10-18.csv')

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Visualización de Datos OCME'),
    html.P("Selecciona una variable combinada:"),
    dcc.Dropdown(
        id='campo-dropdown',
        options=[{'label': columna, 'value': columna} for columna in data_ocme.columns],
        value='AÑO/PERIODO',  # Cambiado a 'AÑO/PERIODO'
        multi=False
    ),
    dcc.Graph(id='grafico-circular'),
    html.Div(id='descripcion-grafico')  # Aquí mostraremos la descripción del gráfico
])

# Función para limitar la longitud de los textos en las leyendas
def limitar_longitud_textos(textos, longitud_maxima=30):
    return [texto[:longitud_maxima] + ('...' if len(texto) > longitud_maxima else '') for texto in textos]

# Función para limitar la cantidad de categorías mostradas y agrupar otras en "Otros"
def limitar_categorias(data, campo_seleccionado, max_categorias=10):
    conteo_valores = data[campo_seleccionado].value_counts()
    etiquetas = conteo_valores.index.tolist()
    valores = conteo_valores.tolist()
    
    if len(etiquetas) > max_categorias:
        etiquetas = etiquetas[:max_categorias]
        valores = valores[:max_categorias]
        etiquetas.append('Otros')
        valores.append(sum(conteo_valores[max_categorias:]))
    
    return etiquetas, valores

# Función para obtener una descripción del campo seleccionado
def obtener_descripcion(campo_seleccionado):
    descripciones = {
        'AÑO/PERIODO': 'Este gráfico circular muestra la distribución de los datos a lo largo de diferentes años o períodos.',
        'NOMBRE DE LOS MEDIOS DE DIVULGACIÓN': 'Este gráfico muestra cómo se distribuyen los datos entre los diferentes medios de divulgación utilizados.',
        'LUGAR DE DIVULGACIÓN': 'Este gráfico muestra la distribución de los datos según los lugares de divulgación.',
        'PROPÓSITO DEL MEDIO UTILIZADO': 'Este gráfico representa la distribución de datos en función del propósito del medio utilizado.',
        'NÚMERO APROX. DE PERSONAS INFORMADAS': 'Este gráfico muestra cómo se distribuye el número aproximado de personas informadas.'
    }
    return descripciones.get(campo_seleccionado, 'Descripción no disponible para este campo.')

# Crear una función para actualizar el gráfico circular y su descripción
@app.callback(
    [Output('grafico-circular', 'figure'),
     Output('descripcion-grafico', 'children')],
    Input('campo-dropdown', 'value')
)
def actualizar_grafico(campo_seleccionado):
    if campo_seleccionado is not None:
        etiquetas, valores = limitar_categorias(data_ocme, campo_seleccionado)
        etiquetas = limitar_longitud_textos(etiquetas)  # Limitar longitud de las leyendas
        fig = px.pie(names=etiquetas, values=valores, title=f'Distribución de {campo_seleccionado}')
        descripcion = obtener_descripcion(campo_seleccionado)
    else:
        fig = px.pie()  # Gráfico vacío si no se ha seleccionado un campo
        descripcion = 'Selecciona una variable para mostrar su gráfico y descripción.'

    return fig, html.P(descripcion)  # Mostrar la descripción debajo del gráfico

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
