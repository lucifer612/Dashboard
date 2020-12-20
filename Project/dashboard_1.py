from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

date_wise_total_csv = pd.read_csv(".\..\data\date_wise_totals.csv")
latest_stat = pd.read_csv(".\..\data\latest_stats.csv")
stock_data = pd.read_csv(".\..\data\data.csv")
reliance_data = pd.read_csv(".\..\data\RELIANCE.NS.csv")
stat_date_wise = pd.read_csv(".\..\data\state_date_wise2.csv")
nifty_pharma= pd.read_csv(".\..\data/nifty pharma.csv")
nifty_it= pd.read_csv(".\..\data/nifty IT.csv")
nifty_fmcg = pd.read_csv(".\..\data/nifty fmcg.csv")
nifty_auto = pd.read_csv(".\..\data/nifty auto.csv")
nifty_finserv = pd.read_csv(".\..\data/nifty finserv.csv")
nifty_media = pd.read_csv(".\..\data/nifty media.csv")
nifty_bank = pd.read_csv(".\..\data/nifty bank.csv")
nifty_realty = pd.read_csv(".\..\data/nifty realty.csv")

def sum_of_confirmed_cases():
    # Safely reassign the filter to a new variable
    total_conf_cases = sum(latest_stat['TotalConfirmed'])
    return total_conf_cases


def sum_of_deaths():
    # Safely reassign the filter to a new variable
    total_deaths = sum(latest_stat['Deaths'])
    return total_deaths


def sum_of_active_cases():
    # Safely reassign the filter to a new variable
    total_active_cases = sum(latest_stat['Active'])
    return total_active_cases


def sum_of_discharged():
    # Safely reassign the filter to a new variable
    total_discharged = sum(latest_stat['Discharged'])
    return total_discharged

insights_it = pd.DataFrame()
insights_it['Day'] = nifty_it['Date']
insights_it['TotalConfirmed'] = date_wise_total_csv['TotalConfirmed']
insights_it['Open'] = nifty_it['Open']
insights_it['Close'] = nifty_it['Close']
insights_it['High'] = nifty_it['High']
#insights_it['Low'] = nifty_it['Low']

insights_it_graph = make_subplots(specs=[[{"secondary_y": True}]])
insights_it_graph.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['TotalConfirmed'], name="total confirmed data",
             ),
    secondary_y=False,
)
insights_it_graph.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['Open'], name="nifty IT Open data"),
    secondary_y=True,
)
insights_it_graph.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['Close'], name="nifty IT Close data"),
    secondary_y=True,
)
insights_it_graph.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['High'], name="nifty IT High data"),
    secondary_y=True,
)
insights_it_graph.update_layout(
     title_text= "Nifty IT and Covid-19 Plot"
)

# # # Set x-axis title
# fig.update_xaxes(title_text="time series")
#
# # # Set y-axes titles
# fig.update_yaxes(title_text="<b>confirmed</b> cases", secondary_y=False)
# fig.update_yaxes(title_text="<b>stock</b> date ", secondary_y=True)
#
insights_pharma = pd.DataFrame()
insights_pharma['Day'] = nifty_pharma['Date']
insights_pharma['TotalConfirmed'] = date_wise_total_csv['TotalConfirmed']
insights_pharma['Open'] = nifty_pharma['Open']
insights_pharma['Low'] = nifty_pharma['Low']
insights_pharma['High'] = nifty_pharma['High']
insights_pharma['Close'] = nifty_pharma['Close']


insights_pharma_graph = make_subplots(specs=[[{"secondary_y": True}]])
insights_pharma_graph.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['TotalConfirmed'], name="total confirmed data"),
    secondary_y=False,
)
insights_pharma_graph.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['Open'], name="nifty pharma Open data"),
    secondary_y=True,
)
insights_pharma_graph.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['Close'], name="nifty pharma Close data"),
    secondary_y=True,
)
insights_pharma_graph.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['High'], name="nifty pharma High data"),
    secondary_y=True,
)
insights_pharma_graph.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['Low'], name="nifty pharma Low data"),
    secondary_y=True,
)
insights_pharma_graph.update_layout(
     title_text= "Nifty Pharma and Covid-19 Plot"
)

