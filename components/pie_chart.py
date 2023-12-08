from dash import html, dcc
import plotly.express as px

def render(app, data):
    fig = px.pie(data, values='Trill', names='country', title='<b>The Top 5 Countries with the Highest Share of Large Companies in the World</b>')
    return html.Div([dcc.Graph(figure=fig)], id="pie-chart")
