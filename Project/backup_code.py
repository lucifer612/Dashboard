import dash 
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Link(
            rel='stylesheet',
            href='E:/Study/sem7/BDAD/Project/assets/test.css'
        ),
    html.H1("DASHBOARD"),
    html.Div([
        html.Div(className = "column",
            children=html.Div([
                html.H2("COVID-19 Data"),
                html.Div('''
                    This is an example of COVID-19 data
                ''')
            ])
        ),
                             
         html.Div(className = "column",
            children=html.Div([
                html.H2("Currency Data"),
                html.Div('''
                    This is an example of CURRENCY data
                ''')
            ])        
        )
   ]),
                         
     html.Div([
       html.Div(className = "graph_column_1",
            children = dcc.Graph(
            className = "sample_graph",
            figure = {
                'data' : [
                    {'x' : [1,2,3] , 'y' : [4,5,6] , 'type' : 'bar' , 'name': 'First Chart' }
                    ],
                'layout' : {
                    'title' : 'Sample Bar Chart',
                    'x-axis' : dict(
                        title = 'x-axis',
                        titlefont = dict(
                        size = 10,
                        color = "black"
                        )),
                    'y-axis' : dict(
                        title = 'y-axis',
                        titlefont = dict(
                        size = 10,
                        color = "blue"
                        ))
                    }
                }
            )
        ),
       
        html.Div(className = "graph_column_1",
            children = dcc.Graph(
            className = "sample_graph_2",
            figure = {
                'data' : [
                    {'x' : [5,3,1] , 'y' : [6,5,4] , 'type' : 'line' , 'name': 'Second Chart' }
                    ],
                'layout' : {
                    'title' : 'Sample line Chart',
                    'x-axis' : dict(
                        title = 'x-axis',
                        titlefont = dict(
                        size = 10,
                        color = "black"
                        )),
                    'y-axis' : dict(
                        title = 'y-axis',
                        titlefont = dict(
                        size = 10,
                        color = "blue"
                        ))
                    }
                }
            )
        ),
   ])                        
                         

])
                     
if __name__ ==  "__main__":
        app.run_server(debug = False)