insights_fmcg = pd.DataFrame()
insights_fmcg['Day'] = nifty_fmcg['Date']
insights_fmcg['TotalConfirmed'] = date_wise_total_csv['TotalConfirmed']
insights_fmcg['Open'] = nifty_fmcg['Open']
insights_fmcg['Low'] = nifty_fmcg['Low']
insights_fmcg['High'] = nifty_fmcg['High']
insights_fmcg['Close'] = nifty_fmcg['Close']


insights_fmcg_graph = make_subplots(specs=[[{"secondary_y": True}]])
insights_fmcg_graph.add_trace(
    go.Scatter(x=insights_fmcg['Day'], y=insights_fmcg['TotalConfirmed'], name="total confirmed data"),
    secondary_y=False,
)
insights_fmcg_graph.add_trace(
    go.Scatter(x=insights_fmcg['Day'], y=insights_fmcg['Open'], name="nifty FMCG Open data"),
    secondary_y=True,
)
insights_fmcg_graph.add_trace(
    go.Scatter(x=insights_fmcg['Day'], y=insights_fmcg['Close'], name="nifty FMCG Close data"),
    secondary_y=True,
)
insights_fmcg_graph.add_trace(
    go.Scatter(x=insights_fmcg['Day'], y=insights_fmcg['High'], name="nifty FMCG High data"),
    secondary_y=True,
)
insights_fmcg_graph.add_trace(
    go.Scatter(x=insights_fmcg['Day'], y=insights_fmcg['Low'], name="nifty FMCG Low data"),
    secondary_y=True,
)
insights_fmcg_graph.update_layout(
     title_text= "Nifty FMCG and Covid-19 Plot"
)

insights_auto = pd.DataFrame()
insights_auto['Day'] = nifty_auto['Date']
insights_auto['TotalConfirmed'] = date_wise_total_csv['TotalConfirmed']
insights_auto['Open'] = nifty_auto['Open']
insights_auto['Low'] = nifty_auto['Low']
insights_auto['High'] = nifty_auto['High']
insights_auto['Close'] = nifty_auto['Close']


insights_auto_graph = make_subplots(specs=[[{"secondary_y": True}]])
insights_auto_graph.add_trace(
    go.Scatter(x=insights_auto['Day'], y=insights_auto['TotalConfirmed'], name="total confirmed data"),
    secondary_y=False,
)
insights_auto_graph.add_trace(
    go.Scatter(x=insights_auto['Day'], y=insights_auto['Open'], name="nifty AUTO Open data"),
    secondary_y=True,
)
insights_auto_graph.add_trace(
    go.Scatter(x=insights_auto['Day'], y=insights_auto['Close'], name="nifty AUTO Close data"),
    secondary_y=True,
)
insights_auto_graph.add_trace(
    go.Scatter(x=insights_auto['Day'], y=insights_auto['High'], name="nifty AUTO High data"),
    secondary_y=True,
)
insights_auto_graph.add_trace(
    go.Scatter(x=insights_auto['Day'], y=insights_auto['Low'], name="nifty AUTO Low data"),
    secondary_y=True,
)
insights_auto_graph.update_layout(
     title_text= "Nifty AUTO and Covid-19 Plot"
)

insights_finserv = pd.DataFrame()
insights_finserv['Day'] = nifty_finserv['Date']
insights_finserv['TotalConfirmed'] = date_wise_total_csv['TotalConfirmed']
insights_finserv['Open'] = nifty_finserv['Open']
insights_finserv['Low'] = nifty_finserv['Low']
insights_finserv['High'] = nifty_finserv['High']
insights_finserv['Close'] = nifty_finserv['Close']


