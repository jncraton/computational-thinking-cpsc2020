from flask import Flask

app = Flask(__name__)

@app.route("/pages/1")
def page1():
    return "Page 1 <a href=/pages/2>Go to page 2</a>"

@app.route("/pages/2")
def page2():
    return "Page 2 <a href=/pages/1>Go to page 1</a>"

if __name__ == '__main__':
    app.run(debug=True)
