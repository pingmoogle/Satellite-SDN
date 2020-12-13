from flask import Flask, render_template, send_from_directory

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
