from flask import Flask, render_template, request, send_from_directory
from topo.funs import generate, generate2

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


@app.route('/topoexample', methods=['GET', 'POST'])
def topo():
    if request.method == 'POST':
        topoName = request.form.get("TopoName")
        timeSlice = request.form.get("sliderTime")
        generate.newgraph(topoName, int(timeSlice))
        return render_template(
            "topos/graph_page.html",
            title="Topo Demo",
        )
    generate.newgraph()
    return render_template(
        "topos/graph_page.html",
        title="Topo Demo",
    )


@app.route('/highlevel', methods=['GET', 'POST'])
def highlevel():
    if request.method == 'POST':
        timeSlice = request.form.get("sliderTime")
        nodes, links = generate2.json2jsseries("topo.json", int(timeSlice))
        return render_template("topos/highlevel.html", nodes=nodes, links=links, timeNow=timeSlice)
    nodes, links = generate2.json2jsseries("topo.json")
    return render_template("topos/highlevel.html", nodes=nodes, links=links, timeNow="0")


@app.route('/lowlevel')
def lowlevel():
    nodes, links = generate2.json2jsseries("topo66.json")
    return render_template('topos/lowlevel.html', nodes=nodes, links=links)


@app.route('/surfacelevel')
def surfacelevel():
    # TODO: 生成series字符串
    return render_template('topos/surfacelevel.html')


@app.route("/terminal")
def newTerminal():
    return render_template("terminal.html")

@app.route("/favicon.ico", methods=['GET'])
def icon():
    return app.send_static_file(
        "pic/favicon.ico"
    )


if __name__ == '__main__':
    app.run(debug=True)