insights_finserv_graph = make_subplots(specs=[[{"secondary_y": True}]])
insights_finserv_graph.add_trace(
    go.Scatter(x=insights_finserv['Day'], y=insights_finserv['TotalConfirmed'], name="total confirmed data"),
    secondary_y=False,
)
insights_finserv_graph.add_trace(
    go.Scatter(x=insights_finserv['Day'], y=insights_finserv['Open'], name="nifty finserv Open data"),
    secondary_y=True,
)
insights_finserv_graph.add_trace(
    go.Scatter(x=insights_finserv['Day'], y=insights_finserv['Close'], name="nifty finserv Close data"),
    secondary_y=True,
)
insights_finserv_graph.add_trace(
    go.Scatter(x=insights_finserv['Day'], y=insights_finserv['High'], name="nifty finserv High data"),
    secondary_y=True,
)
insights_finserv_graph.add_trace(
    go.Scatter(x=insights_finserv['Day'], y=insights_finserv['Low'], name="nifty finserv Low data"),
    secondary_y=True,
)
insights_finserv_graph.update_layout(
     title_text= "Nifty finserv and Covid-19 Plot"
)


nifty_it_plot = make_subplots(specs=[[{"secondary_y": True}]])
nifty_it_plot.add_trace(
    go.Scatter(x=nifty_it['Date'], y=nifty_it['Open'], name="nifty IT Open data"),

)
nifty_it_plot.add_trace(
    go.Scatter(x=nifty_it['Date'], y=nifty_it['Close'], name="nifty IT Close data"),

)
nifty_it_plot.add_trace(
    go.Scatter(x=nifty_it['Date'], y=nifty_it['High'], name="nifty IT High data"),

)
nifty_it_plot.add_trace(
    go.Scatter(x=nifty_it['Date'], y=nifty_it['Low'], name="nifty IT Low data"),

)

nifty_pharma_plot = make_subplots( specs=[[{"secondary_y": True}]])
nifty_pharma_plot.add_trace(
    go.Scatter(x=nifty_pharma['Date'], y=nifty_pharma['Open'], name="nifty pharma Open data"),

)
nifty_pharma_plot.add_trace(
    go.Scatter(x=nifty_pharma['Date'], y=nifty_pharma['Close'], name="nifty pharma Close data"),

)
nifty_pharma_plot.add_trace(
    go.Scatter(x=nifty_pharma['Date'], y=nifty_pharma['High'], name="nifty pharma High data"),

)
nifty_pharma_plot.add_trace(
    go.Scatter(x=nifty_pharma['Date'], y=nifty_pharma['Low'], name="nifty pharma Low data"),

)


nifty_fmcg_plot = make_subplots( specs=[[{"secondary_y": True}]])
nifty_fmcg_plot.add_trace(
    go.Scatter(x=nifty_fmcg['Date'], y=nifty_fmcg['Open'], name="nifty fmcg Open data"),

)
nifty_fmcg_plot.add_trace(
    go.Scatter(x=nifty_fmcg['Date'], y=nifty_fmcg['Close'], name="nifty fmcg Close data"),

)
nifty_fmcg_plot.add_trace(
    go.Scatter(x=nifty_fmcg['Date'], y=nifty_fmcg['High'], name="nifty fmcg High data"),

)
nifty_fmcg_plot.add_trace(
    go.Scatter(x=nifty_fmcg['Date'], y=nifty_fmcg['Low'], name="nifty fmcg Low data"),

)

