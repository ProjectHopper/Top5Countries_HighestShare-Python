from dash import html, dcc
import plotly.express as px

def render(app, data):
    fig=px.bar(data, x='Trill', y='country', orientation ="h")
    return html.Div(dcc.Graph(figure=fig), id="bar-h-chart")
