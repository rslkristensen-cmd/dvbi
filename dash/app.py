from dash import Dash, Input, Output, dcc, html
import plotly.express as px

df = px.data.gapminder()
countries = sorted(df["country"].unique())

app = Dash()
app.layout = [
    html.H1("Life expectancy"),
    dcc.Dropdown(countries, "Denmark", id="country"),
    dcc.Graph(id="graph"),
]

@app.callback(Output("graph", "figure"), Input("country", "value"))
def update_graph(country):
    dff = df[df["country"] == country]
    return px.line(dff, x="year", y="lifeExp")

app.run()