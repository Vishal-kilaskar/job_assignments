from flask import Flask, render_template
import plotly.express as px


my_app = Flask(__name__)
my_app.debug = True


@my_app.route('/')
def home():
    print(__name__)
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    fig.write_html(file='./templates/chart.html')
    return render_template('home.html')


if __name__ == '__main__':
    my_app.run(debug=True)
