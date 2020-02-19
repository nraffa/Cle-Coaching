import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

app = dash.Dash()

colors = {
    'background':'#11111',
    'text': '#7FDBFH'
}
markdown_text = '''

![Image](https://static.wixstatic.com/media/d055e6_da809208202942c4894cefdd3e6d802f~mv2_d_1775_1550_s_2.jpg/v1/crop/x_0,y_61,w_1775,h_1452/fill/w_90,h_79,al_c,q_80,usm_0.66_1.00_0.01/d055e6_da809208202942c4894cefdd3e6d802f~mv2_d_1775_1550_s_2.webp)

*Descubre cuál alimento primario te falta y cómo puedes infundir dicha y satisfacción en tu vida.*
'''
nombres =  np.array(['Vida Social' , 'Relaciones' , 'Alegria'])

app.layout = html.Div(style = {'backgroundColor' : colors['background']}, children= 
    [html.H1(children='Circulo de la Vida', style = {
        'color' : colors['text']
    }),
    
    dcc.Markdown(children = markdown_text),
    html.Label('''Vida Social:
    ''') ,
    dcc.Input(id = 'vida-social' , value = 1 , type = 'number'),
    html.Label('''Relaciones:
    ''') ,
    dcc.Input(id = 'relaciones' , value = 1 , type = 'number'),
    html.Label(''' Alegria:
    ''') ,
    dcc.Input(id = 'alegria', value = 2 , type = 'number'),

    dcc.Graph(id='grafico')
])

@app.callback(
    Output('grafico', 'figure'),
    [Input('vida-social', 'value'),
    Input('relaciones', 'value'),
    Input('alegria', 'value')]
)
def update_output_div(i1 , i2 ,i12):

    return { 
        'data': [            
                {'values': [i1, i2,i12], 'type': 'pie', 'name': nombres }
            ],
            'layout': {
                'title' : '',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'] ,
                'font': {
                    'color': colors['text']},
                'transition' : {'duration' : 2000}
            }
            
        } 
    
    


if __name__ == '__main__':
    app.run_server(debug=True)