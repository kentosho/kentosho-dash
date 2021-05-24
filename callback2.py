import dash  
import dash_core_components as dcc   
import dash_html_components as html
import plotly.graph_objs as go  
import pandas as pd 
import json 

df = pd.read_csv('./data/longform.csv', index_col=0)
dfhokkaido = df[df['area']=='北海道']

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div(
        html.H1('北海道のGDP、人口、一人あたりGDPの推移',
        style = {'textAlign': 'center'})
    ),
    # 付け足し①
    html.Div(
        html.H1(id='add-hover-data')
    ),
    dcc.RadioItems(
        id = 'dropdown-for-hokkaido',
        options = [{'label': i, 'value': i} for i in dfhokkaido.item.unique()],
        value = 'GDP'
    ),
    dcc.Graph(
        id="hokkaidoGraph",
    )
])

@app.callback(
    dash.dependencies.Output('hokkaidoGraph', 'figure'),
    [dash.dependencies.Input('dropdown-for-hokkaido', 'value')]
)
def update_graph(factor):
    dff = dfhokkaido[dfhokkaido['item'] == factor]

    return {
        'data': [go.Scatter(
            x = dff['year'],
            y = dff['value']
        )]
    }

# 付けたし②
@app.callback(
    dash.dependencies.Output('add-hover-data', 'children'),
    [dash.dependencies.Input('hokkaidoGraph', 'hoverData')]
)
def return_hoverdata(hoverData):
    return json.dumps(hoverData)


if __name__ == '__main__':
    app.run_server(debug=True,port=8051,host='192.168.48.3')
