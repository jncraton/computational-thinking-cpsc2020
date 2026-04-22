from flask import Flask, request, session
import languagemodels

app = Flask(__name__)
app.secret_key = "FyJYMJmwZUWASo5J"

@app.route("/")
def home():
    if not "history" in session:
        session["history"] = ""

    usertext = request.args.get("usertext", "")

    if usertext:
        session["history"] += f"<p>User: {usertext}"

        response = languagemodels.do(f"Respond to a user: {usertext}")
        session["history"] += f"<p>Bot: {response}"

    return f"""
        {session['history']}
        <form action=/>
        <textarea type=text name=usertext autofocus></textarea>
        <input type=submit />
        </form>
        """

if __name__ == '__main__':
    app.run(debug=True)
