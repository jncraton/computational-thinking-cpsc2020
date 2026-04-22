from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def square():
    result = ""
    if request.args.get('num'):
        result = float(request.args.get('num')) ** 2

    return f"""
        <form>
            <input name=num autofocus />
            <input type=submit value=Square />
        </form>
        {result}
    """

if __name__ == '__main__':
    app.run(debug=True)
