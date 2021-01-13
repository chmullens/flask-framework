from flask import Flask, render_template, request, redirect
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, PreText, Select
from bokeh.plotting import figure

DEFAULT_TICKERS = ['AAPL', 'GOOG', 'INTC', 'BRCM', 'YHOO']

app = Flask(__name__)
#Simple edit.

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/stockplotter')
def stockplotter:
    return render_template('stockplotter.html')


@app.route('/plot', methods=['POST'])
def plot():
    #This is a dictionary-like object that contains the info
    #contained in the request. Since he called the form "my_name",
    #you'll call that for the form.
    first_name = request.form["my_name"]
    full_name = create_plot(first_name)

    #Here, we'd render a new plot template... which could
    #include the rendering of a button itself.
    return full_name


if __name__ == '__main__':
  app.run(port=33507)
