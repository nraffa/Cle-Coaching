import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

x = 1
y = 1
z = 1

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Cle Coaching'),

    html.H4(children='''
        Descubre cuál alimento primario te falta y cómo puedes infundir dicha y satisfacción en tu vida. 
    '''),
    
    html.Div(children='''
        Vida Social:
    '''),

    dcc.Input(id='input1', value='', type='number')
    

    

])

@app.callback(
    Output('example-graph', 'figure'),
    [Input("input1", "value")]
)
def update_figure(input_data):
    x = input_data
        
    return dcc.Graph(
        id = 'example-graph',
        figure = {
            'data': [
                {'x': input_data, 'type': 'pie', 'name': 'Vida Social'},
            ],
            'layout': {
                'title': 'Circulo de la Vida'
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)

    
#Input(component_id='input1', component_property='value')


#    dcc.Graph(
 #       id='example-graph',
  #      figure={
   #         'data': [
                
    #            {'values': [x], 'type': 'pie', 'name': ['Vida Social', 'Relaciones','Ambiente']},
     #       ],
      #      'layout': {
       #         'title': 'Circulo de la Vida'
        #    }
        #}
    #)