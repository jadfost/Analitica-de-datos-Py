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
        titulo = 'Docentes con Mayor Población'
        columna_entrante_nacional = 'PE - Docente Nacional'
        columna_entrante_internacional = 'PE - Docente Internacional'
        columna_saliente_nacional = 'PS - Docente Nacional'
        columna_saliente_internacional = 'PS - Docente Internacional'
    elif tabla_seleccionada == 'estudiantes':
        data = df_estudiantes
        titulo = 'Estudiantes con Mayor Población'
        columna_entrante_nacional = 'PE - Estudiantes Nacional'
        columna_entrante_internacional = 'PE - Estudiantes Internacional'
        columna_saliente_nacional = 'PS - Estudiantes Nacional'
        columna_saliente_internacional = 'PS - Estudiantes Internacional'
    else:
        data = pd.DataFrame()
        titulo = ''

    if not data.empty:
        # Combinar las columnas de población entrante y saliente en una sola columna
        data['Poblacion'] = data[columna_entrante_nacional] + data[columna_entrante_internacional] + data[columna_saliente_nacional] + data[columna_saliente_internacional]
        
        # Ordenar los datos por población en orden descendente
        data_ordenada = data.sort_values(by=['Poblacion'], ascending=False)
        
        # Tomar los 5 primeros registros con mayor población
        data_top_5 = data_ordenada.head(5)
        
        # Crear un gráfico circular para mostrar los nombres de las personas
        fig = px.pie(data_top_5, names='Poblacion', 
                     title=f'{titulo} - Población Entrante y Saliente', 
                     labels={'Poblacion': 'Nombre'})
    else:
        fig = px.pie()  # Gráfico vacío si no se ha seleccionado una tabla

    return fig

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)