import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
country = []
num = []
city = []
perform = []
data = {'Countries': country, 'IP addresses which is only threat': num,
        'Perform': perform}
with open('dif_threat_ip2.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:

        country.append(row['country'])
        num.append(row['ip'])
        perform.append(row['perform'])

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame(
    data, columns=['Countries', 'IP addresses which is only threat', 'Perform'])

fig = px.bar(df, x="IP addresses which is only threat", y="Countries",
             color="Perform", barmode="group")

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
