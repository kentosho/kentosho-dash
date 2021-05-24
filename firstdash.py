import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
        children = [
            html.H1('Hello Dash',),
            dcc.Graph(
                id = "first-graph",
                figure = {
                    'data': [
                        {'x': [1,2,3,4],
                        'y':[3,2,4,6],
                        'type': 'bar',
                        'name': 'Tokyo'},
                        {'x':[1,2,3,4],
                        'y':[2,4,3,2],
                        'type': 'bar',
                        'name': 'Osaka'}
                    ],
                    'layout': {
                        'title': 'Graph1 Tokyo vs Osaka'
                    }
                    }
                )
            ])
if __name__=='__main__':
    app.run_server(debug=True,host='192.168.48.3',port=8051)
