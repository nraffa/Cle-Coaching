import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Cle Coaching'),



    html.Div(children='''
        Descubre cuál alimento primario te falta y cómo puedes infundir dicha y satisfacción en tu vida. 
    '''),

    dcc.Input(id='input', value='', type='text'),

    html.Div(id='output'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                #{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'values': [2, 5, 10], 'type': 'pie', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Circulo de la Vida'
            }
        }
    )
    

])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    return 'Vida Social: "{}"'.format(input_data)

if __name__ == '__main__':
    app.run_server(debug=True)