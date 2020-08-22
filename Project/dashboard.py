from dash.dependencies import Input, Output
import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
# For working with geographical data
import dash_table
import dash_bootstrap_components as dbc

import plotly.express as px


#### ----- Step 1 (import data)----
date_wise_total_csv = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\date_wise_totals.csv")
latest_stat = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\latest_stats.csv")
stat_date_wise = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\state_date_wise2.csv")

#### ----- Step 2 (Plot data)----

# Plot column 'Confirmed'
fig1 = px.bar(date_wise_total_csv,  x = 'Day', y = 'TotalConfirmed' , title="Covid Confirmed Cases")
fig2 = px.bar(date_wise_total_csv,  x = 'Day', y = 'Deaths' , title="Covid Death Cases")

app = dash.Dash( )

app.layout = html.Div([
    
    html.Link(
            rel='stylesheet',
            href='E:/Study/sem7/BDAD/Project/assets/test.css'
        ),
  #  html.H1(style:{background: blue} 
  #         "DASHBOARD"),
    
    html.Div([  
        html.Div(className = "header",
            children=html.Div([
                           html.P('DASHBOARD', style={'font-size' : '20' ,'color': 'white'})
            ])
        ),
 
  	 html.Div(className = "header",
            children=html.Div([
                   html.P('Gaining insight on how rise in COVID-19 cases affect stock prices of industries',
                    style={'color': 'white', 'textAlign': 'right' , 'font-size' : '6','padding-right':'3px'})
        
            ])
        ),                            
        
   ]), 
     html.Div([  
        html.Div(className = "column",
            children=html.Div([
                html.H2("COVID-19 Data"),
       
            ])
        ),
                             
         html.Div(className = "column",
            children=html.Div([
                html.H2("Stock Market Data"),
                ])        
            )   
   ]),
    
     html.Div([  
        html.Div(className = "column",
            children=html.Div([
                dash_table.DataTable(
                    id='datatable_id',
                    data=latest_stat.to_dict('records'),
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": False} for i in latest_stat.columns
                        ],
                    editable = False,
                    sort_action="native",
                    sort_mode="multi",
                    row_selectable="multi",
                    row_deletable=False,
                    selected_rows=[],
                    #page_action="native",
                    #page_current= 0,
                    #page_size= 6,
                    #page_action='none',
                    style_cell={
                        "whiteSpace": 'normal'
                   },
                   fixed_rows={ 'headers': True, 'data': 0 },
                   virtualization=False,
                   style_cell_conditional=[
                       {'if': {'column_id': 'Location'},
                        'width': '40%', 'textAlign': 'left'},
                   #    {'if': {'column_id': 'Deaths'},
                   #     'width': '30%', 'textAlign': 'left'},
                   #   {'if': {'column_id': 'cases'},
                   #     'width': '30%', 'textAlign': 'left'},
                      ],
                    )
            ]),
            
            
            
        ),
                             
         html.Div(className = "column",
            children=html.Div([
                    dash_table.DataTable(
                    id='datatable_id1',
                    data=date_wise_total_csv.to_dict('records'),
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": False} for i in date_wise_total_csv.columns
                        ],
                    editable = True,
                    sort_action="native",
                    sort_mode="multi",
                    row_selectable="multi",
                    row_deletable=False,
                    selected_rows=[],
                    #below three togather 
                    #page_action="native",
                    #page_current= 0,
                    #page_size= 6,
                   
                    #below three togather
                    page_action='none',
                    style_cell={
                        "whiteSpace": 'normal'
                    },
                    fixed_rows={ 'headers': True, 'data': 0 },
                    virtualization=False,
                    style_cell_conditional=[
                        {'if': {'column_id': 'Day'},
                         'width': '20%', 'textAlign': 'left'},
                    #    {'if': {'column_id': 'deaths'},
                    #     'width': '30%', 'textAlign': 'left'},
                    #    {'if': {'column_id': 'cases'},
                    #     'width': '30%', 'textAlign': 'left'},
                        ],
                    )
                    
                ])        
            )  ,
         
         
         
   ]),         
   
     html.Div([
        html.Div([
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'Deaths', 'value': 'Deaths'},
                         {'label': 'TotalConfirmed', 'value': 'TotalConfirmed'}
                ],
                value='Deaths',
                multi=False,
                clearable=False
            ),
        ]),

        html.Div([
        dcc.Dropdown(id='piedropdown',
            options=[
                    {'label': 'Deaths', 'value': 'Deaths'},
                    {'label': 'TotalConfirmed', 'value': 'TotalConfirmed'}
            ],
            value='TotalConfirmed',
            multi=False,
            clearable=False
        ),
        ]),

    ]),

    html.Div([
        html.Div([
            dcc.Graph(id='linechart'),
        ]),

        html.Div([
            dcc.Graph(id='piechart'),
        ]),

    ]),


    html.Div([  
        html.Div(className = "column",
            children=html.Div([
                html.Div(className = "column",
                         children = dcc.Graph(
                             className = "sample_graph",
                             figure = fig1
                        )
                    ),
            ])
        ),
                             
         html.Div(className = "column",
            children=html.Div([
                html.Div(className = "column",
                         children =  dcc.Graph(
                             className = "sample_graph_2",
                             
                             )
                         ),
                    
                ])        
            )   
   ]),
                         
    html.Div([  
        html.Div(className = "column",
            children=html.Div([
                #html.H2("COVID-19 Data"),
                #html.Div('''
                #    This is an example of COVID-19 data
                #'''),
                html.Div(className = "column",
                         children = dcc.Graph(
                             className = "sample_graph",
                             figure = fig2
                        )
                    ),
            ])
        ),
                             
         html.Div(className = "column",
            children=html.Div([
                #html.H2("Stock Market Data"),
                #html.Div('''
                #    This is an example of Stock Market data
                #'''),
                html.Div(className = "column",
                         children =  dcc.Graph(
                             className = "sample_graph_2",
                             
                             )
                         ),
                    
                ])        
            )   
   ]),         
             
    

])
   

@app.callback(
    [Output('linechart', 'figure'),
     Output('piechart', 'figure')],
    [Input('datatable_id', 'selected_rows'),
     Input('piedropdown', 'value'),
     Input('linedropdown', 'value')]
)
def update_data(chosen_rows,piedropval,linedropval):
    if len(chosen_rows)==0:
        df_filterd = latest_stat[latest_stat['Location'].isin(['Kerala','Gujarat','Punjab'])]
    else:
        print(chosen_rows)
        df_filterd = latest_stat[latest_stat.index.isin(chosen_rows)]

    pie_chart=px.pie(
            data_frame=df_filterd,
            names='Location',
            values=piedropval,
            hole=.3,
            labels={'Location':'States'}
            )

    #extract list of chosen countries
    list_chosen_countries=df_filterd['Location'].tolist()
    #filter original df according to chosen countries
    #because original df has all the complete dates
    df_line = stat_date_wise[stat_date_wise['Location'].isin(list_chosen_countries)]

    line_chart = px.line(
            data_frame=df_line,
            x='Day',
            y=linedropval,
            color='Location',
            labels={'Location':'State', 'Day':'Day'},
            )
    #line_chart.update_layout(uirevision='foo')

    return (pie_chart,line_chart)
                  
if __name__ ==  "__main__":
        app.run_server(debug = False)