nifty_auto_plot = make_subplots( specs=[[{"secondary_y": True}]])
nifty_auto_plot.add_trace(
    go.Scatter(x=nifty_auto['Date'], y=nifty_auto['Open'], name="nifty auto Open data"),

)
nifty_auto_plot.add_trace(
    go.Scatter(x=nifty_auto['Date'], y=nifty_auto['Close'], name="nifty auto Close data"),

)
nifty_auto_plot.add_trace(
    go.Scatter(x=nifty_auto['Date'], y=nifty_auto['High'], name="nifty auto High data"),

)
nifty_auto_plot.add_trace(
    go.Scatter(x=nifty_auto['Date'], y=nifty_auto['Low'], name="nifty auto Low data"),

)


nifty_finserv_plot = make_subplots( specs=[[{"secondary_y": True}]])
nifty_finserv_plot.add_trace(
    go.Scatter(x=nifty_finserv['Date'], y=nifty_finserv['Open'], name="nifty finserv Open data"),

)
nifty_finserv_plot.add_trace(
    go.Scatter(x=nifty_finserv['Date'], y=nifty_finserv['Close'], name="nifty finserv Close data"),

)
nifty_finserv_plot.add_trace(
    go.Scatter(x=nifty_finserv['Date'], y=nifty_finserv['High'], name="nifty finserv High data"),

)
nifty_finserv_plot.add_trace(
    go.Scatter(x=nifty_finserv['Date'], y=nifty_finserv['Low'], name="nifty finserv Low data"),

)



app = dash.Dash(__name__)
app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='./../assets/test.css',
        # href='E:\Study\sem7\BDAD\Project\assets\css.css'
    ),

    # header
    html.Div([
        html.Div(className="header_left",
                 children=html.Div([
                     html.P('DASHBOARD', style={'font-size': '3ex', 'color': 'white'})
                 ])
                 ),

        html.Div(className="header_right",
                 children=html.Div([
                     html.P('Gaining insight on how rise in COVID-19 cases affect stock priceZs of industries',
                            style={'color': 'white', 'font-size': '6', 'padding-right': '3px'})
                 ])
                 ),

    ], className='main_header'),

    # body

    html.Div([
        dcc.Tabs(id='tabs', value='covid', children=[
            dcc.Tab(label='covid', value='covid'),
            dcc.Tab(label='Stock Market', value='stock_market'),
            dcc.Tab(label='Insights', value='insights'),
        ]),
        html.Div(id='tabs-content')
    ])
])


@app.callback(
    [Output('linechart', 'figure'),
     Output('piechart', 'figure'),
     Output('barchart', 'figure'), ],
    [Input('datatable_id', 'selected_rows'),
     Input('piedropdown', 'value'),
     Input('linedropdown', 'value'),
     Input('bardropdown', 'value')]
)
def update_data(chosen_rows, piedropval, linedropval, bardropval):
    if len(chosen_rows) == 0:
        df_filterd = latest_stat[
            latest_stat['Location'].isin(['Kerala', 'Gujarat', 'Punjab', 'Manipur', 'Arunachal Pradesh', 'Chandigarh'])]
    else:
        print(chosen_rows)
        df_filterd = latest_stat[latest_stat.index.isin(chosen_rows)]

    pie_chart = px.pie(
        data_frame=df_filterd,
        names='Location',
        values=piedropval,
        hole=.3,
        labels={'Location': 'States'}
    )

    bar_chart = px.bar(
        data_frame=df_filterd,
        x='Location',
        y=bardropval,
        color='Location',
        labels={'Location': 'States'}
    )
    # extract list of chosen countries
    list_chosen_state = df_filterd['Location'].tolist()
    # filter original df according to chosen countries
    # because original df has all the complete dates
    df_line = stat_date_wise[stat_date_wise['Location'].isin(list_chosen_state)]

    line_chart = px.line(
        data_frame=df_line,
        x='Day',
        y=linedropval,
        color='Location',
        labels={'Location': 'State', 'Day': 'Day'},
    )
    # line_chart.update_layout(uirevision='foo')

    return (pie_chart, line_chart, bar_chart)


# line_chart.update_layout(uirevision='foo')

