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
    html.P("Selecciona una variable de análisis:"),
    dcc.Dropdown(
        id='campo-dropdown',
        options=[{'label': columna, 'value': columna} for columna in data_ocme.columns],
        value='AÑO/PERIODO',  # Cambiado a 'AÑO/PERIODO'
        multi=False
    ),
    dcc.Graph(id='grafico-barras'),
    html.Div(id='descripcion-grafico')  # Aquí mostraremos la descripción del gráfico
])

# Función para obtener una descripción del campo seleccionado
def obtener_descripcion(campo_seleccionado):
    # Puedes agregar aquí descripciones para cada campo seleccionado
    descripciones = {
    'AÑO/PERIODO': 'Esta gráfica muestra la evolución a lo largo de los años/periodos.',
    'NOMBRE DE LOS MEDIOS DE DIVULGACIÓN': 'Esta gráfica muestra el nombre de los medios de divulgación y la cantidad de veces utilizados.',
    'LUGAR DE DIVULGACIÓN': 'Esta gráfica muestra el lugar de divulgación de la información y la cantidad de veces que se realizo.',
    'PROPÓSITO DEL MEDIO UTILIZADO': 'Esta gráfica muestra el propósito del medio y la cantidad de veces utilizado.',
    'NÚMERO APROX. DE PERSONAS INFORMADAS': 'Esta gráfica muestra el número aproximado de personas informadas.'
}
    return descripciones.get(campo_seleccionado, 'Descripción no disponible para este campo.')

# Crear una función para actualizar el gráfico de barras y la descripción
@app.callback(
    [Output('grafico-barras', 'figure'),
     Output('descripcion-grafico', 'children')],
    Input('campo-dropdown', 'value')
)
def actualizar_grafico(campo_seleccionado):
    if campo_seleccionado is not None:
        fig = px.bar(data_ocme, x=campo_seleccionado, title=f'Gráfico de barras para {campo_seleccionado}')
        descripcion = obtener_descripcion(campo_seleccionado)
        # Ajustar la orientación de las etiquetas en el eje x
        fig.update_xaxes(tickangle=45)  # Cambia el ángulo a 45 grados para mejorar la legibilidad
    else:
        fig = px.bar()  # Gráfico vacío si no se ha seleccionado un campo
        descripcion = 'Selecciona una variable para mostrar su gráfico y descripción.'

    return fig, descripcion

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
