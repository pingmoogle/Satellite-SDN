import re, json

from flask import Flask, render_template, request
from topo.funs import generate2, seekFile, users

app = Flask(__name__)

differentHandlers = {
    "txt": generate2.txt2jsseries,
    "gml": generate2.gml2jsseries,
    "json": generate2.json2jsseries,
    "txt.json": generate2.json2jsseries,
    "gml.json": generate2.json2jsseries
}


@app.route('/', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET':
        return render_template(
            "login.html",
            title="Login Page"
        )
    if request.method == 'POST':
        username = request.form.get("username")
        userpassword = request.form.get("userpassword")
        result = users.userCheck(username, userpassword)
        if result is not False:
            return highlevel(username=result)


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template(
        "index.html",
        title="Home Page"
    )


@app.route('/highlevel', methods=['GET', 'POST'])
def highlevel(username=" "):
    if request.method == 'POST':
        timeSlice = request.form.get("sliderTime")
        if timeSlice == None: timeSlice = 0
        nodes, links = generate2.json2jsseries("topo.json", int(timeSlice))

        return render_template("topos/highlevel.html", nodes=nodes, links=links, timeNow=timeSlice, userName=username)
    nodes, links = generate2.json2jsseries("topo.json")
    return render_template("topos/highlevel.html", nodes=nodes, links=links, timeNow="0",
                           title="高空网络", userName=username)


@app.route('/lowlevel')
def lowlevel():
    nodes, links = generate2.json2jsseries("topo66.json")
    # nodes, links = generate2.txt2jsseries("D:\\Document\\satellite-sdn\\topo\data\\topo2.txt")
    return render_template('topos/lowlevel.html', nodes=nodes, links=links, title="低空网络")


@app.route('/diy', methods=['GET', 'POST'])
def diy():
    if request.method == "POST":
        newfile = request.files["newFile"]
        newfileName = seekFile.uploadFile(newfile)
        a1 = re.search('(\..*)', newfileName).group(1)
        nodes, links = differentHandlers[a1[1:]](filename=newfileName)
        fh = seekFile.fileHistroy()
        return render_template("topos/diy.html", nodes=nodes, links=links, timeNow="0", fileHistoryList=fh,
                               fileName=newfileName, title="DIY")
    if request.method == "GET":
        nodes, links = generate2.json2jsseries(filename="topo.json")
        fh = seekFile.fileHistroy()
        return render_template("topos/diy.html", nodes=nodes, links=links, timeNow="0", fileHistoryList=fh,
                               title="DIY")


@app.route('/diy-history', methods=['POST'])
def diyHistory():
    choice = request.form.get("fileHistory")
    a1 = re.search('(\..*)', choice).group(1)
    nodes, links = differentHandlers[a1[1:]](filename=choice)
    fh = seekFile.fileHistroy()
    return render_template("topos/diy.html", nodes=nodes, links=links, timeNow="0", fileHistoryList=fh,
                           fileName=choice, title="DIY")


@app.route('/save-changes', methods=["POST"])
def saveChanges():
    # filename = request.form.get("fileName")
    changesAll = json.loads(request.get_data(as_text=True))
    print(changesAll)

    generate2.appendAction(changesAll.pop("fileName"), changesAll)
    return 'OK', 200


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
