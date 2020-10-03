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

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['TotalConfirmed'], name="total confirmed data"),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['Open'], name="nifty IT Open data"),
    secondary_y=True,
)
fig.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['Close'], name="nifty IT Close data"),
    secondary_y=True,
)
fig.add_trace(
    go.Scatter(x=insights_it['Day'], y=insights_it['High'], name="nifty IT High data"),
    secondary_y=True,
)


# # Add figure title
# fig.update_layout(
#     title_text="stock open date and total confirmed cases"
# )
#
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


fig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['TotalConfirmed'], name="total confirmed data"),
    secondary_y=False,
)
fig1.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['Open'], name="nifty pharma Open data"),
    secondary_y=True,
)
fig1.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['Close'], name="nifty pharma Close data"),
    secondary_y=True,
)
fig1.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['High'], name="nifty pharma High data"),
    secondary_y=True,
)
fig1.add_trace(
    go.Scatter(x=insights_pharma['Day'], y=insights_pharma['Low'], name="nifty pharma Low data"),
    secondary_y=True,
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
                        figure=px.line(stock_data, x="Date", y="Open" , title = 'NIFTY Open Data'))

                ),
                dcc.Graph(
                    figure=px.line(reliance_data, x="Date", y="Open" ,title='Reliance Stock Open Data' )

                )
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
                    figure=fig
                )
            ),
            html.Div(
                dcc.Graph(
                    figure=fig1
                )
            )
        ])

if __name__ == "__main__":
    app.run_server(debug=False)