import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
continent = []
num = []
data = {'continent': continent, 'Number of each ip´s': num}
with open('../fixed_data/continents/continent_list.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:

        continent.append(row['continent'])
        num.append(int(row['number']))


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame(
    data, columns=['continent', 'Number of each ip´s'])

fig = px.bar(df, x="continent", y="Number of each ip´s",
             color="continent", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[


    html.Div(children='Shows the number of ip\'s', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
