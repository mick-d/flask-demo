from flask import Flask, render_template, request, redirect
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from bokeh.plotting import figure
from bokeh.embed import components

plot = figure()
plot.circle([1,2], [3,4])
script, div = components(plot)

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index_bs.html')

@app.route('/stock_plot')
def bokeh_plot():
  return render_template('bokeh_plot_bs.html', script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)
