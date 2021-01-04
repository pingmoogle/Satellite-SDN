from flask import Flask, render_template, request, send_from_directory
from topo.funs import generate

app = Flask(__name__)


@app.route('/')
def login():
    return render_template(
        "login.html",
        title="Login Page"
    )


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template(
        "index.html",
        title="Home Page"
    )


@app.route('/topo', methods=['GET', 'POST'])
def topo():
    if request.method == 'POST':
        topoName = request.form.get("TopoName")
        timeSlice = request.form.get("TimeSlice")
        generate.newgraph(filename=topoName)
        return  render_template(
            "topos/graph_page.html",
            title="Topo Demo",
        )
    generate.newgraph()
    return render_template(
        "topos/graph_page.html",
        title="Topo Demo",
    )


@app.route("/favicon.ico", methods=['GET'])
def icon():
    return app.send_static_file(
        "pic/favicon.ico"
    )


if __name__ == '__main__':
    app.run(debug=True)
