from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template(
        "index.html",
        title="Home Page"
    )


@app.route('/topo', methods=['GET', 'POST'])
def topo():
    return render_template(
        "topoExample.html",
        title="Topo Demo"
    )


@app.route('/topographs/<graphname>')
def topographs(graphname):
    return render_template(
        "topos/"+graphname,
        title="Topo Demo"
    )


if __name__ == '__main__':
    app.run(debug=True)
