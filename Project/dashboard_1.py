from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
# import dash_bootstrap_components as dbc
import plotly.express as px

#### ----- Step 1 (import data)----
date_wise_total_csv = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\date_wise_totals.csv")
latest_stat = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\latest_stats.csv")

stat_date_wise = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\state_date_wise2.csv")
#stock = pd.read_csv("E:\Study\sem7\BDAD\stockMarket\HUL_Stock.csv")
#### ----- Step 2 (Plot data)----

# Plot column 'Confirmed'
fig1 = px.bar(date_wise_total_csv, x='Day', y='TotalConfirmed', title="Covid Confirmed Cases")
fig2 = px.bar(date_wise_total_csv, x='Day', y='Deaths', title="Covid Death Cases")


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


#stylesheet = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
#app = dash.Dash(__name__, external_stylesheets=stylesheet)
app = dash.Dash(__name__)
app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='E:\Study\sem7\BDAD\Project\assets\test.css',
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

    ]),

    # body
    html.Div([
        # for covid
        html.Div([
            html.Div(
                children=html.Div([
                    html.H2("COVID-19 Data"),
                ])
            ),
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
            ),

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
                        # style_cell_conditional=[
                        #    {'if': {'column_id': 'Location'},
                        #     'width': '10%', 'textAlign': 'left'},
                        #    {'if': {'column_id': 'Deaths'},
                        #     'width': '30%', 'textAlign': 'left'},
                        #   {'if': {'column_id': 'cases'},
                        #     'width': '30%', 'textAlign': 'left'},
                        #   ],
                    )
                ])
            ),
            html.Div(className="pie_and_line_chart",
                     children=html.Div([
                         dcc.Dropdown(id='linedropdown',
                                      options=[
                                          {'label': 'Deaths', 'value': 'Deaths'},
                                          {'label': 'TotalConfirmed', 'value': 'TotalConfirmed'}
                                      ],
                                      value='Deaths',
                                      multi=False,
                                      clearable=False
                                      ),
                         html.Div([
                             dcc.Graph(id='piechart'),
                         ]),
                     ]),
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
                     ]),
                     ),
        ], className='six column'),
        #
        # # for stock market
        # html.Div([
        #     #        html.Div(className = "column",
        #     #                children=html.Div([
        #     #                    html.H2("Stock Market Data"),
        #     #                    ])
        #     #                ),
        #     #       html.Div(className="latest_stat",
        #     #                  children=html.Div([
        #     dash_table.DataTable(
        #         id='datatable_id2',
        #         data=stat_date_wise.to_dict('records'),
        #         columns=[
        #             {"name": i, "id": i, "deletable": False, "selectable": False} for i in stat_date_wise.columns
        #         ],
        #         editable=False,
        #         sort_action="native",
        #         sort_mode="multi",
        #         row_selectable="multi",
        #         row_deletable=False,
        #         selected_rows=[],
        #         # page_action="native",
        #         # page_current= 0,
        #         # page_size= 6,
        #         # page_action='none',
        #         style_table={
        #             'maxHeight': '35ex',
        #             'overflowY': 'scroll',
        #             'width': '100%',
        #             'minWidth': '100%',
        #         },
        #         fixed_rows={'headers': True, 'data': 0},
        #         virtualization=True,
        #         # style_cell_conditional=[
        #         #     {'if': {'column_id': 'Location'},
        #         #     'width': '10%', 'textAlign': 'left'},
        #         #    {'if': {'column_id': 'Deaths'},
        #         #     'width': '30%', 'textAlign': 'left'},
        #         #   {'if': {'column_id': 'cases'},
        #         #     'width': '30%', 'textAlign': 'left'},
        #         #   ],
        #     )
        # ])

    ], ),
])

@app.callback(
    [Output('linechart', 'figure'),
     Output('piechart', 'figure')],
    [Input('datatable_id', 'selected_rows'),
     Input('piedropdown', 'value'),
     Input('linedropdown', 'value')]
)
def update_data(chosen_rows, piedropval, linedropval):
    if len(chosen_rows) == 0:
        df_filterd = latest_stat[latest_stat['Location'].isin(['Kerala', 'Gujarat', 'Punjab'])]
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

    return (pie_chart, line_chart)


if __name__ == "__main__":
    app.run_server(debug=False)
