from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template(
        "index.html",
        title="Home Page"
    )


if __name__ == '__main__':
    app.run(debug=True)
