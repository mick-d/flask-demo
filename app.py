from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

plot = figure()
plot.circle([1,2], [3,4])
test_html = file_html(plot, CDN, "my plot")

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/stock_plot')
def plot():
  return test_html

if __name__ == '__main__':
  app.run(port=33507)
