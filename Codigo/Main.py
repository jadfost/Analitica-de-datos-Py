import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Panel de Navegación'),
    dcc.Dropdown(
        id='script-dropdown',
        options=[
            {'label': 'Script 1', 'value': 'script1.py'},
            {'label': 'Script 2', 'value': 'script2.py'},
            # Agrega más scripts aquí
        ],
        value=None,  # Valor inicial
        multi=False
    ),
    dcc.Graph(id='output-graph')
])

# Crear una función para ejecutar scripts
def ejecutar_script(script):
    try:
        # Ejecutar el script deseado
        exec(open(script).read(), globals())
    except Exception as e:
        print(f"Error al ejecutar el script {script}: {e}")

# Crear una función de callback para actualizar el gráfico según el script seleccionado
@app.callback(
    Output('output-graph', 'figure'),
    Input('script-dropdown', 'value')
)
def actualizar_grafico(script_seleccionado):
    if script_seleccionado:
        ejecutar_script(script_seleccionado)
        # Puedes agregar lógica adicional para mostrar el resultado del script en un gráfico si es necesario

    # Retorna un gráfico vacío como un marcador de posición
    return {}

# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