#
# @app.callback(
#     Output('cases', 'children'),
#     [Input(component_id='stat_dropdown', component_property='value')]
# )
#
# def print_stat_data(stat_dropdown_val):
#     if stat_dropdown_val  = 'Delhi':
#         select_stat = latest_stat['Location']['']
#     # return sum(total_conf_cases)
#     return 'You have selected "{}"'.format(stat_dropdown_val)


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'covid':
        return html.Div([

            # for covid
            html.Div([
                html.Div(
                    children=html.Div([
                        html.H3("Current India's COVID-19 Data"),
                    ])
                ),
                html.Div([
                html.Div([html.Div([
                    html.P("Confirmed", className='text'),
                    html.P(children=sum_of_confirmed_cases(),
                           id='text')],
                    className="mini_container",
                ),
                    html.Div(
                        [html.P("Active", className='text'),
                         html.P(children=sum_of_active_cases(),
                                id='ActiveCases')],
                        # id="totalConfirmed",
                        className="mini_container",
                    ),
                    html.Div(
                        [html.P("Discharged", className='text'),
                         html.P(children=sum_of_discharged(),
                                id='Discharged')],
                        # id="totalConfirmed",
                        className="mini_container",
                    ),
                    html.Div(
                        [html.P("Deaths", className='text'),
                         html.P(children=sum_of_deaths(),
                                id='Deaths')],
                        # id="totalConfirmed",
                        className="mini_container",
                    )],
                    id="info-container",
                    className="row container-display",
                ),],id='covid_info_padding'),

                html.Div(
                    children=html.Div([
                        dash_table.DataTable(
                            id='datatable_id',
                            data=latest_stat.to_dict('records'),
                            columns=[{"name": i, "id": i, "deletable": False, "selectable": False} for i in
                                     latest_stat.columns
                                     ],
                            editable=False,
                            sort_action="native",
                            sort_mode="multi",
                            row_selectable="multi",
                            row_deletable=False,
                            selected_rows=[],
                            # page_action="native",
                            # page_current= 0,
                            # page_size= 6,
                            # page_action='none',
                            style_table={
                                'maxHeight': '40ex',
                                'overflowY': 'scroll',
                                'width': '20ex',
                                'minWidth': '100%',
                            },
                            fixed_rows={'headers': True, 'data': 0},
                            virtualization=True,
                            style_cell_conditional=[
                                {'if': {'column_id': 'Location'},
                                 'width': '25%',
                                 'text-align': 'left'},
                                   {'if': {'column_id': 'TotalConfirmed'},
                                    'width': '20%', 'textAlign': 'left'},
                                   {'if': {'column_id': 'Deaths'},
                                    'width': '20%', 'textAlign': 'left'},
                                   {'if': {'column_id': 'Discharged'},
                                    'width': '20%', 'textAlign': 'left'},
                                   {'if': {'column_id': 'Active'},
                                    'width':  '15%', 'textAlign': 'left'},

                            ],
                        )
                    ],id='table_padding')
                ),
                html.Div(className="",
                         children=html.Div([
                             dcc.Dropdown(id='linedropdown',
                                          options=[
                                              {'label': 'Deaths', 'value': 'Deaths'},
                                              {'label': 'TotalConfirmed', 'value': 'TotalConfirmed'}
                                          ],
                                          value='TotalConfirmed',
                                          multi=False,
                                          clearable=False
                                          ),
                             html.Div([
                                 dcc.Graph(id='piechart'),
                             ]),
                         ],className="covid_line_graph_dropdown_1"),
                         ),
                html.Div(className="pie_and_line_chart",
                         children=html.Div([
                             dcc.Dropdown(id='piedropdown',
                                          options=[{'label': 'Deaths', 'value': 'Deaths'},
                                                   {'label': 'TotalConfirmed', 'value': 'TotalConfirmed'}
                                                   ],
                                          value='TotalConfirmed',
                                          multi=False,
                                          clearable=False
                                          ),
                             html.Div([
                                 dcc.Graph(id='linechart'),
                             ]),
                         ],id='pie_chart_padding'),
                         ),
                html.Div(className="pie_and_line_chart",
                         children=html.Div([
                             dcc.Dropdown(id='bardropdown',
                                          options=[{'label': 'Deaths', 'value': 'Deaths'},
                                                   {'label': 'TotalConfirmed', 'value': 'TotalConfirmed'}
                                                   ],
                                          value='TotalConfirmed',
                                          multi=False,
                                          clearable=False
                                          ),
                             html.Div([
                                 html.Div([
                                     dcc.Graph(id='barchart'),

                                 ])
                             ]),
                         ],id='bar_chart_padding'),
                    ),
            ]),
        ])
    elif tab == 'stock_market':
        return html.Div([
            # # for stock market
            html.Div([
                html.Div(
                         children=html.Div([
                             html.H3("Stock Market Data"),
                         ],id = 'stock_market_data_heading')
                         ),
                html.Div(
                    dcc.Graph(
                        figure=nifty_it_plot,
                     ),
                ),
                html.Div(
                    dcc.Graph(
                        figure=nifty_pharma_plot,
                    ),
                ),
                html.Div(
                    dcc.Graph(
                        figure=nifty_fmcg_plot,
                    ),
                ),
                html.Div(
                    dcc.Graph(
                        figure=nifty_auto_plot,
                    ),
                ),
                html.Div(
                    dcc.Graph(
                        figure=nifty_finserv_plot,
                    ),
                ),

            ])
        ])
    elif tab == 'insights':
        return html.Div([
            html.Div(children = html.Div([
                html.H3('Insights'),
            ],id='insights'),
            ),
            html.Div(
                dcc.Graph(
                    figure=insights_it_graph
                )
            ),
            html.Div(
                html.P(
                    "As we can see just after first few cases of CoVID-19, nifty IT dropped more than 2000 points in 2 weeks."
                    "Just after 2 weeks as the demand for IT services went up, so did the stock of those companies and hence nifty IT gained momentum which led to a new High"
                    , id='insights_p')
            ),

            html.Div(
                dcc.Graph(
                    figure=insights_pharma_graph
                )
            ),

            html.Div(
                html.P(
                    "When the inital wave of CoVID-19 hit, nifty pharma dropped around 1000 points. But as we know the demand for medicines and medical services spiked and so did the stock, which in just 2 weeks rised more than 2000 points"
                    , id='insights_p')
            ),

            html.Div(
                dcc.Graph(
                    figure=insights_fmcg_graph
                )
            ),

            html.Div(
                html.P(
                    "As the first wave of CoVID-19 hit, nifty FMCG dropped approximately 5000 points, just after the lockdown was imposed the demand of consumer goods rised greatly and the stock recovered its previous position within a month."
                    "It wasn't stable though, as we can see it did drop couple 1000 points a few times. Also the stock hasn't gained new highs like that of Nifty IT and Nifty Pharma"
                    , id='insights_p')
            ),

            html.Div(
                dcc.Graph(
                    figure=insights_auto_graph
                )
            ),

            html.Div(
                html.P(
                    "The behavior of nifty auto is similar to nifty FMCG, the rise/recovery of nifty auto was because of increase in demand of personal mobility because of the Pandemic"
                    , id='insights_p')
            ),

            html.Div(
                dcc.Graph(
                    figure=insights_finserv_graph
                )
            ),

            html.Div(
                html.P(
                    "The nifty finserv dipped more than 5000 points during the initial wave and still hasn't recovered fully. The reason being, people are less likely to invest in long term plans,take loans as what comes next is unknown."
                , id='insights_p' )
            ),

        ])

if __name__ == "__main__":
    app.run_server(debug=False)
    #app.run_server(host='0.0.0.0', port=5002)